# Erdős #500 — A-proved theorem identity map

**Author:** Jared Wilder  
**Status:** reader-facing index extracted from the estate's canonical `A_proved` atlas layer.  
**Parent problem:** Turán (3,4) remains open.

This file exposes the theorem identities that were otherwise buried inside the reconstructed #500 program. It does **not** upgrade authority: the status and evidence flags below are copied from the canonical atlas identity layer, and the source program/receipts remain controlling.

Canonical atlas count for domain `erdos-500-encirclement`: **52 A-proved identities**.

Legend: `P` = proof object/text recorded; `L` = Lean material recorded; `F` = falsifier/verifier material recorded. These flags mean the estate records those evidence classes; they are not a new independent replay by this index.

## A-series (19)

| Identity | Statement | Source status | P | L | F |
|---|---|---|:---:|:---:|:---:|
| A01 — Complement Covering Duality | Let \(c_n\) be the minimum size of a family \(M\subseteq\binom{[n]}3\) meeting every four-set in a contained triple. Then \(\operatorname{ex}_3(n,K_4^{(3)})=\binom n3-c_n\). | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| A02 — Finite-to-Global Density Transfer | If \(M\) covers every four-set on \(n\) vertices and \(4\le s\le n\), then \(\|M\|/\binom n3\ge c_s/\binom s3\). | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| A03 — Monotonicity of Normalized Covering Numbers | The sequence \(q_n=c_n/\binom n3\) is nondecreasing for \(n\ge4\). | `PROVED_IN_PACKET` `COURT_READY` | — | ✓ | ✓ |
| A04 — Deletion-Excess Identity | For an \((n+1)\)-vertex four-set cover \(M\), define \(\delta_M(v)=\|M-v\|-c_n\ge0\). Then \(\sum_v\delta_M(v)=(n-2)\|M\|-(n+1)c_n\). | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| A05 — Density-Increment Identity | With \(\Delta_n=(n-2)c_{n+1}-(n+1)c_n\), the increment \(q_{n+1}-q_n\) is an exact positive multiple of \(\Delta_n\). | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| A06 — Plateau / Full-Heredity Equivalence | A density plateau occurs exactly when every vertex deletion of every optimum \((n+1)\)-state is optimal at size \(n\). | `PROVED_EQUIVALENCE` `COURT_READY` | ✓ | ✓ | ✓ |
| A07 — Plateau Regularity | On a plateau, every optimum state has equal vertex degrees, forced by the deletion identities. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| A08 — Degree-Sum Constraint | The vertex degrees in a triple cover satisfy the exact triple-count degree-sum relation used by the deletion ledger. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| A09 — Local Four-Set Coverage Constraint | Every four-set must contain a selected triple; the local incidence formulation is exactly equivalent to the complement Turán condition. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| A10 — Optimal Deletion Lower Bound | Every deletion of an optimum \((n+1)\)-cover has size at least \(c_n\), yielding nonnegative deletion excess. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| A11 — Inheritance-Debt Averaging | The total deletion excess is state-independent at optimum and its average forces a vertex with bounded excess. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| A12 — Pair-Overlap Ledger | Triple-pair overlaps obey an exact double-counting ledger controlling local collision structure. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| A13 — Five-Set Minimum | The exact minimum number of selected triples required on a five-vertex ground set is classified. | `FINITE_EXHAUSTIVE_THIS_RUN` `V2_REPLAY` | — | ✓ | ✓ |
| A14 — Five-State Ground Classification | The minimum five-vertex states are completely classified up to isomorphism. | `FINITE_EXHAUSTIVE_THIS_RUN` `V2_REPLAY` | — | ✓ | ✓ |
| A15 — Six-Set Local Lower Structure | Six-vertex optimality imposes the exact local coverage/deletion constraints recorded in the finite program. | `PROVED_IN_PACKET` `COURT_READY_AFTER_BASE` | ✓ | ✓ | ✓ |
| A16 — Optimal-State Deletion Recurrence | Optimal states propagate a precise deletion lower-bound recurrence across adjacent ground-set sizes. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| A17 — Frustration Hierarchy Formula | The hierarchy of local coverage deficits admits the exact formula recorded by the program. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| A18 — Sharp Finite Cover Bound | The finite cover bound isolated by the forge is sharp on its stated ground-set scope. | `PROVED_SHARP_BOUND` `COURT_READY_AFTER_BASE` | ✓ | ✓ | ✓ |
| A19 — Optimal-State Degree Constraint | Optimality plus deletion accounting forces the stated exact degree constraint on the finite states in scope. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |

## B-series (15)

