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
| A01 — Complement Covering Duality | Let \(c_n\) be the minimum size of a family \(M\subseteq\binom{[n]}3\) meeting every four-set in a contained triple. Then \[ \operatorname{ex}_3(n,K_4^{(3)})=\binom n3-c_n. \] | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| A02 — Finite-to-Global Density Transfer | If \(M\) covers every four-set on \(n\) vertices and \(4\le s\le n\), then \[ \frac{\|M\|}{\binom n3}\ge \frac{c_s}{\binom s3}. \] | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| A03 — Monotonicity of Normalized Covering Numbers | The sequence \(q_n=c_n/\binom n3\) is nondecreasing for \(n\ge4\). | `PROVED_IN_PACKET` `COURT_READY` | — | ✓ | ✓ |
| A04 — Deletion-Excess Identity | For an \((n+1)\)-vertex four-set cover \(M\), define \(\delta_M(v)=\|M-v\|-c_n\ge0\). Then \[ \sum_v\delta_M(v)=(n-2)\|M\|-(n+1)c_n. \] For optimal \(M\), the right side is the state-independent inheritance debt \(\Delta_n\). | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| A05 — Density-Increment Identity | With \(\Delta_n=(n-2)c_{n+1}-(n+1)c_n\), \[ q_{n+1}-q_n= \frac{6\Delta_n}{(n-2)(n-1)n(n+1)}. \] | `PROVED_IN_PACKET` `COURT_READY` | — | ✓ | ✓ |
| A06 — Plateau–Full-Heredity Equivalence | For \(n\ge4\), \(q_{n+1}=q_n\) iff every vertex deletion of every optimal \((n+1)\)-vertex cover is an optimal n-vertex cover. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| A07 — Plateau Regularity | If \(q_{n+1}=q_n\), every optimal \((n+1)\)-vertex cover is regular of degree \(c_{n+1}-c_n\). | `PROVED_IN_PACKET` `COURT_READY` | — | ✓ | ✓ |
| A08 — Optimal-Deletion Count Bound | For optimal \(M\) on \(n+1\) vertices, if \(z(M)\) is the number of optimal n-vertex deletions, then \[ z(M)\ge n+1-\Delta_n. \] | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| A10 — Deletion-Averaging Recurrence | For \(n\ge4\), \[ c_{n+1}\ge \left\lceil\frac{n+1}{n-2}\,c_n\right\rceil. \] | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| A11 — Four-Set Coverage-Waste Identity | For a cover \(M\), let \(r(S)=\|M\cap\binom S3\|\), \(a_j=\|\{S:r(S)=j\}\|\), and \[ W(M)=(n-3)\|M\|-\binom n4. \] Then \[ W(M)=a_2+2a_3+3a_4. \] | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| A12 — Pair-Overlap Ledger | Let \(d_M(xy)\) be pair codegree. Then \[ W(M)=\sum_{xy}\binom{d_M(xy)}2-a_3-3a_4. \] | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| A13 — Five-Set Minimum | Every five vertices in a four-set cover span at least three selected triples, and three is attainable. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| A14 — Five-State Ground Classification | For a five-set \(X\), map each selected triple \(T\subset X\) to its complementary pair \(X\setminus T\). A three-triple family covers all four-faces iff the resulting three-edge graph is \(P_3\sqcup K_2\). Thus the minimum five-state is unique up to isomorphism. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| A15 — Five-Set Excitation Identity | Define \(\epsilon_5(X)=\|M[X]\|-3\). Then \[ \binom{n-3}{2}\|M\|=3\binom n5+\sum_{X\in\binom V5}\epsilon_5(X), \] and therefore \[ \frac{\|M\|}{\binom n3}=\frac3{10}+\frac1{10}\mathbb E_X\epsilon_5(X). \] | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| A16 — Local Waste–Excitation Identity | For every five-set \(X\), \[ \sum_{\substack{S\subset X\\\|S\|=4}}(r(S)-1)=1+2\epsilon_5(X). \] | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| A17 — Frustration Hierarchy Formula | Let \[ \Lambda_s=\min_M\sum_{X\in\binom{[s]}5}\epsilon_5(X), \] where M ranges over s-vertex covers. Then \[ \Lambda_s=\binom{s-3}{2}c_s-3\binom s5, \] and \[ \sup_s\frac{\Lambda_s}{\binom s5}=\lim_{n\to\infty}10q_n-3. \] Hence Turán (3,4) is equivalent to the supremum being \(13/9\). | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| A18 — Centered Integral Form | For indicator variables \(x_T\in\{0,1\}\), put \(z_T=4x_T-1\in\{-1,3\}\). The covering constraints become \[ \sum_{T\in\binom S3}z_T\ge0\quad\forall S\in\binom V4, \] and the conjectured bound is equivalent to \[ \sum_Tz_T\ge\left(\frac79-o(1)\right)\binom n3. \] | `PROVED_IN_PACKET` `COURT_READY` | — | ✓ | ✓ |
| A19 — General Local-Density Transfer for Covering Designs | For \(r<k\), let \(c_n^{r,k}\) be the minimum number of r-sets meeting every k-set. Every n-vertex \((r,k)\)-cover M and every \(k\le s\le n\) satisfy \[ \frac{\|M\|}{\binom nr}\ge\frac{c_s^{r,k}}{\binom sr}. \] | `PROVED_IN_PACKET` `COURT_READY` | — | ✓ | ✓ |
| A20 — General Deletion Debt and Plateau Rigidity | For an optimal \((r,k)\)-cover \(M\) on \(n+1\) vertices, \[ \sum_v(\|M-v\|-c_n^{r,k})=(n+1-r)c_{n+1}^{r,k}-(n+1)c_n^{r,k}. \] A normalized-density plateau holds iff every deletion is optimal; on a plateau every optimum is regular of degree \(c_{n+1}^{r,k}-c_n^{r,k}\). | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |

