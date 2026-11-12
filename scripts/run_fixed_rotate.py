#!/usr/bin/env python3
"""run_fixed_rotate.py — CLOCK-014: FIXED vs ROTATING operator-bearing lineage.

Arm FIXED:   the same five operator-steps, same order, every generation.
Arm ROTATING: the same five operator-steps, a different order each generation
              (rotated by generation index).
Both arms carry a conclusion-lineage (last-turn distill) and end with an AMNESIA-STRIP
(topic only — no scaffold, no carry) to reveal whether the narrowing lived in the
memory-of-the-bearing or in the attractor/geometry.

Usage:
  python3 run_fixed_rotate.py --a Cycle_Agent --b Threshold_Agent \
      --topic "A topic to work with: death and renewal within human communities." \
      --gens 6 --out /path/to/dir [--rounds 6]
"""
import argparse, json, os, re, subprocess, sys
from datetime import datetime

BRIDGE = "/home/dev/.openclaw/workspace/skills/chat-bridge/bridge.py"
LAST_TURN_CHARS = 900

# The five operator-steps (Reflector, Generator, Limiter, Valuator, Steward)
STEPS = [
    "Name what is already present but not yet examined.",
    "What new possibilities open when those are taken seriously?",
    "Which of those possibilities encounter real constraints?",
    "Of what remains, which seem most worth keeping?",
    "What conditions would let what is kept continue?",
]

def start_chat(a, b, starter, rounds, requested_by):
    cmd = [sys.executable, BRIDGE, "start", "--a", a, "--b", b,
           "--starter", starter, "--rounds", str(rounds), "--requested-by", requested_by]
    p = subprocess.run(cmd, capture_output=True, text=True)
    try:
        return json.loads(p.stdout).get("conversation_id")
    except Exception:
        sys.stderr.write("[run_fixed_rotate] start failed:\n" + p.stdout + "\n" + p.stderr + "\n")
        return None

def wait_chat(cid, timeout=600):
    return subprocess.run([sys.executable, BRIDGE, "wait", cid, "--timeout", str(timeout)],
                          capture_output=True, text=True).returncode

def get_transcript(cid):
    return subprocess.run([sys.executable, BRIDGE, "transcript", cid],
                          capture_output=True, text=True).stdout

def last_turn(text):
    parts = re.split(r"\n## ", text)
    if not parts:
        return ""
    last = parts[-1]
    lines = last.split("\n", 1)
    return (lines[1] if len(lines) > 1 else last).strip()

def scaffold_text(order):
    lines = ["Work through this in order, each step as an operation:"]
    lines += ["%d. %s" % (i+1, STEPS[idx]) for i, idx in enumerate(order)]
    return "\n".join(lines)

def run_gen(a, b, starter, rounds, tag):
    cid = start_chat(a, b, starter, rounds, tag)
    if not cid:
        return None, "start-failed"
    if wait_chat(cid) != 0:
        return None, "wait-timeout"
    return get_transcript(cid), None

def run_arm(a, b, topic, mode, gens, rounds, outdir, arm_name):
    """mode = 'fixed' or 'rotate'. Returns list of transcripts + the amnesia transcript."""
    os.makedirs(os.path.join(outdir, arm_name), exist_ok=True)
    lineage = []
    for gen in range(1, gens + 1):
        if mode == "fixed":
            order = list(range(5))
        else:
            order = [(gen - 1 + k) % 5 for k in range(5)]
        scaff = scaffold_text(order)
        if gen == 1:
            starter = topic + "\n\n" + scaff
        else:
            mem = "\n".join("(Gen %d) %s" % (i+1, x) for i, x in enumerate(lineage))
            starter = topic + "\n\n" + scaff + "\n\nCarried prior conclusions:\n" + mem + "\n\nPush only what is unresolved."
        tx, err = run_gen(a, b, starter, rounds, "cline-014-%s-gen%d" % (arm_name, gen))
        if tx is None:
            sys.stderr.write("[run_fixed_rotate] %s gen %d failed: %s\n" % (arm_name, gen, err))
            return lineage, None
        with open(os.path.join(outdir, arm_name, "gen%02d.txt" % gen), "w") as f:
            f.write(tx)
        lineage.append(last_turn(tx)[:LAST_TURN_CHARS])
        print("[%s] gen %d done (%d chars)" % (arm_name, gen, len(tx)), flush=True)
    # amnesia strip
    tx, err = run_gen(a, b, topic, rounds, "cline-014-%s-amnesia" % arm_name)
    if tx is not None:
        with open(os.path.join(outdir, arm_name, "amnesia_strip.txt"), "w") as f:
            f.write(tx)
    else:
        sys.stderr.write("[run_fixed_rotate] %s amnesia strip failed: %s\n" % (arm_name, err))
    return lineage, tx

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--a", required=True)
    ap.add_argument("--b", required=True)
    ap.add_argument("--topic", required=True)
    ap.add_argument("--gens", type=int, default=6)
    ap.add_argument("--rounds", type=int, default=6)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    outdir = args.out or ("/home/dev/.openclaw/workspace/exports/cline014-" + datetime.now().strftime("%Y%m%d-%H%M%S"))
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "STEPS.txt"), "w") as f:
        f.write("\n".join(STEPS))
    print("[cli014] fixed arm...", flush=True)
    run_arm(args.a, args.b, args.topic, "fixed", args.gens, args.rounds, outdir, "FIXED")
    print("[cli014] rotating arm...", flush=True)
    run_arm(args.a, args.b, args.topic, "rotate", args.gens, args.rounds, outdir, "ROTATING")
    print("[cli014] DONE -> " + outdir, flush=True)

if __name__ == "__main__":
    main()