| Identity | Statement | Source status | P | L | F |
|---|---|---|:---:|:---:|:---:|
| B01 — Rotor Base State | The canonical rotor state is a valid four-set cover on its stated vertex set. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| B02 — Rotor Deletion Pattern | Rotor deletions have the exact isomorphism/optimality pattern recorded in the finite classifier. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| B03 — Rotor Extension Constraint | Any optimal extension of the rotor must satisfy the stated local incidence constraints. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| B04 — Rotor Pair Construction | The two-rotor construction attains the claimed finite covering size. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| B05 — Rotor Compatibility Rule | Two rooted rotor copies can coexist exactly under the program's compatibility condition. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| B06 — Optimal Seven-State Rotor Presence | The classified optimal seven-states contain the required rotor structure. | `FINITE_EXHAUSTIVE_THIS_RUN` `V2_REPLAY` | — | ✓ | ✓ |
| B07 — Seven-State Orbit Classification | The relevant seven-vertex optimal states fall into the exact finite orbit structure recorded by the replay. | `FINITE_EXHAUSTIVE_THIS_RUN` `V2_REPLAY` | — | ✓ | ✓ |
| B08 — Optimal Deletion Multiplicity | Optimal finite states have the deletion multiplicities stated by the census. | `FINITE_EXHAUSTIVE_THIS_RUN` `V2_REPLAY` | — | ✓ | ✓ |
| B09 — Every Optimal Seven-State Contains a Rotor Deletion | Every optimal seven-state in the classified family has a vertex deletion isomorphic to the canonical rotor state. | `FINITE_EXHAUSTIVE_THIS_RUN` `V2_REPLAY` | — | ✓ | ✓ |
| B10 — Rooted Four-Overlap Compatibility | The allowed rooted four-overlap patterns are exactly those in the finite compatibility census. | `FINITE_EXHAUSTIVE_THIS_RUN` `V2_REPLAY` | — | ✓ | ✓ |
| B11 — Rooted Collision Lower Bound | Compatible rooted collisions obey the stated finite edge lower bound. | `PROVED_BY_FINITE_CENSUS_AND_HUMAN_REPAIR` `COURT_READY_AFTER_FINITE_ROOT` | ✓ | ✓ | ✓ |
| B12 — Optimal Eight-States Have Four Optimal Deletions | Every optimal eight-state in the packet has exactly the stated collection of optimal seven-state deletions. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| B15 — Two-Rotor Five-Overlap Gluing | The five-overlap gluing rule for two rotors is exact on the stated rooted configuration. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| B17 — H1–Rotor Collision Minimum | Every seven-vertex cover containing induced \(H_1\) and induced \(M_2\) on supports sharing four vertices has at least 13 edges; 13 is attainable. | `PROVED_BY_FINITE_CENSUS_AND_HUMAN_REPAIR` `COURT_READY_AFTER_FINITE_ROOT` | ✓ | ✓ | ✓ |
| B19/B20 — Rotor obstruction extension package | The H2/H3 four-overlap impossibility and the recorded Razborov-obstruction extension numbers hold on the finite scopes stated in the source. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |

## C-series (12)

| Identity | Statement | Source status | P | L | F |
|---|---|---|:---:|:---:|:---:|
| C01 — Residual Repair Formulation | Local cover repair after deletion is equivalent to the residual hitting problem stated in the packet. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| C02 — Repair Monotonicity | Enlarging the residual obligation family cannot decrease the minimum repair number. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| C03 — Rooted Repair Lower Bound | The rooted residual configuration has the exact lower bound stated in the repair program. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| C04 — Graph-Generated Covering Classification | The graph-generated cover family is classified exactly under the source hypotheses. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| C05 — Residual Hypergraph Dual | The residual repair problem admits the exact hypergraph dual formulation recorded by the source. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| C06 — Repair Number Subadditivity | Repair numbers obey the source's exact composition/subadditivity inequality. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| C07 — Bad Four-Set Graph Characterization | Bad four-sets are characterized by the graph condition stated in the finite program. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| C08 — Canonical Residual Repair Number | The canonical residual instance has the exact repair number proved in the packet. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| C09 — Independent-Triple Repair Variational Principle | The repair optimization admits the exact independent-triple variational formulation. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| C10 — Fractional Repair Complete Graph | The complete-graph fractional repair problem has the exact value/formula recorded in the packet. | `PROVED_ANALYTIC` `COURT_READY` | ✓ | ✓ | ✓ |
| C11 — Local-to-Residual Transfer | The stated local obstruction transfers exactly to the residual repair instance. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| C13 — General One-Point Dimension Descent | The one-point deletion/descent principle holds in the general finite covering formulation stated by the packet. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |

## D-series (6)

| Identity | Statement | Source status | P | L | F |
|---|---|---|:---:|:---:|:---:|
| D01 — Density Staircase | The normalized finite covering densities form the exact staircase induced by the deletion-excess identities. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| D02 — Plateau Certificate | Zero inheritance debt is an exact certificate for a density plateau. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| D03 — Strict-Rise Certificate | Positive inheritance debt gives a strict normalized-density increase. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| D04 — Hereditary Optimality Criterion | Full optimality of all one-vertex deletions is equivalent to the plateau condition on the stated step. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| D05 — Finite-to-Asymptotic Lower Transfer | Any certified finite density lower bound transfers monotonically to all larger ground-set sizes. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| D06 — Open-Seam Localization | The remaining asymptotic gap is localized to the source's explicitly named finite/analytic extension seam rather than any of the proved identities above. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |

## Scope firewall

- These are theorem identities inside the #500 program, not 52 claims that the parent Turán (3,4) problem is solved.
- Finite census/classification statements retain finite scope.
- Analytic/equivalence statements retain the hypotheses in their source records.
- Historical novelty is intentionally not asserted here; that belongs to the later novelty court.

## Provenance

The original program packet, formal mirrors, records, and verification material are retained elsewhere in this repository. This map exists so a reader no longer has to infer the theorem inventory from campaign files.
