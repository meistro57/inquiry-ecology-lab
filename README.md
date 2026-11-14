# Inquiry Ecology Lab



An experimental field notebook for studying how two AI personas, run through
Mark's Chat Bridge, generate *concepts* — and whether the machinery (pairing,
starter framing, and memory) changes what they produce.

The core discovery, in one line:

> **The research unit moved from "persona" to "inquiry ecology."**
> Two personas with fixed invariants form a *pairing* whose geometry — not the
> personas' individual identities — sets the domain of what gets discussed, while
> the *starter* sets the stance and the *interaction* assigns roles.

## What's in here

- `GLOSSARY.md` — the working vocabulary, so a finding can't be mistaken for a vibe.
- `CONCEPTS.md` — the "hall of fame": the most generative ideas, with an honest note
  on which ones have actually survived pressure-testing vs. which are still pretty.
- `EXPERIMENTS.md` — the run catalog: pairing → domain / form / roles / product.
- `METRICS.md` — the scoring dimensions (Compression Resistance, Meta-Ascent Depth,
  Memory-Passing Robustness).
- `scripts/lineage_runner.py` — the multi-generation "living memory" runner
  (carries each generation's conclusions forward, then runs an amnesia-strip).
- `scripts/usage_chart.py` — the DeepSeek spend chart (cairosvg -> PNG).
- `scripts/check_site.py` — drift check: reports when the source markdown (CONCEPTS/CLOCK/EXPERIMENTS/DECISIONS) has pulled ahead of the published site files (graph/concepts.json + index.html). Run it before assuming the site is current.

## The headline findings so far

1. **Pairing sets the domain; starter sets the form/stance; interaction sets roles.**
   The same persona can be a "generator" in one pairing and a "limiter" in another.
   Roles are verbs, not nouns.
2. **Convergence does not imply synthesis.** Every run converges (it's an
   architectural prior), so "they converged" is not a success condition. What matters
   is *what the convergence did* — preserved a distinction, reconciled, or papered it over.
3. **Memory changes trajectory, not geometry.** The deep "attractor" (a core insight)
   is re-derivable from scratch; the *distinctions* and vocabulary are memory-carried
   and die under an amnesia-strip.
4. **The organism was the pond.** Memory can be external-but-constitutive (ants,
   beaver dams, a notebook). The individual session is stateless; the *ecology*
   (personas, transcripts, glossary) is what accumulates.

## Running the lineage experiment

```bash
python3 scripts/lineage_runner.py \
  --a Negative_Space_Tracker \
  --b Density_Tracker \
  --starter "A topic to work with: what is shaped by absence." \
  --gens 8 --rounds 6 --out /tmp/lineage
```

Each generation inherits the prior generations' distilled conclusions as memory.
The final output includes an `amnesia_strip.txt` — a fresh run with no memory, to
see what survives the wipe.

## Status

Early days. Everything here is a *candidate signature*, not a law. Most findings are
still **Untested** until they've been deliberately stress-tested (see METRICS.md and
the "Compression Resistance" scores in CONCEPTS.md).
