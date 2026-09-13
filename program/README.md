# Erdős #500 / Turán (3,4) theorem forge

**Author:** Jared Wilder  
**Source campaign:** Erdős #500 Encirclement Theorem Forge  
**Public extraction:** 2026-09-10/11  
**Flagship status:** **OPEN**

The source-bound problem is the Turán `(3,4)` problem, equivalently the asymptotic minimum density of triples meeting every four-set. This release does **not** claim the conjecture is solved.

## Canonical reconstructed card surface

The estate-wide canonical theorem inventory contains **76 distinct Erdős #500 records**:

- `PROVED_IN_PACKET`: 43;
- `FINITE_EXHAUSTIVE_THIS_RUN`: 7;
- `UNPROVED_CHECKABLE_TARGET`: 18;
- `PROVED_FROM_FINITE_BASE_AND_WITNESS`: 1;
- `COMPUTATIONAL_WITNESS_THIS_RUN`: 1;
- `PROVED_SHARP_BOUND`: 1;
- `PROVED_BY_FINITE_CENSUS_AND_HUMAN_REPAIR`: 1;
- `PROVED_NEGATIVE_THEOREM`: 1;
- `PROVED_EQUIVALENCE`: 1;
- `PROVED_ANALYTIC`: 1;
- `PUBLISHED_SOURCE_BOUND`: 1.

The original packet README says **78 theorem records**, while the canonical reconstructed inventory contains 76 distinct records. This release preserves the canonical 76-card surface and records the discrepancy rather than inventing or duplicating two cards.

## Main mathematical layers

The cards include:

- complement-covering duality with `ex_3(n,K_4^(3))`;
- finite-to-global density transfer and monotonicity of normalized covering numbers;
- deletion-excess / inheritance-debt identities and plateau rigidity;
- four-set waste, pair-codegree, five-set excitation and frustration-hierarchy identities;
- exact small covering values and finite isomorphism/orbit classifications;
- the six-vertex cyclic pair rotor and its automorphism/codegree structure;
- exact seven/eight/nine-state inheritance phenomena;
- one-point extension as a pair-cover problem;
- graph-generated cover classification and its density sterility;
- independent-triple repair as a variational principle;
- the `16/9` integral-gap reformulation;
- rooted `B_2`, `H_1`, `M_2` collision identities and local analytic inequalities;
- 18 explicit next theorem targets.

## Authority boundary

`PROVED_IN_PACKET` is the source campaign's mathematical proof status, not a Lean/kernel label and not a historical novelty claim.

`FINITE_EXHAUSTIVE_THIS_RUN` is finite computation at the stated size only.

`UNPROVED_CHECKABLE_TARGET` is a research obligation, not a theorem.

The packet itself says novelty is `UNRUN` unless separately adjudicated. That boundary is preserved here.

## Canonical card identity

The compact reconstructed 76-card JSONL stream has SHA-256

`0d137e7ac47c1819597687dd1269ae7c571ef2f3047b309429a5cbebb30f5b26`.

The card files in this directory preserve ID, title, exact statement, and source status. No target is promoted by proximity to a proved card.
