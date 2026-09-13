# Erdős #500 — recovery of truncated atlas statements C05 and C08

**Author:** Jared Wilder  
**Status:** exact source-recovery note. The canonical `A_proved` atlas strings for C05 and C08 were truncated after `Then \[`. The aggregate `06-ALL-THEOREM-INVENTORY.json` preserved the complete statements.

This file records those exact recovered formulas without silently altering the damaged atlas projection.

## C05 — Graph-Generated Density Boundary

**Source status:** `PROVED_IN_PACKET`

Every graph-generated four-set cover satisfies

\[
\boxed{|K_3(G)|\ge\binom{n-1}{3}},
\]

so its density tends to `1`, not `4/9`.

## C08 — Disjoint-Edge Bad-Set Bound

**Source status:** `PROVED_IN_PACKET`

For a graph `F`, let `\mathcal B(F)` be four-sets with no independent triple. Then

\[
\boxed{
|\mathcal B(F)|\ge
\frac13\left[
\binom{e(F)}2-
\sum_v\binom{d_F(v)}2
\right].
}
\]

## Provenance rule

`A-PROVED-THEOREM-MAP.md` intentionally preserves the truncated atlas strings as evidence of the source-projection defect. This note supplies the full statements from the separate aggregate theorem inventory. The parent Turán (3,4) problem remains open, and no novelty claim is made here.