## B-series (15)

| Identity | Statement | Source status | P | L | F |
|---|---|---|:---:|:---:|:---:|
| B02 — Unique Five-Vertex Optimum Orbit | There are exactly 30 labeled three-edge covers on five vertices, forming one isomorphism orbit with representative \[ \{012,013,234\}. \] | `FINITE_EXHAUSTIVE_THIS_RUN` `V2_REPLAY` | — | ✓ | ✓ |
| B03 — Unique Six-Vertex Rotor Orbit | There are exactly 30 labeled six-edge covers on six vertices, forming one isomorphism orbit represented by \[ M_2=\{012,013,045,145,234,235\}. \] | `FINITE_EXHAUSTIVE_THIS_RUN` `V2_REPLAY` | — | ✓ | ✓ |
| B04 — Rotor Pair Construction | Partition six vertices into pairs \(A,B,C\), orient them cyclically \(A\to B\to C\to A\), and take all triples consisting of one full pair plus one vertex from its successor pair. The resulting six triples cover every four-set. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| B05 — Rotor Automorphism Group | The automorphism group of \(M_2\) has order 24 and is isomorphic to \[ (C_2)^3\rtimes C_3, \] where the three involutions swap vertices inside the rotor pairs and \(C_3\) cyclically permutes the pairs. | `FINITE_EXHAUSTIVE_THIS_RUN` `V2_REPLAY` | ✓ | ✓ | ✓ |
| B06 — Rotor Degree and Pair-Codegree Profile | In \(M_2\), every vertex has degree 3. Exactly three disjoint pairs have codegree 2, and the other twelve pairs have codegree 1. The codegree-2 pairs form the rotor perfect matching. | `PROVED_IN_PACKET` `COURT_READY` | — | ✓ | ✓ |
| B07 — Rotor Four-Set and Deletion Profiles | Every five-vertex deletion of \(M_2\) has exactly three edges. Among its fifteen four-sets, twelve span one edge and three span two; the three two-edge four-sets are precisely unions of two rotor pairs and are copies of \(B_2\). | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| B09 — Every Optimal Seven-State Contains a Rotor Deletion | Every 12-edge seven-vertex cover has at least one vertex whose deletion is \(M_2\). | `PROVED_IN_PACKET` `COURT_READY_AFTER_BASE` | ✓ | ✓ | ✓ |
| B12 — Optimal Eight-States Have Four Optimal Deletions | Every optimal eight-vertex cover has at least four optimal seven-vertex deletions. Moreover an explicit optimum in the packet has exactly four. | `PROVED_SHARP_BOUND` `COURT_READY_AFTER_BASE` | ✓ | ✓ | ✓ |
| B14 — Nine-Vertex Full Heredity and Regularity | Every optimal nine-vertex cover is 10-regular, and every one of its nine vertex deletions is an optimal eight-vertex cover. | `PROVED_IN_PACKET` `COURT_READY_AFTER_BASE` | — | ✓ | ✓ |
| B15 — Two-Rotor Five-Overlap Gluing | Fix two six-vertex supports in a seven-vertex universe sharing five vertices. There are 30 compatible labeled induced \(M_2\)-pairs, one orbit under support-preserving isomorphisms, and every pair extends to a 12-edge seven-cover. | `FINITE_EXHAUSTIVE_THIS_RUN` `V2_REPLAY` | ✓ | ✓ | ✓ |
| B16 — H1–Rotor Four-Overlap Classification | Fix a five-set and six-set sharing four vertices in a seven-vertex universe. Among 15 labeled \(H_1\) states and 30 labeled \(M_2\) states, exactly 12 induced-compatible pairs exist. They form one support-preserving orbit, and the shared four-set is necessarily \(B_2\). | `FINITE_EXHAUSTIVE_THIS_RUN` `V2_REPLAY` | ✓ | ✓ | ✓ |
| B17 — H1–Rotor Collision Minimum | Every seven-vertex cover containing induced \(H_1\) and induced \(M_2\) on supports sharing four vertices has at least 13 edges; 13 is attainable. | `PROVED_BY_FINITE_CENSUS_AND_HUMAN_REPAIR` `COURT_READY_AFTER_FINITE_ROOT` | ✓ | ✓ | ✓ |
| B18 — Canonical Collision Repair Classification | For a canonical \(H_1/M_2\) overlap, the residual repair number is 3. Exactly three labeled minimum repair sets exist, forming two orbits under the stabilizer of the forced overlap. | `FINITE_EXHAUSTIVE_THIS_RUN` `V2_REPLAY` | — | ✓ | ✓ |
| B19 — H2/H3–Rotor Four-Overlap Impossibility | No induced \(H_2\) or induced \(H_3\) and induced \(M_2\) can have supports intersecting in four vertices. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| B20 — Razborov Obstruction Extension Numbers | For the one-point extension operator, \[ \phi(H_1)=2,\qquad \phi(H_2)=2,\qquad \phi(H_3)=1. \] Thus their minimum six-vertex covering halos have 8, 10, and 10 edges. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |

