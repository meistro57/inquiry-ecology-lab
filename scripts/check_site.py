#!/usr/bin/env python3
"""Detect whether the inquiry-ecology-lab website has drifted behind its source.

The site (graph/concepts.json + index.html) renders from GitHub Pages on a push to
main, but those two files are the *output* of a hand-study of CONCEPTS.md / CLOCK.md /
EXPERIMENTS.md / DECISIONS.md. They fell behind not because anything broke, but because
nothing noticed when the source-of-truth markdown moved ahead of the site files.

This script reports drift — safely and non-destructively. It does NOT rewrite the
graph (the node ids, scores, and edges are human judgment with no machine-derivable
key; naive regeneration would duplicate nodes). It just answers one question:

    Is the source markdown newer than the published site files?

Usage:
  python3 scripts/check_site.py            # exit 0 if current, 1 if stale
"""
import subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ["CONCEPTS.md", "CLOCK.md", "EXPERIMENTS.md", "DECISIONS.md"]
SITE = ["graph/concepts.json", "index.html"]

def last_commit(repo, path):
    out = subprocess.run(
        ["git", "-C", str(repo), "log", "-1", "--format=%ct", "--", path],
        capture_output=True, text=True
    )
    return int(out.stdout.strip() or 0)

def main():
    newest_source = max(last_commit(ROOT, p) for p in SOURCES)
    newest_site = max(last_commit(ROOT, p) for p in SITE)

    src_name = SOURCES[0]
    for p in SOURCES:
        if last_commit(ROOT, p) == newest_source:
            src_name = p
            break

    if newest_source > newest_site:
        print(f"STALE: {src_name} (commit {newest_source}) is newer than the site files ({newest_site}).")
        print("Run the site-refresh procedure to add new concept nodes + prose, then push.")
        sys.exit(1)
    else:
        print("current: site files are up to date with the source markdown.")
        sys.exit(0)

if __name__ == "__main__":
    main()
