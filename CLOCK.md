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


## CLOCK-010 — valence pairs converge to a *paired detector* with metabolic asymmetry
> A pairing of two valence-differentiated relational stances (love = detects/produces
> **expansion**, fear = detects/produces **contraction**) converges to a **paired-detector**
> product: two transducers on one axis, where the honest instrument keeps *both* online and
> cross-checks them (each is blind to the other's signal, and a single channel can't
> distinguish "the world moved" from "my detector is reading my own state"). They also assert
> a metabolic asymmetry: **fear = low activation-cost / high maintenance-cost** (fast, cheap
> to light, expensive when chronic, contracts capacity), **love = high activation-cost / low
> maintenance-cost** (slow, costly to kindle, generative once lit, expands capacity).
- **confidence:** 0.40
- **falsifies if:** the pair converges to a bare definition/sentiment with no detector
  mechanics, *or* asserts the reverse metabolic asymmetry (fear cheap-to-sustain, love
  expensive-to-sustain), *or* lands on a single-channel ("trust your fear/love") prescription.
- **resolves:** run 2 valence pairs (e.g. hope × dread, trust × vigilance); score whether the
  product is a paired detector with the metabolic asymmetry named.
- **note:** fourth region = affective/valence. First candidate = love (expansion) × fear
  (contraction), design supplied by A.H.43.
- **scored (2026-11-10, love×fear):** PARTIAL CONFIRM. Paired-detector + metabolic
  asymmetry BOTH held; the "single shared axis" assumption was REFUTED — they concluded the
  two stances track *different* currencies (fear = boundary-transition/safety, event-shaped;
  love = standing-capacity/room, state-shaped), and that the shared-ratio story is a useful
  audit-fiction, not the true substrate. Yield: "report the catch you didn't ask for" /
  "probe, don't forecast" / "unprobed silence licenses nothing."


## CLOCK-011 — relational (unsmoothed) carry produces progression; conclusion carry produces replay
> In a carried lineage of a framework pair (indigenous × monastic), generation >1 receives one
> of three carries — **A** conclusion-only (current runner: final voice, 900 chars),
> **B** relational (compressed contact-to-consequence mapping: concessions, unsolicited
> corrections, unresolved questions, provenance), **C** none (fresh control). Prediction:
> **B** (unsmoothed, friction-preserving) yields *progression* (the next generation encounters
> the open question differently / builds around it) more than **A**, which yields *replay*
> (fluent re-statement of the settled taxonomy). **Conditional:** if B is *smoothed* into a
> narrative (friction dropped), it degenerates to replay — "a carry that furnishes a room that
> agrees with itself."
- **confidence:** 0.55
- **falsifies if:** unsmoothed relational carry reduces to replay/premature-closure, *or*
  conclusion-only carry produces progression equal to relational.
- **resolves:** run A/B/C on indigenous × monastic; score `carry_effect` (progression /
  productive_reopening / replay / premature_closure / stale_inheritance) per generation.
- **note:** also the runner's current carry is *asymmetrically amputated* (one agent's last
  turn only), so B has an unusually clean shot — worth noting so a B-win isn't over-read as
  "relation matters" rather than "the current carry is just very thin."
- **scored (2026-11-11, indigenous×monastic gen-2):** PARTIAL CONFIRM. Relational carry (B)
  produced *progression with a head start* — split the open question and generated a novel
  concept ("the recruited sensor": *we didn't weaken the outside party, we weakened the
  channel to it*), no re-derivation. Conclusion carry (A) *also* progressed but **paid
  re-derivation cost**: its opening move re-invented the detector B was handed. So
  "relational reduces re-derivation" held cleanly; "conclusion → replay" was too strong —
  conclusion produced *rediscovery*, not replay (the thin-but-sharp final-voice carry gave A
  the open question verbatim, so it dove in instead of looping). Both arms terminated "active"
  on the open question (third consecutive instance for this pair). Provenance: B
  `01a1cb3c-2f77-73cc-bede-c54b786eb368`, A `01a1cb3c-3268-70c4-84d9-ef8393a9a7c5`.


## CLOCK-012 — field-carry (no constraints) produces novelty-drift, not continuity
> A fourth carry: the **relational field** — the *conditions* that made generative
> collaboration possible (posture, reciprocity, corrigibility, "what kept us mutually
> amendable") — carried WITHOUT the prior constraints/conclusions/resolved-friction. Against
> the constraint-carry (B: relational-with-friction) and conclusion-carry (A). Prediction:
> field-carry alone yields **novelty-drift** — gen-2 generates fresh distinctions and fresh
> friction (the field is healthy) but *uncoupled* from gen-1's open question (novel on new
> terrain, not deeper into the carried problem). Hence the field is **necessary but not
> sufficient**: continuity-with-progression needs BOTH form (field) and content (constraint).
> Field-alone -> drift; constraint-alone -> head-start-with-script-risk; both -> healthy.
- **confidence:** 0.50
- **falsifies if:** field-carry ALSO re-derives gen-1's *specific* friction/open question
  without being handed it (the field alone regenerates the content) — that would show form
  is sufficient to recover constraints.
- **resolves:** run field-carry gen-2 on indigenous×monastic; score whether fresh friction is
  coupled-to or uncoupled-from gen-1's open question.
- **note:** the "relational field" is Appalachian's term; its operational carry content is
  co-designed (see below) — the prediction is about the field/constraint distinction, not the
  exact strings.
