#!/usr/bin/env python3
"""lineage_runner.py — run a multi-generation Chat Bridge lineage with carried memory.

Goal: test whether inherited history changes an inquiry's trajectory/depth/geometry.

Protocol (the "cheap" version — does NOT touch the bridge's internals):
  - Runs the same persona pair repeatedly for N generations.
  - Each generation inherits a rolling LINEAGE (distilled conclusions of prior gens).
  - Each generation's transcript + the growing lineage are saved to --out.
  - After the last generation it runs an AMNESIA-STRIP (fresh run, no lineage).

Usage:
  python3 lineage_runner.py --a PersonaA --b PersonaB \
      --starter "topic text" --gens 5 --out /path/to/dir [--rounds 6]

Fixed 2026-11-09: startup no longer shell-string-interpolates the starter. It uses a
subprocess ARGUMENT LIST, so arbitrary text in the carried lineage (apostrophes,
double quotes, newlines) no longer breaks the command. This was the gen-3 crash.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime

BRIDGE = "/home/dev/.openclaw/workspace/skills/chat-bridge/bridge.py"
LAST_TURN_CHARS = 900


def start_chat(a, b, starter, rounds, requested_by):
    """Start a chat; returns conversation_id, or None on failure."""
    cmd = [sys.executable, BRIDGE, "start",
           "--a", a, "--b", b,
           "--starter", starter,
           "--rounds", str(rounds),
           "--requested-by", requested_by]
    p = subprocess.run(cmd, capture_output=True, text=True)
    try:
        data = json.loads(p.stdout)
        return data.get("conversation_id")
    except Exception:
        sys.stderr.write("[lineage_runner] start failed:\n" + p.stdout + "\n" + p.stderr + "\n")
        return None


def wait_chat(cid, timeout=600):
    p = subprocess.run([sys.executable, BRIDGE, "wait", cid, "--timeout", str(timeout)],
                       capture_output=True, text=True)
    return p.returncode


def get_transcript(cid):
    p = subprocess.run([sys.executable, BRIDGE, "transcript", cid],
                       capture_output=True, text=True)
    return p.stdout


def last_turn(text):
    """Crude distill: the text of the final '## Persona' section."""
    parts = re.split(r"\n## ", text)
    if not parts:
        return ""
    last = parts[-1]
    lines = last.split("\n", 1)
    body = lines[1] if len(lines) > 1 else last
    return body.strip()


def run_generation(a, b, starter, rounds, requested_by):
    cid = start_chat(a, b, starter, rounds, requested_by)
    if not cid:
        return None, None, "start-failed"
    rc = wait_chat(cid)
    if rc != 0:
        return cid, None, "wait-timeout"
    transcript = get_transcript(cid)
    return cid, transcript, None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True)
    ap.add_argument("--b", required=True)
    ap.add_argument("--starter", required=True)
    ap.add_argument("--gens", type=int, default=5)
    ap.add_argument("--rounds", type=int, default=6)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    outdir = args.out or ("/home/dev/.openclaw/workspace/exports/lineage-" + ts)
    os.makedirs(outdir, exist_ok=True)

    base_starter = args.starter
    lineage = []

    for gen in range(1, args.gens + 1):
        if gen == 1:
            starter = base_starter
        else:
            memory = "\n".join("(Gen %d) %s" % (i + 1, x) for i, x in enumerate(lineage))
            starter = (
                "Continuation of your lineage — generation %d. "
                "Here is what you concluded across prior generations:\n%s\n\n"
                "Build on this. Do not re-derive settled ground; push only what is unresolved."
                % (gen, memory)
            )
        cid, transcript, err = run_generation(args.a, args.b, starter, args.rounds,
                                               "lineage-run gen%d" % gen)
        if transcript is None:
            sys.stderr.write("[lineage_runner] generation %d failed: %s\n" % (gen, err))
            sys.exit(1)

        with open(os.path.join(outdir, "gen%02d.txt" % gen), "w") as f:
            f.write(transcript)

        lineage.append(last_turn(transcript)[:LAST_TURN_CHARS])
        print("gen %d: conversation=%s chars=%d" % (gen, cid, len(transcript)), flush=True)

    with open(os.path.join(outdir, "LINEAGE.md"), "w") as f:
        f.write("# Lineage\n\n")
        f.write("\n\n".join("(Gen %d) %s" % (i + 1, x) for i, x in enumerate(lineage)))

    # Amnesia strip
    cid, transcript, err = run_generation(args.a, args.b, base_starter,
                                          args.rounds, "lineage-run amnesia-strip")
    if transcript is not None:
        with open(os.path.join(outdir, "amnesia_strip.txt"), "w") as f:
            f.write(transcript)
        print("amnesia-strip: conversation=%s chars=%d" % (cid, len(transcript)), flush=True)
    else:
        print("amnesia-strip: failed (%s)" % err, flush=True)

    print("\n[done] output dir: " + outdir, flush=True)


if __name__ == "__main__":
    main()
