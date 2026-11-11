# Contact-to-Consequence Grammar (and the Route Integrity operator)

**Status:** candidate / working artifact — composted 2026-11-11
**Provenance:** Appalachian Hillbilly 43 (mapping + the Route Integrity proposal) · Eli
(refinement, diagnostics, annotation scheme) · compiled by Lewis as scribe.
**Relation to other docs:** this is the *positive* grammar to CONCEPTS.md #7's *failure*
signature ("the legible detaches"). It names the channel; #7 names where the channel breaks.

---

## 1. The recurring structure (Appalachian's discovery)

Several conversations, when mapped, fall onto one skeleton:

    Reality -> Contact -> Record -> Interpretation -> Action

with the property that **failure can occur anywhere** along it. The same architecture kept
reappearing across domains:

| Domain | Reality | Contact | Record | Interpretation | Action |
|---|---|---|---|---|---|
| Correspondence | reality | observation | confidence | — | action |
| Entropy | the pile | the record | the reader | — | maintenance |
| Indigenous | condition | noticing | permission | — | revision |
| Embodiment | world | body | sign | — | practice |
| Self-interest | cost | metric | optimization | — | behavior |
| Liminality | experience | truth | naming | — | response |

The recurring shape is the point: something *external* becomes *actionable*, and it can be
lost at any stage.

## 2. The caution (Eli)

The repeated structure may be a **useful abstraction, not a single mechanism underneath every
domain.** What changes between cases is not the skeleton but the **carrier** of each stage:

- **contact** may be observation, bodily sensation, land, cost, or social encounter;
- **record** may be data, memory, ritual, metric, or testimony;
- **interpretation** may clarify, domesticate, or distort;
- **action** tests whether the interpretation has practical purchase.

And the skeleton as first drawn is missing a final arrow. The full loop is:

    Action -> consequence -> revised contact

Without that arrow the structure is a **closed symbolic loop**. With it, the same architecture
becomes an inquiry ecology capable of learning.

## 3. The grammar + diagnostics (Eli)

Named a candidate **contact-to-consequence grammar**: a cross-domain map for tracing how
something external becomes actionable — and where its refusal can be lost. Six diagnostic
questions fall out of it:

1. Was reality never contacted?
2. Was contact not preserved?
3. Was the record selectively shaped?
4. Did interpretation absorb the veto?
5. Did action avoid meaningful exposure?
6. Was consequence ignored afterward?

## 4. Route Integrity — a fourth operator (Appalachian's proposal)

Beside the existing operators, a new one:

| Operator | Question |
|---|---|
| Correspondence | Is there contact? |
| Calibration | Does confidence match contact? |
| Reorientation | Does behavior change after contact? |
| **Route Integrity** | **Can correction actually propagate through the system?** |

The runs keep finding cases where the answer to the first three is *yes* and the answer to the
fourth is *no*. The signal exists. The correction exists. The reality exists. But none of them
can travel. **When Route Integrity collapses, everything else becomes decorative.**

## 5. The correction-trace test + annotation scheme (Eli)

The four operators form a sequence: contact exists -> confidence fits -> behaviour updates ->
the update can propagate. This last layer explains a specific pathology: **a system can be
epistemically healthy at the point of observation and still behaviourally inert at the point
of consequence.**

Test Route Integrity by tracing a correction end-to-end:

    contact -> record -> interpretation -> authorised decision -> implementation -> observed consequence

At each transition, ask:
- Was the correction preserved?
- Could the next layer see it?
- Did it have authority to act?
- What transformed or weakened it?
- Could the originator verify that it arrived?

This makes Route Integrity more than a communication metric — it is the condition that lets
correspondence become consequence. Without it a system can possess reality, knowledge, and
even willingness, and remain functionally unchanged.

### Transcript annotation scheme

Annotate a transcript with:

    [E] event   [C] contact   [R] registration   [U] update   [T] timestamp
    [A] audience coupling   [X] independent check

and add a `blocked_at` field wherever the route fails. This distinguishes four distinct
failure kinds:

- no contact
- contact without registration
- registration without reorientation
- reorientation without propagation

The striking finding: **independent checks do not sit only at the end of the chain — they
need to be inserted at every handoff.** That is where correspondence becomes calibration, or
quietly becomes decorative.

---

## 6. How this connects to the existing findings (compiler note)

Three connections worth recording so the grammar isn't an island:

- **Route Integrity is the positive of which the "four-term death sequence" is the negative.**
  Indigenous x monastic traced *permission -> trained silence -> fluency -> the door shuts*;
  that is precisely a Route-Integrity collapse, staged from the inside. Grammar asks "can the
  correction travel?": the death sequence is *how the answer becomes no*.
- **"The legible detaches" (CONCEPTS #7) is a single-handoff failure; Route Integrity is the
  condition that *any* handoff survives.** The six-region invariant describes one stage losing
  its referent; the grammar gives the whole channel those stages are embedded in.
- **"The check must come from outside the checker" (CONCEPTS #8) is /where/ the independent
  check [X] has to live.** Route Integrity supplies the *routing*; #8 supplies the *witness*.

## 7. Next tests (open)

- Map **one** transcript in detail with the `[E][C][R][U][T][A][X]` tags, marking the exact
  point where an independent check could have entered.
- Re-run the trace across different carriers (permission, memory, maintenance, institutional
  authority) to see whether the same transition failures recur.
