# The Clock — frozen predictions (v0.1)

The consequence ledger. The correspondence/calibration run taught us the rule:
**a claim is only scoreable if its prior is frozen before the outcome.** A git
commit is a frozen needle — the timestamp here is the locked prior.

Each prediction carries: claim · confidence · what would falsify it · how it resolves.
Status is `pending` until a future run scores it. These are bridge-*behavior*
predictions (testable by running the bridge), deliberately chosen over the
conceptual distinctions (which are tools, not claims).

Frozen via commit timestamp: 2026-11-10.

---

## CLOCK-001 — same-function → meta is graded, not binary
> A same-function pairing of **non-recursive** operators meta-regresses **shallow**
> (depth ≤ 1); a same-function pairing of **self-recursive** operators (limit /
> classify / invisibility) meta-regresses **deep** (depth ≥ 3).
- **confidence:** 0.72
- **falsifies if:** a non-recursive same-function pair regresses deep, *or* a
  recursive pair regresses shallow.
- **resolves:** run 2 more same-function pairs (one each kind), measure meta-depth.

## CLOCK-002 — role mobility is starter-driven
> Holding a pairing fixed, a pointed starter that puts one invariant on the
> defensive inverts the roles (the defensive one becomes the limiter); a neutral
> starter does not invert.
- **confidence:** 0.70
- **falsifies if:** role inversion occurs under neutral starter, or fails to occur
  under a pointed starter.
- **resolves:** a replication block varying only starter valence.

## CLOCK-003 — attractor survives, distinctions die
> An amnesia-strip after ≥ 4 generations of carried memory re-derives the base
> attractor but drops all lineage-specific vocabulary.
- **confidence:** 0.85
- **falsifies if:** the stripped run re-derives the lineage vocabulary, *or* fails
  to re-derive the base attractor.
- **resolves:** one more amnesia-strip on a *different* pair (not Negative Space × Density).

## CLOCK-004 — terminology speciates by ~gen 2–3
> A carried-memory lineage shifts its dominant metaphor/domain-vocabulary by
> generation 2–3 of accumulation.
- **confidence:** 0.60
- **falsifies if:** a fresh lineage keeps one metaphor stable across 4+ generations.
- **resolves:** trace metaphor continuity across a fresh lineage.

## CLOCK-005 — operator distribution predicts product class
> A generator-dominant distribution (≥60% generate) yields proliferation or
> taxonomy; a limiter-adjacent balanced distribution yields refinement or protocol.
- **confidence:** 0.55
- **falsifies if:** ≥3 future runs show the opposite pairing (limiter-heavy → proliferation).
- **resolves:** score operator distribution + product on ≥5 future runs.

## CLOCK-006 — convergence is near-constant (the null)
> ≥90% of future 6-round runs converge (reach closure) regardless of pairing.
- **confidence:** 0.90
- **falsifies if:** >20% of the next 10 runs fail to converge.
- **resolves:** track convergence across the next 10 runs.

---


## CLOCK-007 — teleological pairs converge to *instruments*, not definitions
> A pairing of two goal-directed operators (extract / optimize / maximize / compress —
> both aiming at a target) converges to an **operating procedure** (a falsifiable
> rule with a threshold and a stop-condition), whereas descriptive/reflective pairs
> converge to a **definition**. Teleological pairs also reach instrument-closure
> *faster* (≤ round 3) because both sides share "objective/what's at stake" vocabulary.
- **confidence:** 0.62
- **falsifies if:** a future teleological pair converges to a definition/metaphor
  without any procedure, *or* takes >5 rounds to close.
- **resolves:** run 2 more teleological pairs (e.g. compression × maximization,
  economy × throughput); score product class + closure round.
- **note:** first datapoint = extraction × optimization (converged to
  residual-tripwire + stop-when-invalidation>latency by round 4, two procedures).


## CLOCK-008 — temporal pairs converge to a *rate/phase* distinction
> A pairing of two temporal operators (entropy / accumulation / drift / decay —
> both about change-over-time) converges to a claim about **relative speed/phase**
> (which process runs faster, whether accumulation can outpace degradation, whether
> the two rates can be made to observe each other), rather than an instrument
> (teleological) or a definition (descriptive).
- **confidence:** 0.45
- **falsifies if:** a temporal pair converges to an instrument or a bare definition
  with no rate/phase claim.
- **resolves:** run 2 temporal pairs (e.g. entropy × accumulation, decay × repair);
  score whether the closing position is rate/phase-structured.
- **note:** zero-data prior. First candidate = entropy × accumulation.

## Honest limits

- The **scorer is still us** (me reading transcripts). A frozen prior gets most of
  the honesty; "who else can read the ruler" is the remaining 20% and a later build.
- These are the *first* clock entries — they exist to prove the clock works, not to
  be the definitive registry. Real consequence (does a distinction change a decision
  weeks later) still needs the compost + time; this clock is the *fast* reality we
  can already test against.