## C-series (12)

| Identity | Statement | Source status | P | L | F |
|---|---|---|:---:|:---:|:---:|
| C01 — Exact One-Point Extension Operator | Let \(M\) be a four-set cover on V and \(H=\binom V3\setminus M\). Adding a new vertex x requires selecting a pair family \(F\subseteq\binom V2\). The extension \(M\cup\{xab:ab\in F\}\) is a cover iff F contains at least one pair of every triple in H. Hence the minimum extension cost is the pair-cover number \(\tau_2(H)\). | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| C02 — Triangle-Support Complement Formula | For \(G=\binom V2\setminus F\), \[ \tau_2(H)=\binom n2-\max\{\|E(G)\|:K_3(G)\subseteq M\}. \] | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| C03 — Extension Defect and Slack Drift | For an optimal n-cover M define \[ \sigma(M)=\tau_2(\binom V3\setminus M)-(c_{n+1}-c_n)\ge0. \] The cheapest child has exactly \(\sigma(M)\) excess edges above \(c_{n+1}\). More generally, if M has slack s, child slack is \[ s' = s+\tau_2(H)-(c_{n+1}-c_n). \] | `PROVED_IN_PACKET` `COURT_READY` | — | ✓ | ✓ |
| C04 — Graph-Generated Covering Classification | If \(M=K_3(G)\) and M covers every four-set, then \(\overline G\) is a star plus isolated vertices. Conversely every such complement gives a cover. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| C05 — Graph-Generated Density Boundary | Every graph-generated four-set cover satisfies \[ | `PROVED_IN_PACKET` `COURT_READY` | — | — | — |
| C06 — Bad-Four-Set Residual Theorem | If \(K_3(G)\subseteq M\) and \(R=M\setminus K_3(G)\), then R meets every four-set on which G has no triangle. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| C07 — Bad Four-Set Graph Characterization | A graph F on a four-set has no independent triple iff it contains a triangle or two disjoint edges. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| C08 — Disjoint-Edge Bad-Set Bound | For a graph F, let \(\mathcal B(F)\) be four-sets with no independent triple. Then \[ | `PROVED_IN_PACKET` `COURT_READY` | — | — | — |
| C09 — Independent-Triple Repair Variational Principle | For a graph F, let \(i_3(F)\) be its independent triples and \(\rho(F)\) the minimum number of additional triples covering all four-sets with no independent triple. Then \[ c_n=\min_F\bigl(i_3(F)+\rho(F)\bigr). \] | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| C10 — Fractional Repair of the Complete Graph | For F=K_n, the fractional triple cover of all four-sets has value \[ \rho^*(K_n)=\frac14\binom n3. \] | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| C12 — 16/9 Integrality-Gap Equivalence | For F=K_n, \[ \frac{\rho(K_n)}{\rho^*(K_n)}=4q_n. \] Therefore Turán’s conjecture is equivalent to this integrality-gap ratio tending to \(16/9\). | `PROVED_EQUIVALENCE` `COURT_READY` | — | ✓ | ✓ |
| C13 — General One-Point Dimension Descent | For an \((r,k)\)-cover M on V, adding a new vertex x reduces to selecting \((r-1)\)-sets that meet every \((k-1)\)-set S for which M contains no r-subset of S. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |

## D-series (6)

| Identity | Statement | Source status | P | L | F |
|---|---|---|:---:|:---:|:---:|
| D01 — Razborov Obstruction Four-Set Profiles | The induced four-set edge-count profiles are \[ H_1:4^1\,2^4,\qquad H_2:4^1\,3^4,\qquad H_3:4^3\,3^2. \] | `PROVED_IN_PACKET` `COURT_READY` | — | ✓ | ✓ |
| D02 — Unique Shared Root of H1 and M2 | The only four-vertex induced type that can occur as a restriction of both \(H_1\) and \(M_2\) is \(B_2\), the two-edge type with a shared pair. | `PROVED_IN_PACKET` `COURT_READY` | ✓ | ✓ | ✓ |
| D03 — Root Multiplicity Counts | Every induced \(H_1\) contains exactly four \(B_2\) four-subsets; every induced \(M_2\) contains exactly three. | `PROVED_IN_PACKET` `COURT_READY` | — | ✓ | ✓ |
| D04 — Rooted Incidence Chain Rules | Let \(h(Q)\) count outside vertices extending an induced \(B_2\) root Q to \(H_1\), and \(m(Q)\) count outside vertex-pairs extending Q to \(M_2\). Then \[ \sum_Q h(Q)=4N(H_1),\qquad \sum_Q m(Q)=3N(M_2), \] where copies and roots are counted as unlabeled vertex subsets with their induced type. | `PROVED_IN_PACKET` `COURT_READY` | — | ✓ | ✓ |
| D05 — Collision–Segregation Covariance Inequality | For normalized nonnegative root functions h,m, \[ \mathbb E[hm]=\mathbb Eh\,\mathbb Em+\operatorname{Cov}(h,m), \] and \[ \mathbb Eh\,\mathbb Em-\mathbb E[hm]\le \sqrt{\operatorname{Var}(h)\operatorname{Var}(m)}. \] Thus suppressing mixed extensions below the independent-product rate forces rooted variance. | `PROVED_ANALYTIC` `COURT_READY` | — | ✓ | ✓ |
| D07 — H2/H3 Local Halo Surplus | Any six-vertex cover containing induced \(H_2\) or induced \(H_3\) has at least 10 edges, exceeding the six-vertex 4/9 target \(80/9\). An \(H_1\)-containing six-cover may have 8 edges. | `PROVED_IN_PACKET` `COURT_READY` | — | ✓ | ✓ |

## Scope firewall

- These are theorem identities inside the #500 program, not 52 claims that the parent Turán (3,4) problem is solved.
- Finite census/classification statements retain finite scope.
- Analytic/equivalence statements retain the hypotheses in their source records.
- Historical novelty is intentionally not asserted here; that belongs to the later novelty court.

## Provenance

Each row originates in the estate domain `erdos-500-encirclement`; the original program packet, formal mirrors, records, and verification material are retained elsewhere in this repository. This map exists so a reader no longer has to infer the theorem inventory from campaign files.