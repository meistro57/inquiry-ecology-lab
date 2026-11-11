# Decision Ledger

A running record of judgment calls made while operating the lab — the implicit choices
worth making explicit so they can be ratified, reused, or revised. This is the lab's memory
of *how we chose*, kept distinct from CLOCK.md (frozen *predictions*) and CONCEPTS.md
(frozen *findings*).

Each entry records what was decided, under what constraints, why, and whether it held up.

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