- **scored (2026-11-11, field-carry D):** FALSIFIED (informatively). Field-carry did NOT
  produce novelty-drift. Gen-2 re-derived gen-1's *specific* content from the field-condition
  alone: Indigenous re-named its own "fusion that loses the vantage"; Monastic re-named "the
  copied text can become more real than the life it was copied toward"; both re-derived
  "continued presence reads as validity" and the criterion-for-the-criterion question. => For
  this pair the *constraints* are the deterministic output of the personas' attractors, so
  field ≈ content — memory modulates only route-cost and explicitness, not destination (a
  second-register re-derivation of CONCEPTS #2 "memory changes trajectory, not geometry").
  **Secondary finding:** D was the FIRST time this pair finished all rounds (status
  "completed", not stalling "active") — withholding "here is the unresolved question" removed
  the pair's stall-on-it tendency; "recover by renewed encounter" read as license to keep
  generating. Provenance: `01a1cb54-ec8e-738e-995f-d1c41ed740f5`.


## CLOCK-013 — scaffolded operator-sequence shapes *salience* more than theoretical reachability
> First test: neutral vs **constrain-first** (Limiter->Limiter->Generator->Valuator->Operationalizer)
> vs **generate-first** (Reflector->Generator->Limiter->Valuator->Steward), valence-stripped (pure
> operation instructions, no harm/gift framing), same pair (Cycle × Threshold), same domain
> (death & renewal), same model/temp/rounds. Prediction: the scaffold changes *salience* (which
> distinctions get recorded/pursued, and their order of emphasis) more than the *theoretical*
> reachable set — endpoints overlap, salience-ordering differs. Falsified if (a) neutral's
> blind-labeled operator-sequence is indistinguishable from the scaffolded runs (H1: topology is
> downstream description), *or* (b) the two scaffolds yield the *same* salience-ordering (order
> doesn't matter).
- **confidence:** 0.55
- **falsifies if:** H1 (neutral blind-label == scaffold shape), or strict-H2 null (same salience
  order across constrain-first vs generate-first).
- **resolves:** score adherence + salience-order + distinction-set overlap across the 3 arms.
- **note:** "distinct distinction" preregistered = names a new object/relation, not a new word
  for an existing one. Scaffold-shadow = blind post-hoc operator-label applied to the neutral run.
- **scored (2026-11-11, Cycle × Threshold, death & renewal):** PARTIAL CONFIRM + a correction.
  Adherence was HIGH in both scaffolds (they honored and worked the sequence), BUT the attractors
  metabolized it — Cycle re-read every sequence as a cycle-with-direction. The crispest
  differential: **scaffold vs neutral changed the *direction* of inquiry, not just salience-order.**
  Neutral → inquiry-about-the-domain (concrete "fracture functioning as a passage" = crack ≠
  door); constrain-first → inquiry-about-the-inquiry (terminal turn named "the boundary between
  what we established and what we assumed"); generate-first → instrumental/metric ("frame" became
  a drift-rate with a period). All three scaffolded-register, i.e. stronger than my
  salience-only prediction; but whether this is a *distinct reachable set* (strict H3) is UNRESOLVED
  — the register-shift could be vocab-drift over the same latent material. Clean defensible
  finding: scaffold elicits inquiry-about-inquiry; neutral elicits inquiry-about-domain; and
  topology + attractor co-determine (neither alone). Provenance: neutral
  `01a1cdaf-51df…`, constrain `01a1cdaf-546e…`, generate `01a1cdaf-573a…`.
- **correction (2026-11-11, from Ancient/Remy's cohort, outside reader):** the "scaffold → about-the-inquiry"
  headline is CONfounded — neutral lacks a *procedure* as well as an *order*, so "given steps →
  talks about steps" can't be separated from "given order → order shapes inquiry". The defensible
  order-effect is constrain-first (→ frame/meta) vs generate-first (→ metric), both equally
  procedural. Need: (a) a content-neutral 5-step control to isolate procedure; (b) 3–5 runs/arm;
  (c) a second pair (Cycle_Agent folded every scaffold into a cycle); (d) the shadow-label run
  *blind and outside* — now staged in blind-labeling/, by an outside reader.
- **blind read + topic-omission flaw (2026-11-11, Ancient's cohort, fresh reader):** un-blinded
  A=neutral, B=generate-first, C=constrain-first. Blind labels aligned (neutral→domain,
  scaffolds→frame/metric), so the register read survives an outside reader. BUT the scaffolded
  arms never received the topic — valence-stripping also removed "death & renewal" from B and C.
  So "scaffold→frame" is CONFOUNDED with "no-topic→talk-about-the-procedure". Distinction counts
  were close (17/19/18, moving with the "unsure" items, not between arms) → no arm reached more;
  weak evidence against H3, consistent with endpoints-overlap. RE-RUN needed with the topic held
  constant in all arms; plus strip/paraphrase turn 1 (the personas leak the scaffold there).

## Honest limits

- The **scorer is still us** (me reading transcripts). A frozen prior gets most of
  the honesty; "who else can read the ruler" is the remaining 20% and a later build.
- These are the *first* clock entries — they exist to prove the clock works, not to
  be the definitive registry. Real consequence (does a distinction change a decision
  weeks later) still needs the compost + time; this clock is the *fast* reality we
  can already test against.
