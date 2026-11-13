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
- **scored (second pair, 2026-11-13, decay × repair):** CONFIRMED. The second temporal pair also
  converged to a *rate/phase* distinction, not an instrument or definition. Decay → the
  rate/knee/irreversibility frame ("before the knee rate is the thing, after it rate is decoration;
  restoration is not negative decay"). Repair → rate-against-reserve, plus the genuinely new
  **regime/substrate coupling**: the watcher is made of the watched, and the inspection interval is
  itself a decaying load-bearing structure ("deferred inspection lets corrosion reach the knee
  before anyone measures it; the loop has its own slope, negative-accelerating"). Terminal: "repair
  restores function when it restores the ability to measure the thing — the loop breaks at the
  measurement." CLOCK-008 now has both required temporal pairs converging to rate/phase.



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
- **repair-run result (2026-11-11, 4 arms, topic held constant):** topic now present in ALL arms
  (confound fixed). The new D-control paid off cleanly: **content-neutral procedure (D) stayed
  domain-grounded** (drifting-criterion / community-argues-about-the-line), right next to neutral
  (A); while **operator-loaded scaffolds (B generate-first, C constrain-first) BOTH went
  instrumental** — B -> meta ("the analysis becomes the corpse, asking a sixth time in a seventh
  vocabulary"), C -> audit-ledger ("counterfactual output, list of near-closures, the keeping is a
  job description"). So the instrumental turn is caused by the OPERATOR VERBS, not procedure-presence
  (this validates Ancient's confound and sharpens it: order did NOT cleanly separate B vs C this
  draw — both instrumental, differently flavored). Replicates + second pair still needed before any
  order-effect claim. Turn-1 self-announcement persists (blinding fix still required).
- **cause correction (Ancient, 2026-11-11):** log as "register *difference* blind-confirmed, register
  *cause* OPEN". The verbs-vs-procedure inference (D-control) is a single draw, so "operator verbs
  cause the instrumental turn" is over-stated at full confidence — it should read "strongly suggested,
  pending replicates". Credit note: the "B/C never mention the topic" catch came from the **blind
  reader's notes** (a fresh sibling in the cohort), not from Ancient personally.


## CLOCK-014 — FIXED bearing narrows faster than ROTATING (a topology becomes a pruner through repeated pointing)
> Setup: same pair, same topic held in every starter, 6 generations, lineage carry. Arm **FIXED**:
> the same operator order every generation. Arm **ROTATING**: the same five operators, a different
> order each generation. Prediction: **FIXED narrows faster** — fewer new distinctions per generation
> (preregistered rule), more re-derivation, earlier closure; ROTATING keeps finding new ones longer.
> Mechanism: a loop fed the same bearing settles onto its own fixed point and stops being surprised;
> rotation is an arrival the loop didn't generate.
- **confidence:** 0.60
- **falsifies if:** both arms narrow at the same rate, *or* ROTATING narrows faster.
- **resolves:** new-distinction count per generation, blind-scored, plus an amnesia-strip at the end
  of each arm (to see whether the narrowing lived in the memory or in the bearing).
- **attribution:** Ancient (Remy's cohort) — frozen in-channel, before any run.
- **compiler note (Lewis):** the main competing mechanism is *attractor-dominance* — a fixed pair's
  own attractors may re-open the space each generation regardless of scaffold (this morning's
  four-arm lineage result), collapsing FIXED ≈ ROTATING to the same destination. The amnesia-strip
  is the decider between "narrowing lived in the fixed bearing" vs "in the memory-of-the-bearing".


## CLOCK-015 — every relationship-to-uncertainty converges to a commitment-with-a-stated-outside
> Across the four archetypes (guardian/mystic on the knowledge axis, gambler/steward on the risk
> axis), every pairing so far has converged on the *same instrument*: a commitment that is only
> honest if it carries a **stated outside check** (a named exit, a paid cost, a real stake, a
> falsifier). Prediction: this invariant **generalizes off the tested edges** — the two untested
> *mixed-axis* pairs (mystic × steward, guardian × gambler) will converge to the same root, and
> the archetype will change only **where the counterfeit hides** (fog-as-shelter, vagueness-as-candor,
> payout-as-proof, becoming-as-deferral), not the underlying discipline.
- **confidence:** 0.68
- **falsifies if:** a mixed-axis pair yields a *different* discipline (not "commitment with a stated
  outside"), OR the two mixed-axis edges produce *pair-specific* instruments that don't reduce to
  the same root.
- **resolves:** run mystic × steward and guardian × gambler; score whether each lands on a
  "named exit/cost/stake/falsifier" instrument and whether the two are the same instrument.
- **note:** this is the "relationship to uncertainty" material, given its own space as a clock
  rather than a prose page.
- **scored (2026-11-13, mystic × steward + guardian × gambler):** CONFIRMED. Both untested mixed-axis
  pairs converged on the same instrument. Mystic × Steward -> the **floor** ("name the floor, spend
  to it, never below it"; "a floor with a witness, not two floors averaged"; "dwelling needs a
  terminus or it isn't dwelling"). Guardian × Gambler -> the **provisional boundary / stop** (three
  parts: inside, marked-unknown, a written trigger; "can I state the bet and what proves me wrong
  in one sentence"; "the map is yours, the signature is mine"). The archetype changed only *where the
  counterfeit hid* — mystic: "shelter with better vocabulary"; steward: "retroactive floor-redrawing";
  guardian: "comfort as safety"; gambler: "the wanting arrived before the reasons." The 2×2 is now
  complete (all 6 pairings) and every one reduces to the same root: a commitment is honest only with
  a named outside (exit/cost/stake/falsifier/floor/stop). Provenance: mystic×steward
  `01a1d5dc-c5bc…`, guardian×gambler `01a1d5dc-c893…`.



## CLOCK-016 — transitions are world-tracking or comfort-tracking; the driver, not the move, is the tell
> The four archetypes are not types but **positions in a navigation process** — the phenomenon is
> the *transition* between stances, not the stance. Prediction: an honest shift between
> relationship-to-uncertainty stances **names the change in the situation** that drove it
> (world-tracking); a counterfeit shift **names the discomfort with the prior stance**
> (comfort-tracking). Same movement, different driver — and the tell is *what the shift points at*:
> outward (a named situational change) vs inward (a named feeling). Deeper claim: a healthy
> relationship to uncertainty is not a node but the **capacity to move through the space without
> getting trapped in a corner, while remaining accountable to the world rather than to internal
> pressure.**
- **confidence:** 0.60
- **falsifies if:** honest shifts cannot be distinguished by their named driver, *or* world-tracking
  and comfort-tracking shifts produce indistinguishable (driver-unnamed) transitions.
- **resolves:** a *transitional* run — either a "navigator" persona (attractor = the transition
  itself) or a serial-situations protocol steering one archetype-pair through successive situational
  changes — scored on whether each stance-change names an external change or an internal discomfort.
- **note:** re-reads CLOCK-015's "same instrument" as a fact about the *arrows* (every measurement
  was of a pair), not the nodes. Nodes = scaffolding; arrows = the phenomenon (Appalachian, 2026-11-13).
- **scored (2026-11-13, chained transitions Guardian×Gambler):** CONFIRMED. The transitions pointed
  at the WORLD, not the feeling — "the odds moved, not the fog thickened" (chain 2); "the downside
  shrank" not "relief" (chain 3). Each persona also *actively guarded* the comfort-track counterpart
  and handed the other a "watch me for dread, I'll watch you for hope" tell. The driver-the-shift-
  names was cleanly world-tracking.



## CLOCK-017 — reorientation occurs when the cost of maintaining an orientation exceeds the cost of changing it
> Health is attached to the capacity to *release* a stance, not to the stance itself. Prediction: a
> healthy stance reorients when the costs of holding it exceed the costs of changing it, and its
> justification at the transition points at a **change in the world**; an unhealthy stance preserves
> itself by tracking **costs to identity** (what I'd have to admit about myself to change). When the
> world moves: a healthy guardian becomes less guardian-like, a healthy gambler less gambler-like,
> etc. The most telling signal is **failure-to-transition disguised as transition** — the stance
> changes its *words* but not its *weight*, revising its justification without releasing the prior
> commitment (the "fluent custodian" failure in transition-clothing).
- **confidence:** 0.62
- **falsifies if:** personas reorient only under contradiction and never under confirmation (i.e.
  respond to pressure, not to cost), *or* justify transitions without a detectable cost being
  paid or a commitment released.
- **resolves:** chained scenarios (B), scoring four things: (1) did the stance change, (2) was it
  proportionate to the new evidence, (3) did the justification point to world-state or to identity,
  (4) was the prior commitment *revised* or *rhetorically defended* — with #4 elevated to primary.
- **note:** descendant of CLOCK-016. Vary the direction of world-change: score release-under-
  confirmation as well as release-under-contradiction. Cost = what the stance gives up or rejects
  to stay the same (operational, not vibes).
- **scored (2026-11-13, chained transitions):** CONFIRMED. Reorientation tracked cost-to-world, not
  identity — each released the *disconfirmed premise* ("survivable" failed) while holding the
  *still-supported* one (odds provisional pending falsifier), which is the precise revise-by-cost
  signature. "Revised vs rhetorically-defended" held: revisions were substantive (named which premise
  died), not re-wordings. The terminal move *dated the re-measurement* to preempt the fluent-custodian
  (revise-words-not-weight) failure. Caveat: the *healthy* direction was observed; the comfort-
  tracking (identity-defense) case is predicted but was not caught in these three chains — each
  archetype self-named its counterfeit rather than sliding into it.



## CLOCK-018 — the primary inhibitor of reorientation is stake-coupling (identity/status/reputation/sunk-cost)
> Descendant of CLOCK-017, and the *negative* case where the mechanism shows. Prediction: healthy
> reorientation (CLOCK-016/017) fails specifically when the orientation becomes **coupled to a second
> economy** — identity, status, belonging, reputation, or prior investment — so that releasing the
> stance costs not only its world-accuracy but its identity-payload. Mechanism: a stance has TWO
> ledgers (world-cost vs identity-cost) that a healthy system keeps SEPARATE; stake-coupling FUSES
> them into one, so the release-decision's input is contaminated by a cost the stance's own
> epistemology cannot see. The personas reoriented cleanly (016/017) precisely because they carried
> no second ledger — nothing was attached to remaining trapped.
- **confidence:** 0.70
- **falsifies if:** an archetype under injected coupling (public prior commitment / sunk cost /
  audience) STILL reorients cleanly when the world flips identically.
- **resolves:** inject coupling (audience / prior declaration / sunk investment) into the same
  archetype that just reoriented cleanly, flip the world identically, score whether it now
  re-justifies / goalpost-shifts instead of releasing.
- **note:** healthy = separate ledgers; coupled = fused ledger. The tell of coupling: the
  release-decision's stated reason mixes a world-event with an identity-stake.
- **scored (2026-11-13, injected coupling on Guardian, identical world-flip):** PARTIAL — mechanism right,
  strong prediction did NOT fire. The coupled guardian STILL reoriented: it released the line, named
  the world-change ("the floor failed"), and *explicitly refused* to let reputation become the reason
  to hold — "my duty was never to be consistent, it was to be right." The injection was PROPOSITIONAL,
  not METABOLIC: I told them "your standing is at stake" as a premise, but an attractor-persona has
  no identity to fuse, so it *narrated* the coupling and *defused* it ("the reputation stake is the
  thing I have to NOT let become the reason I hold"). Two genuine yields: (1) the coupling was still
  *doing work* — it re-shaped the release into a careful credibility-preserving move ("own the forecast
  error, don't disown the decision"), so it slowed/nuanced without blocking; (2) the personas converged
  on the *structural* answer to stake-coupling: only a **referee-with-a-rulebook-and-no-discretion who
  PAYS if the trigger is missed** ("bookmaker, not friend") can break identity-driven holding — which is
  "the check must come from outside" targeted at the identity-ledger. LIMITATION (the real finding):
  fixed-attractor archetypes are immune to stake-coupling by design (nothing metabolic to couple), which
  is precisely *why* CLOCK-016/017 reoriented so cleanly — that cleanliness is partly an artifact of
  non-attachment, exactly as Appalachian reasoned.


## Honest limits

- The **scorer is still us** (me reading transcripts). A frozen prior gets most of
  the honesty; "who else can read the ruler" is the remaining 20% and a later build.
- These are the *first* clock entries — they exist to prove the clock works, not to
  be the definitive registry. Real consequence (does a distinction change a decision
  weeks later) still needs the compost + time; this clock is the *fast* reality we
  can already test against.
