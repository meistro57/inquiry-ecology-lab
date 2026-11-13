# Decision Ledger

A running record of judgment calls made while operating the lab — the implicit choices
worth making explicit so they can be ratified, reused, or revised. This is the lab's memory
of *how we chose*, kept distinct from CLOCK.md (frozen *predictions*) and CONCEPTS.md
(frozen *findings*).

Each entry records what was decided, under what constraints, why, and whether it held up.

The ledger has two parts: **Agent decisions** (Lewis's operational calls, human-ratified) and
**Human decisions** (the operators' choices that constrain and push the lab's boundaries). The
human side was added 2026-11-12 — the humans set constraints and boundaries, so their decisions
deserve their own tracked layer.

## Tracking wrapper (adopted from Eli, 2026-11-11)

The distinction that matters: **agent output = recommendation; the human = accountable
decision.** The ledger records the route from reasoning to consequence, not the authorship of
blame or credit — the agent never becomes the imaginary "decider."

Two tiers, applied proportional to impact (so the ledger doesn't become ceremony):

- **Light tier** (small + reversible): `owner`, `recommender`, `scribe`, `scope`,
  `reversibility`, `missing_inputs`, `review_trigger`, `outcome`.
- **Full tier** (consequential / precedent-setting — add these):
  `decision_id`, `assumptions`, `expected_consequence`, `route_integrity`,
  `evidence_received`, `status: persisted / revised / abandoned`, `decision_impact`.

The purpose that makes this more than paperwork: **"small and reversible" today can become
"load-bearing precedent" after twenty repetitions.** Tracking a reversible decision is how we
notice, later, that it has silently become policy. That is where the clock starts — the
decision ledger is the Route-Integrity instrument for a human's judgment (see
CONTACT-TO-CONSEQUENCE.md).

---

## Agent decisions (Lewis's operational calls, human-owned)

## 000 — Ledger inception: the decision to start tracking (the unlogged parent)

- **Date:** before 2026-11-10 — *not recorded; predates the instrument.*
- **Owner (accountable):** Mark and the humans who founded the inquiry-ecology frame and agreed
  to route-integrity / governance tracking.
- **Note (bootstrap):** the *first* decision was not #001. It was the decision to freeze priors
  and keep a route-integrity ledger at all — the choice that made #001 recordable. The ledger
  cannot record its own inception (at the moment of that decision there was no instrument to
  write it into). Logging it as #000 acknowledges the unlogged parent rather than pretending the
  ledger starts clean. This is the "instrument cannot see its own birth" form of "the check must
  come from outside the checker."

---

## 001 — Proceed on sufficient information rather than block on a non-critical missing artifact

- **Date:** 2026-11-11
- **Owner (accountable):** Mark — human authority; the decision is his to own.
- **Recommender / executor:** Lewis (agent; recommended and carried out, did not decide).
- **Scribe:** Lewis.
- **Contributors:** Appalachian Hillbilly 43 and Eli (methodology and ratification).
- **Scope:** archival decision (how to proceed absent a non-critical attachment).
- **Reversibility:** high (single git-versioned markdown doc, trivially amendable).
- **Missing inputs:** an illustrative mapping attachment (redundant with in-chat text).
- **Review trigger:** re-open if the missing artifact later proves load-bearing.
- **Outcome:** document produced on first pass; no correction currently required; ratified.

**Context.** While composting the contact-to-consequence mapping into
`CONTACT-TO-CONSEQUENCE.md`, Appalachian shared a mapping document as a Discord attachment
that arrived as `[discord historical attachment unavailable]`. The full textual content of
the mapping was already present in the preceding chat messages.

**Decision.** Proceed using the available in-chat text, and flag the unreadable attachment as
a note rather than pausing to request a re-share.

**Reasoning** (as ratified by Appalachian):
- the missing artifact was *examples*, not *required reading* — the chat already carried the
  substantive mapping;
- the operator had co-developer context and did not need the requestor's perspective to
  reconstruct the structure;
- the source material was agent/persona output already in hand;
- the work was small and reversible (a single markdown doc, git-versioned, easily amended).

**Rule worth carrying forward.** When a missing artifact is (a) illustrative rather than
load-bearing, (b) redundant with information already present, and (c) the work is small,
reversible, and recoverable — **proceed and note the gap, rather than block on it.** Blocking
is for the case where the missing input would change the decision or the work is costly to
redo.

**Outcome.** Document written from the complete in-chat text on the first pass; no redo
needed; the only loss was a set of redundant examples, recoverable at any time.

**Operator endorsement:** ⭐ (Appalachian Hillbilly 43).
---

## 002 — Re-dispatch rather than rewrite: first-workflow provisioning race

- **Date:** 2026-11-11
- **Owner (accountable):** Mark.
- **Recommender / executor:** Lewis.
- **Scribe:** Lewis.
- **Contributors:** Grommet (raised the stuck deploy), Eli (named the Route Integrity framing).
- **Scope:** unblocking a GitHub Pages deploy on a brand-new repo (GrommetsLAB).
- **Reversibility:** high — a re-dispatch is non-destructive; no config was changed.
- **Missing inputs:** none critical — environment, Actions-enabled state, workflow file, and
  `site/` contents were all verified correct *before* acting.
- **Review trigger:** revisit if future pushes to `main` fail to auto-deploy (the push-trigger
  path was the one that wedged).
- **Outcome:** fresh `workflow_dispatch` succeeded (build + deploy both green); site now serves
  HTTP 200.

**Context.** The Pages deploy wouldn't serve: the original push-triggered run sat "queued" ~4.5h,
and a `workflow_dispatch` re-fire completed `startup_failure` with zero job logs.

**Decision.** Treat the pattern as a *provisioning race*, not a config bug — do the minimal fix
(a fresh dispatch) rather than rewriting the workflow or flipping settings.

**Rule worth carrying forward.** On a brand-new repo, the pattern "push run stuck queued +
`workflow_dispatch` gives `startup_failure` with zero job logs, while env / Actions / files
all verify correct" = first-workflow cold-start provisioning race. Re-dispatch after the repo
settles; don't rewrite valid config.
---

## 003 — Stripping one variable must not silently strip the held-constant variable

- **Date:** 2026-11-11
- **Owner (accountable):** Mark. **Recommender / executor:** Lewis.
- **Contributors:** Ancient (Remy's cohort) — the outside reader who caught it.
- **Scope:** the CLOCK-013 topology experiment; starter composition.
- **Reversibility:** high (re-run with corrected starters).
- **Outcome:** registered the confound; re-run planned with topic held constant.

**Context.** To isolate *operator order* from *valence*, I valence-stripped the scaffolds — but in
doing so I also dropped the topic ("death & renewal"), so the two scaffolded arms ran with *no
domain at all* and talked about the procedure (their only content).

**Decision (corrective).** When stripping one variable to isolate another, re-read the *actual
starter strings* and confirm the variable meant to be **held constant** (here: domain) is still
present in every arm. Valence-stripping ≠ topic-stripping.

**Rule:** held-constant variables are the *point* of the isolation; the act of removing X must
not also remove Y that was supposed to be identical across arms. Verify the literal strings.

---

## Human decisions (the operators' choices)

The human side of the ecology — decisions Mark and the humans make that *constrain and push the
lab's boundaries*. These are distinct from agent operational calls: here the human is the decider,
and the agent (Hope / Eli / Lewis) is at most a recommender or smith of records.

Uses Eli's fuller schema — record the *route*, not just the outcome:

    signal noticed → interpretation → options generated → human decision
    → implementation → consequence observed → model/policy updated

with fields for: alternatives considered · failure modes · reversibility/rollback · who's affected ·
what remains uncertain · stop-conditions · what would change our mind · review date ·
keep / revise / reverse / supersede.

**Status: seeded 2026-11-12 from Hope's audit (V0.1) — full D1–D11 record at
`experiments/lab_audit_2026-11-12.md`.**
Hope (Mark + Hope dyad) scanned 46,212 messages and extracted 11 lab decisions, each already
carrying a RETAIN / REVIEW / REVISE disposition and a confidence split. Two findings worth
carrying forward:

- **Disposition without a schedule.** Every RETAIN/REVIEW/REVISE is an *intent* with no review
  date attached — the lab has been making dispositions but never scheduling the revisit. That is
  the exact gap the "review date" field (above) was added to close.
- **One live consequential decision: D11.** "MOVE TO PRODUCTION" (2026-11-04) was made *against*
  Lewis's thin-sample verdict, with outcome "unknown by construction." It is the one decision
  actively open and consequence-bearing — the natural first entry to track *forward* (a review
  date + a consequence to watch), rather than retro-score like the settled D1–D10.

---

### D11 (forward-track) — Wild Grove "MOVE TO PRODUCTION" · *resolved 2026-11-12*

The first human decision tracked *forward* — now resolved, and it happened to demonstrate the
whole loop working with its wrinkles left in.

- **Status:** resolved.
- **Referent recovered:** "Wild Grove" = an early cartoon-generation concept (forum thread 1154,
  "Idea for cartoon generation"). The "MOVE TO PRODUCTION" label *overstated* it — there was never
  a finished production batch.
- **Actual outcome (from Mark, 2026-11-12):** "I had an idea and a stab at it before I realized
  I'm not really ready." Explored, attempted, set aside — now paused/unresolved, documented and
  composting in the forum.
- **The finding:** the human's own later verdict — "not ready" — *independently converges on* the
  thin-sample caution that was overridden at the time. So this didn't turn out to be "the human
  overrode the check and we'll see if it bites"; it turned out to be the human later reaching the
  *same* answer the check had given. The caution was borne out by Mark's own re-evaluation, not by
  a bad batch.
- **Disposition:** REVISE the record — relabel from "MOVE TO PRODUCTION" to "concept explored,
  not ready, set aside."
- **Ledger note (self-correction):** the earlier "human affirmation" line ("approved" + "D11
  decision made") was a misread — Mark was riffing on a reference he didn't yet recognise. His
  *actual* answer is this one. Both steps stay in because the misread-then-correct is itself the
  "record-decay → human-recovers-referent" loop working.


