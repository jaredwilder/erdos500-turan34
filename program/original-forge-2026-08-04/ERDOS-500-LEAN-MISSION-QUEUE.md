# Erdős #500 Lean Mission Queue

**Rule:** these are normalized missions, not compilation receipts. Bind every accepted theorem back to its claim hash.

## Tier 1 — Generic finite-set identities

1. `ex3_tetrahedron_eq_total_sub_coverNumber` — E500-A01
2. `cover_density_ge_local_cover_density` — E500-A02
3. `sum_deletionExcess_eq_inheritanceDebt` — E500-A04
4. `cover_density_increment_eq_debt` — E500-A05
5. `cover_density_plateau_iff_all_deletions_optimal` — E500-A06
6. `plateau_optimal_cover_regular` — E500-A07
7. `optimalDeletion_count_ge_vertices_sub_debt` — E500-A08
8. `coverageWaste_eq_fourMultiplicityExcess` — E500-A11
9. `coverageWaste_eq_pairOverlap_sub_clusterRebate` — E500-A12
10. `cover_density_eq_threeTenths_add_meanFiveExcitation` — E500-A15

## Tier 2 — Local classifications

1. `fiveGroundState_iff_complementPairGraph_P3_disjoint_K2` — E500-A14
2. `native_decide_unique_sixCover_rotor` — E500-B03
3. `rotor_degree_codegree_profile` — E500-B06
4. `rotor_deletion_fourSet_profiles` — E500-B07
5. `coverNumber_seven_eq_twelve` — E500-B08
6. `coverNumber_eight_eq_twenty` — E500-B11
7. `coverNumber_nine_eq_thirty` — E500-B13
8. `optimalNine_fullyHereditary_regular10` — E500-B14

## Tier 3 — Collision package

1. `Razborov_H_profiles` — E500-D01
2. `H1_M2_commonFourRoot_iff_B2` — E500-D02
3. `H1_rotor_fourOverlap_uniqueOrbit` — E500-B16
4. `H1_rotor_collision_min_thirteen` — E500-B17
5. `canonicalCollision_minRepairs_three_twoOrbits` — E500-B18
6. `H2_H3_rotor_fourOverlap_impossible` — E500-B19

## Tier 4 — Generalized blades

1. `general_cover_density_ge_local` — E500-A19
2. `general_cover_deletionDebt_plateauRigidity` — E500-A20
3. `general_onePointExtension_dimensionDescent` — E500-C13

## Suggested Lean representation

- Vertex type: `Fin n`.
- Triple family: `Finset (Finset (Fin n))` with cardinality-3 predicate, or a boolean predicate on `Finset (Fin n)`.
- Four-cover predicate: every cardinality-4 set contains a selected cardinality-3 subset.
- Keep generic incidence identities separate from finite `native_decide` theorems.
- For B08, formalize the human contradiction after importing the finite B03 lemma that every six-edge minimum cover is pair-positive and 3-regular.

## Acceptance receipt

For every theorem record: Lean version, command line, exit code, stdout/stderr hash, source hash, theorem statement hash, and `#print axioms` output.