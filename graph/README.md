# Graph archive — concepts as a walkable web

A structured layer under the human-readable docs. Each concept is a node carrying
four scores (1-5: coherence / relational / viability / living) plus provenance
(pairing + status). Edges are typed: extends / supports / refines / relates /
instantiated-by / sibling / guards.

This is the *retrieve-path* for the archive: walk from any concept to what it
depends on, contradicts, or was derived under — instead of reading a flat list.

## The four axes (from Appalachian's archive visual)

- **Ecological Coherence** — does it hold together without contradicting itself?
- **Relational Intelligence** — does it connect to other concepts, or is it an island?
- **Adaptive Viability** — does it survive pressure / falsification?
- **Living Systems** — does it keep generating, or was it a one-off?

## Status values

verified (survived falsification) > supported (repeated) > candidate > untested.

Rule: a concept only becomes a *beam* when it deepens under pressure (see METRICS.md).

## Format

The machine-readable form is `graph/concepts.json` (nodes + typed edges). This
markdown is the human explanation of how to read it.
