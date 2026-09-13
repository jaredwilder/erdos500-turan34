# Erdős #500 Encirclement Theorem Forge
## Exact identities, finite ground states, overlap theorems, negative results, theorem candidates, and forced-close programs

**Generated:** 2026-08-04  
**Novelty:** UNRUN for every generated claim; use the local novelty checker.  
**Lean:** UNRUN; Lean names are missions, not receipts.  
**Flagship:** OPEN. No theorem card below closes Turán (3,4) unless a close program’s missing edge is separately certified.

## Claim boundary

This packet applies the Encirclement theorem-refinery doctrine: exact statements, Search/Court separation, proof routes, falsifiers, certificate routes, novelty missions, and forced-close attempts. Published results are separated from newly derived elementary facts, finite computations, and unproved candidates.

### Notation

- \(c_n\): minimum number of triples meeting every four-set on \(n\) vertices.
- \(q_n=c_n/\binom n3\).
- \(M_2=\{012,013,045,145,234,235\}\): the six-vertex rotor.
- \(B_2\): the four-vertex 3-graph with two edges sharing a pair.
- \(H_1,H_2,H_3\): Razborov’s five-vertex forbidden configurations, with exact edge sets recorded in the verification script.

## Executive harvest

- **Total theorem records:** 78
- **Court-ready/finite/published records:** 60
- **Unproved checkable targets:** 18
- **Forced-close programs:** 6
- Fresh high-value finite results include a human-checkable proof of \(c_7=12\), exact \(c_8=20\) and \(c_9=30\), full heredity of every optimal nine-state, unique rotor and collision overlap types, and the 13-edge \(H_1/M_2\) collision theorem.

# A — Covering identities and general blades

## E500-A01 — Complement Covering Duality

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `100/100`  
**Claim hash:** `a4bc02578f5dc549162ac000a88b63880861c2aa7bb661c9541cb921847f00ca`

**Statement.** Let \(c_n\) be the minimum size of a family \(M\subseteq\binom{[n]}3\) meeting every four-set in a contained triple. Then
\[
\operatorname{ex}_3(n,K_4^{(3)})=\binom n3-c_n.
\]

**Proof route.** Take the complement of the edge set. A four-set spans all four triples in the original 3-graph iff its complement contains none of its four triples.

**Falsifier.** A four-set on which the complement/forbidden-clique equivalence fails.

**Verification route.** Direct finite-set proof; exhaustively check all 3-graphs for n≤6 as a regression test.

**Lean mission.** `ex3_tetrahedron_eq_total_sub_coverNumber`

**Novelty queries.**
- `"K4^3-free" complement triple covering every 4-set`
- `"Turan (3,4)" covering duality`

**Flagship relation.** Exact semantic bridge for every close attempt.

---

## E500-A02 — Finite-to-Global Density Transfer

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `95/100`  
**Claim hash:** `e482dafcf2dfb0f48160e895531f0db62c238bb9abe8f496e4a8961d886d93b5`

**Statement.** If \(M\) covers every four-set on \(n\) vertices and \(4\le s\le n\), then
\[
\frac{|M|}{\binom n3}\ge \frac{c_s}{\binom s3}.
\]

**Proof route.** Count pairs \((e,X)\) with \(e\in M\), \(e\subseteq X\), and \(|X|=s\). Every s-set contains at least c_s triples and every triple lies in C(n-3,s-3) s-sets.

**Falsifier.** A cover and an s for which the double-counted incidence inequality reverses.

**Verification route.** Symbolic binomial-identity check plus random finite cover tests.

**Lean mission.** `cover_density_ge_local_cover_density`

**Novelty queries.**
- `"finite to asymptotic" Turan covering density`
- `local covering number averaging hypergraph`

**Flagship relation.** Turns every certified finite value into a universal density bound.

---

## E500-A03 — Monotonicity of Normalized Covering Numbers

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `92/100`  
**Claim hash:** `800449163ee523e33130638dc7ec4a47626f5df809c4f9f4eb656fac8bc7482a`

**Statement.** The sequence \(q_n=c_n/\binom n3\) is nondecreasing for \(n\ge4\).

**Proof route.** Apply E500-A02 to an optimal (n+1)-vertex cover with s=n.

**Falsifier.** An n with q_(n+1)<q_n.

**Verification route.** Exact arithmetic check using any independently verified finite c_n table.

**Lean mission.** `normalized_coverNumber_mono`

**Novelty queries.**
- `normalized covering number monotone induced subsets`
- `Turan 3 4 finite density monotonicity`

**Flagship relation.** Supremum of finite densities equals the asymptotic covering density.

---

## E500-A04 — Deletion-Excess Identity

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `100/100`  
**Claim hash:** `1472f7ccc35db52e0fd3c01077cfe7a3dc707cf599261a3791379d3b21f0292e`

**Statement.** For an \((n+1)\)-vertex four-set cover \(M\), define
\(\delta_M(v)=|M-v|-c_n\ge0\). Then
\[
\sum_v\delta_M(v)=(n-2)|M|-(n+1)c_n.
\]
For optimal \(M\), the right side is the state-independent inheritance debt \(\Delta_n\).

**Proof route.** Each triple survives in exactly n-2 of the n+1 vertex deletions. Sum deletion sizes and subtract the baseline (n+1)c_n.

**Falsifier.** A cover whose summed deletion sizes are not (n-2)|M|.

**Verification route.** Direct incidence checker over arbitrary finite edge lists.

**Lean mission.** `sum_deletionExcess_eq_inheritanceDebt`

**Novelty queries.**
- `deletion excess extremal hypergraph covering`
- `hereditary extremal state debt identity`

**Flagship relation.** Converts cross-order nonheredity into exact density gain.

---

## E500-A05 — Density-Increment Identity

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `98/100`  
**Claim hash:** `727b69343099efe2619ca86ead42a95c00e84d3094db23bac5d00948ee84bf99`

**Statement.** With \(\Delta_n=(n-2)c_{n+1}-(n+1)c_n\),
\[
q_{n+1}-q_n=
\frac{6\Delta_n}{(n-2)(n-1)n(n+1)}.
\]

**Proof route.** Substitute c_n=q_n C(n,3) into E500-A04 and simplify.

**Falsifier.** An exact c_n sequence violating the displayed algebraic identity.

**Verification route.** Rational symbolic simplification and integer table replay.

**Lean mission.** `cover_density_increment_eq_debt`

**Novelty queries.**
- `extremal density increment deletion excess`
- `covering number hereditary debt`

**Dependencies.** `E500-A04`

**Flagship relation.** Makes the finite density staircase a weighted sum of inheritance failures.

---

## E500-A06 — Plateau–Full-Heredity Equivalence

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `96/100`  
**Claim hash:** `a5a2766cffdd22403f91832a80329828e33c484c8cbf15e182e403c996e23e16`

**Statement.** For \(n\ge4\), \(q_{n+1}=q_n\) iff every vertex deletion of every optimal \((n+1)\)-vertex cover is an optimal n-vertex cover.

**Proof route.** By E500-A05, a plateau is equivalent to Δ_n=0. Every deletion excess is a nonnegative integer, so their sum is zero iff all are zero.

**Falsifier.** An optimal cover on a density plateau with a nonoptimal deletion, or conversely.

**Verification route.** Finite c_n replay and deletion enumeration for small n.

**Lean mission.** `cover_density_plateau_iff_all_deletions_optimal`

**Novelty queries.**
- `density plateau hereditary extremal hypergraph`
- `all deletions optimal covering design`

**Dependencies.** `E500-A04`, `E500-A05`

**Flagship relation.** A numerical plateau forces complete state-space rigidity.

---

## E500-A07 — Plateau Regularity

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `88/100`  
**Claim hash:** `35646fdbdf4f10f51dd8b993753056a8f47899e3580505ed011c99d643cdf735`

**Statement.** If \(q_{n+1}=q_n\), every optimal \((n+1)\)-vertex cover is regular of degree \(c_{n+1}-c_n\).

**Proof route.** Under E500-A06, |M-v|=c_n for every v, so d_M(v)=c_{n+1}-c_n.

**Falsifier.** A plateau optimum with unequal vertex degrees.

**Verification route.** Degree computation on any finite plateau instance.

**Lean mission.** `plateau_optimal_cover_regular`

**Novelty queries.**
- `plateau regularity covering hypergraph`
- `hereditary optimum regular 3-graph`

**Dependencies.** `E500-A06`

**Flagship relation.** Produces rigid equality-case structure.

---

## E500-A08 — Optimal-Deletion Count Bound

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `90/100`  
**Claim hash:** `28dfaf1bd71a6e0a7c887f3fab31b584d742771fc096a93e0503f1d7c0282b20`

**Statement.** For optimal \(M\) on \(n+1\) vertices, if \(z(M)\) is the number of optimal n-vertex deletions, then
\[
z(M)\ge n+1-\Delta_n.
\]

**Proof route.** The n+1-z nonoptimal deletions each have integer excess at least one; their total is Δ_n.

**Falsifier.** An optimum with fewer optimal deletions than the bound.

**Verification route.** Enumerate deletion sizes of certified finite optima.

**Lean mission.** `optimalDeletion_count_ge_vertices_sub_debt`

**Novelty queries.**
- `number of optimal deletions inheritance debt`
- `extremal state hereditary count`

**Dependencies.** `E500-A04`

**Flagship relation.** Immediately forces embedded smaller optima when Δ_n is small.

---

## E500-A09 — Cumulative Inheritance-Debt Expansion

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `93/100`  
**Claim hash:** `ee730a41a64f64511975a2403f820e93ed3a2f5fb27a2abd3b1f449aadd336dc`

**Statement.** For \(N>n_0\),
\[
q_N=q_{n_0}+\sum_{n=n_0}^{N-1}
\frac{6\Delta_n}{(n-2)(n-1)n(n+1)}.
\]

**Proof route.** Telescoping E500-A05.

**Falsifier.** A finite c_n sequence for which the telescoped identity fails.

**Verification route.** Exact rational replay.

**Lean mission.** `cover_density_eq_base_add_debt_sum`

**Novelty queries.**
- `cumulative deletion debt Turan density`
- `extremal covering density telescoping`

**Dependencies.** `E500-A05`

**Flagship relation.** Recasts the asymptotic conjecture as a lifetime debt sum.

---

## E500-A10 — Deletion-Averaging Recurrence

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `95/100`  
**Claim hash:** `74656bfd8671d0bb9ea05ba8271b106c1e9f5e960bf19bd976bad281f2c32eba`

**Statement.** For \(n\ge4\),
\[
c_{n+1}\ge \left\lceil\frac{n+1}{n-2}\,c_n\right\rceil.
\]

**Proof route.** Every deletion of an (n+1)-cover has at least c_n edges, while the sum of deletion sizes is (n-2)|M|.

**Falsifier.** A cover below the rounded lower bound.

**Verification route.** Exact arithmetic plus finite witness checks.

**Lean mission.** `coverNumber_succ_ge_ceiling_ratio`

**Novelty queries.**
- `covering number deletion recurrence`
- `Turan finite recurrence c_n`

**Flagship relation.** Closes c_8 and c_9 from smaller exact values and witnesses.

---

## E500-A11 — Four-Set Coverage-Waste Identity

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `95/100`  
**Claim hash:** `3828db37dec741d1be4d151806a43acf6594283ec6db6467e4909e9731788c92`

**Statement.** For a cover \(M\), let \(r(S)=|M\cap\binom S3|\), \(a_j=|\{S:r(S)=j\}|\), and
\[
W(M)=(n-3)|M|-\binom n4.
\]
Then
\[
W(M)=a_2+2a_3+3a_4.
\]

**Proof route.** Each selected triple lies in n-3 four-sets, so sum_S r(S)=(n-3)|M|. Subtract one mandatory hit per four-set.

**Falsifier.** A cover whose incidence count does not match the multiplicity ledger.

**Verification route.** Direct combinatorial counter over an edge list.

**Lean mission.** `coverageWaste_eq_fourMultiplicityExcess`

**Novelty queries.**
- `coverage waste four-set multiplicity hypergraph`
- `redundant triple covering ledger`

**Flagship relation.** Converts the 4/9 conjecture into a redundancy lower bound.

---

## E500-A12 — Pair-Overlap Ledger

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `99/100`  
**Claim hash:** `177f54d8b2e5c7c4be6caa481600a45b5ec1d36b87e1d599b96a2703cc77713d`

**Statement.** Let \(d_M(xy)\) be pair codegree. Then
\[
W(M)=\sum_{xy}\binom{d_M(xy)}2-a_3-3a_4.
\]

**Proof route.** Two selected triples lie in a common four-set iff they share a pair, giving sum C(d(xy),2)=a_2+3a_3+6a_4. Subtract the formula in E500-A11.

**Falsifier.** A cover violating either exact pair-overlap count.

**Verification route.** Direct pair-codegree and four-set-multiplicity checker.

**Lean mission.** `coverageWaste_eq_pairOverlap_sub_clusterRebate`

**Novelty queries.**
- `pair codegree overlap clustering rebate`
- `Turan 3 4 overlap ledger`

**Dependencies.** `E500-A11`

**Flagship relation.** Isolates gross overlap pressure versus clustering rebate.

---

## E500-A13 — Five-Set Minimum

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `90/100`  
**Claim hash:** `72711d67e597cc0b27635c847f1316e9ef1ee1b7ce0e0b36d4fdd4a880f45b3d`

**Statement.** Every five vertices in a four-set cover span at least three selected triples, and three is attainable.

**Proof route.** A selected triple covers exactly two of the five four-faces of a five-set; two triples cover at most four faces. Give an explicit three-triple cover.

**Falsifier.** A five-set covered by at most two triples.

**Verification route.** Exhaustively enumerate C(10,0)+C(10,1)+C(10,2) candidates.

**Lean mission.** `fiveVertex_cover_min_three`

**Novelty queries.**
- `five vertex triple covering minimum`
- `local Turan 3 4 five vertices`

**Flagship relation.** Creates the first nontrivial local ground state.

---

## E500-A14 — Five-State Ground Classification

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `96/100`  
**Claim hash:** `b146c9b66ed85d61813d8d7b4faa4ea08682f4e649eaa7b125a6125eee3edba5`

**Statement.** For a five-set \(X\), map each selected triple \(T\subset X\) to its complementary pair \(X\setminus T\). A three-triple family covers all four-faces iff the resulting three-edge graph is \(P_3\sqcup K_2\). Thus the minimum five-state is unique up to isomorphism.

**Proof route.** A four-face X\{v} is covered iff v is incident to a complementary pair. A three-edge graph on five vertices with no isolated vertex must have components of orders 3 and 2, hence P3 and K2.

**Falsifier.** A distinct three-edge no-isolate graph on five vertices.

**Verification route.** Exhaustive graph and triple-family enumeration; 30 labeled realizations.

**Lean mission.** `fiveGroundState_iff_complementPairGraph_P3_disjoint_K2`

**Novelty queries.**
- `P3 union K2 five vertex triple cover`
- `unique local ground state Turan 3 4`

**Dependencies.** `E500-A13`

**Flagship relation.** Gives a finite alphabet for local-state and Lean formalization.

---

## E500-A15 — Five-Set Excitation Identity

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `100/100`  
**Claim hash:** `61f54e40aea13d9d7b1bc8dd42bb0a4f33b20f7138f5dc6f3816bd5b0800a7b9`

**Statement.** Define \(\epsilon_5(X)=|M[X]|-3\). Then
\[
\binom{n-3}{2}|M|=3\binom n5+\sum_{X\in\binom V5}\epsilon_5(X),
\]
and therefore
\[
\frac{|M|}{\binom n3}=\frac3{10}+\frac1{10}\mathbb E_X\epsilon_5(X).
\]

**Proof route.** Count each selected triple in the C(n-3,2) five-sets containing it, then use C(n-3,2)C(n,3)=10C(n,5).

**Falsifier.** A cover whose triple/five-set incidence count fails.

**Verification route.** Exact integer and rational checker.

**Lean mission.** `cover_density_eq_threeTenths_add_meanFiveExcitation`

**Novelty queries.**
- `five-set excitation identity hypergraph covering`
- `average local excess 13/9 Turan`

**Flagship relation.** The conjecture is equivalent to mean excitation at least 13/9.

---

## E500-A16 — Local Waste–Excitation Identity

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `88/100`  
**Claim hash:** `eeb35b1a7c0d81669e0e21889cba9adfa058dedaf77a147253fc7fdac1d8b7b4`

**Statement.** For every five-set \(X\),
\[
\sum_{\substack{S\subset X\\|S|=4}}(r(S)-1)=1+2\epsilon_5(X).
\]

**Proof route.** Each selected triple in X belongs to exactly two of its five four-faces, so the left side is 2|M[X]|-5.

**Falsifier.** A five-set violating the local incidence count.

**Verification route.** Direct local checker.

**Lean mission.** `fiveExcitation_eq_half_localWaste_sub_one`

**Novelty queries.**
- `five-set excess four-face waste identity`
- `local coverage waste excitation`

**Dependencies.** `E500-A11`, `E500-A15`

**Flagship relation.** Unifies four-set waste and five-state language.

---

## E500-A17 — Frustration Hierarchy Formula

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `100/100`  
**Claim hash:** `21138d7571b3a248b60a496958c83454dca3804bf4940efb5dfdf4c7aca79631`

**Statement.** Let
\[
\Lambda_s=\min_M\sum_{X\in\binom{[s]}5}\epsilon_5(X),
\]
where M ranges over s-vertex covers. Then
\[
\Lambda_s=\binom{s-3}{2}c_s-3\binom s5,
\]
and
\[
\sup_s\frac{\Lambda_s}{\binom s5}=\lim_{n\to\infty}10q_n-3.
\]
Hence Turán (3,4) is equivalent to the supremum being \(13/9\).

**Proof route.** Use E500-A15 on an optimal s-cover and finite-to-global transfer; q_s is monotone and converges to the asymptotic covering density.

**Falsifier.** A finite s for which the exact formula fails, or a mismatch between the supremum and density limit.

**Verification route.** Exact c_s table replay and symbolic binomial algebra.

**Lean mission.** `frustrationHierarchy_eq_coverDensity`

**Novelty queries.**
- `frustration hierarchy five-state excitation`
- `local ground state integrality gap Turan`

**Dependencies.** `E500-A03`, `E500-A15`

**Flagship relation.** Exact local-to-global target for discharging or flag certificates.

---

## E500-A18 — Centered Integral Form

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `85/100`  
**Claim hash:** `a55ff3f46f89b25958e7b262d6342f29e49ec5e61d04e1a956670ee0fe5867d5`

**Statement.** For indicator variables \(x_T\in\{0,1\}\), put \(z_T=4x_T-1\in\{-1,3\}\). The covering constraints become
\[
\sum_{T\in\binom S3}z_T\ge0\quad\forall S\in\binom V4,
\]
and the conjectured bound is equivalent to
\[
\sum_Tz_T\ge\left(\frac79-o(1)\right)\binom n3.
\]

**Proof route.** Each four-set sum equals 4(r(S)-1). Also sum z=4|M|-C(n,3).

**Falsifier.** A binary covering vector that violates the algebraic equivalence.

**Verification route.** Bit-vector checker and exact arithmetic.

**Lean mission.** `centeredIntegral_coverForm`

**Novelty queries.**
- `{-1,3} four-face nonnegative hypergraph`
- `integral Turan centered variables`

**Flagship relation.** Exposes the problem as an integrality theorem over a two-point alphabet.

---

## E500-A19 — General Local-Density Transfer for Covering Designs

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `82/100`  
**Claim hash:** `83d4da5e056cdb1f254d701de6bf5e1905608663b016ddb836452082e1e85b13`

**Statement.** For \(r<k\), let \(c_n^{r,k}\) be the minimum number of r-sets meeting every k-set. Every n-vertex \((r,k)\)-cover M and every \(k\le s\le n\) satisfy
\[
\frac{|M|}{\binom nr}\ge\frac{c_s^{r,k}}{\binom sr}.
\]

**Proof route.** Double count (r-edge,s-set) incidences exactly as in E500-A02.

**Falsifier.** A covering-design instance violating the incidence count.

**Verification route.** Generic finite-set theorem; specialize to r=3,k=4.

**Lean mission.** `general_cover_density_ge_local`

**Novelty queries.**
- `covering design normalized number monotonicity`
- `r-set hits every k-set local density transfer`

**Flagship relation.** Transfers the RSI blade beyond Erdős #500.

---

## E500-A20 — General Deletion Debt and Plateau Rigidity

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `86/100`  
**Claim hash:** `913639e82b5a05e2df71f5841c49f295b561141bbc7c2c48aedff4965aa737ad`

**Statement.** For an optimal \((r,k)\)-cover \(M\) on \(n+1\) vertices,
\[
\sum_v(|M-v|-c_n^{r,k})=(n+1-r)c_{n+1}^{r,k}-(n+1)c_n^{r,k}.
\]
A normalized-density plateau holds iff every deletion is optimal; on a plateau every optimum is regular of degree \(c_{n+1}^{r,k}-c_n^{r,k}\).

**Proof route.** Each r-edge survives in n+1-r deletions; nonnegative deletion excess gives the equivalence and regularity.

**Falsifier.** A covering design violating the deletion incidence or plateau conclusion.

**Verification route.** Generic Lean finite-set formalization.

**Lean mission.** `general_cover_deletionDebt_plateauRigidity`

**Novelty queries.**
- `covering design hereditary plateau regularity`
- `general deletion excess extremal set systems`

**Flagship relation.** A potentially reusable general theorem family.

---

# B — Finite ground states and overlap theorems

## E500-B01 — Exact Small Values c4,c5,c6

**Status:** `FINITE_EXHAUSTIVE_THIS_RUN`  
**Authority:** `V2_REPLAY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `90/100`  
**Claim hash:** `8289f608d802d9f72da17df5667dc4450a0da6403c54660080fa7bea33f1aae0`

**Statement.** \[
c_4=1,\qquad c_5=3,\qquad c_6=6.
\]

**Proof route.** Enumerate all fixed-size triple families; prove lower sizes impossible and provide witnesses.

**Falsifier.** A smaller covering family at any of n=4,5,6.

**Verification route.** Standard-library exhaustive script included; independent implementation recommended.

**Lean mission.** `native_decide_coverNumbers_4_5_6`

**Novelty queries.**
- `exact Turan 3 4 small covering values 4 5 6`
- `minimum triples every four-set six vertices`

**Flagship relation.** Base cases for all finite-state theorems.

---

## E500-B02 — Unique Five-Vertex Optimum Orbit

**Status:** `FINITE_EXHAUSTIVE_THIS_RUN`  
**Authority:** `V2_REPLAY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `82/100`  
**Claim hash:** `27232135006e05f370da2e6e87c4875553b7acbf71278d6a5d65dc6600f7c349`

**Statement.** There are exactly 30 labeled three-edge covers on five vertices, forming one isomorphism orbit with representative
\[
\{012,013,234\}.
\]

**Proof route.** Enumerate the 120 three-triple families and canonicalize under S5.

**Falsifier.** A second canonical orbit or a different labeled count.

**Verification route.** Included exhaustive and canonical-label checker.

**Lean mission.** `native_decide_unique_fiveCover_orbit`

**Novelty queries.**
- `30 labeled minimum covers five vertices`
- `unique five vertex Turan covering orbit`

**Dependencies.** `E500-A14`

**Flagship relation.** Computational receipt supporting E500-A14.

---

## E500-B03 — Unique Six-Vertex Rotor Orbit

**Status:** `FINITE_EXHAUSTIVE_THIS_RUN`  
**Authority:** `V2_REPLAY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `100/100`  
**Claim hash:** `7fdaf7fc1f8017a8bb314f98f4d72a2e71ff8190bc0b976a8d2b9df93a0b077a`

**Statement.** There are exactly 30 labeled six-edge covers on six vertices, forming one isomorphism orbit represented by
\[
M_2=\{012,013,045,145,234,235\}.
\]

**Proof route.** Enumerate C(20,6)=38,760 candidates, filter covers, and canonicalize under S6.

**Falsifier.** A second orbit, a non-cover in the listed orbit, or a different count.

**Verification route.** Included exhaustive checker; matches Razborov's published uniqueness statement for M2.

**Lean mission.** `native_decide_unique_sixCover_rotor`

**Novelty queries.**
- `unique six vertex six edge Turan covering M2`
- `rotor hypergraph 30 labeled`

**Flagship relation.** Central finite ground state and published-prior-art collision.

---

## E500-B04 — Rotor Pair Construction

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `88/100`  
**Claim hash:** `39997bd78d63755b56154f3b60ad9648f7c415143130e7595d294ea5053197a6`

**Statement.** Partition six vertices into pairs \(A,B,C\), orient them cyclically \(A\to B\to C\to A\), and take all triples consisting of one full pair plus one vertex from its successor pair. The resulting six triples cover every four-set.

**Proof route.** Any four vertices either contain a full pair and a successor vertex, or consist of two full pairs; in both cases one construction edge is present.

**Falsifier.** A four-set with no rotor edge.

**Verification route.** Direct exhaustive check for the symbolic representative.

**Lean mission.** `rotorPairCycle_is_cover`

**Novelty queries.**
- `three pairs cyclic six-edge covering`
- `M2 rotor construction Turan`

**Flagship relation.** Human construction underlying M2.

---

## E500-B05 — Rotor Automorphism Group

**Status:** `FINITE_EXHAUSTIVE_THIS_RUN`  
**Authority:** `V2_REPLAY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `65/100`  
**Claim hash:** `b4f33fe68a5b58522dcf6e413ef2570fc117c550584f76e8ab047175837408fc`

**Statement.** The automorphism group of \(M_2\) has order 24 and is isomorphic to
\[
(C_2)^3\rtimes C_3,
\]
where the three involutions swap vertices inside the rotor pairs and \(C_3\) cyclically permutes the pairs.

**Proof route.** The displayed subgroup has order 24; orbit-stabilizer with 30 labeled copies gives |Aut(M2)|=6!/30=24.

**Falsifier.** An automorphism outside the displayed group or failure of a displayed map.

**Verification route.** Enumerate all 720 vertex permutations.

**Lean mission.** `automorphismGroup_rotor_order24`

**Novelty queries.**
- `automorphism group M2 Turan six vertex`
- `rotor hypergraph C2^3 semidirect C3`

**Flagship relation.** Useful for symmetry-reduced SAT/Lean.

---

## E500-B06 — Rotor Degree and Pair-Codegree Profile

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `85/100`  
**Claim hash:** `101c35d8895f4f67463430a5e55384c7c7d2563d58bb405ce4d3ae1ba82edc71`

**Statement.** In \(M_2\), every vertex has degree 3. Exactly three disjoint pairs have codegree 2, and the other twelve pairs have codegree 1. The codegree-2 pairs form the rotor perfect matching.

**Proof route.** Read from the pair-cycle construction or count directly on the representative.

**Falsifier.** A vertex or pair with a different degree/codegree.

**Verification route.** Direct edge-list checker.

**Lean mission.** `rotor_degree_codegree_profile`

**Novelty queries.**
- `M2 pair codegree perfect matching`
- `six vertex rotor codegree profile`

**Dependencies.** `E500-B04`

**Flagship relation.** Supplies the pair-positive lemma used in the c7 human proof.

---

## E500-B07 — Rotor Four-Set and Deletion Profiles

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `88/100`  
**Claim hash:** `de58334b2430ee83b02f1fb64c0825046ed847980142153c38c7cd5d77ebeea8`

**Statement.** Every five-vertex deletion of \(M_2\) has exactly three edges. Among its fifteen four-sets, twelve span one edge and three span two; the three two-edge four-sets are precisely unions of two rotor pairs and are copies of \(B_2\).

**Proof route.** Directly inspect the pair-cycle construction; deletion count also follows from 3-regularity.

**Falsifier.** A deletion or four-set with a different edge count.

**Verification route.** Included profile checker.

**Lean mission.** `rotor_deletion_fourSet_profiles`

**Novelty queries.**
- `M2 four-set profile 1^12 2^3`
- `rotor B2 roots`

**Dependencies.** `E500-B04`, `E500-B06`

**Flagship relation.** Creates the shared rooted state for collision mining.

---

## E500-B08 — Exact Seven-Vertex Covering Number

**Status:** `PROVED_FROM_FINITE_BASE_AND_WITNESS`  
**Authority:** `COURT_READY_AFTER_BASE`  
**Novelty:** `UNRUN`  
**Structural leverage:** `100/100`  
**Claim hash:** `66fafaf0973ee7810197c3ba4856a07ffa945d7922e8669f117ff80f3a85777e`

**Statement.** The minimum seven-vertex covering number is
\[
c_7=12.
\]

**Proof route.** Upper bound: verify the explicit 12-edge witness in the packet. Lower bound: assume an 11-edge cover. Every vertex degree is at most 5 because each deletion is a six-vertex cover. The degree multiset is \(5^5,4^2\). Deleting a degree-5 vertex gives \(M_2\). Hence high-high pair codegrees are 2 and high-low pair codegrees are 1. Counting triple types forces exactly two high-high-low edges. Any such edge, after deleting one high endpoint, leaves a high-low pair of codegree zero in \(M_2\), contradicting E500-B06.

**Falsifier.** An 11-edge cover or an error in the degree/codegree deductions.

**Verification route.** Included witness and proof-assumption checker; the only finite base used is exhaustive E500-B03.

**Lean mission.** `coverNumber_seven_eq_twelve`

**Novelty queries.**
- `c7=12 Turan 3 4 covering human proof`
- `seven vertex minimum triple cover every four-set`

**Dependencies.** `E500-B03`, `E500-B06`

**Flagship relation.** Turns the solver result into a short checkable theorem.

---

## E500-B09 — Every Optimal Seven-State Contains a Rotor Deletion

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY_AFTER_BASE`  
**Novelty:** `UNRUN`  
**Structural leverage:** `93/100`  
**Claim hash:** `d4ae658a02927db9945207c6a130f3fa299c9218e6da02bb37ee7171b9e4f307`

**Statement.** Every 12-edge seven-vertex cover has at least one vertex whose deletion is \(M_2\).

**Proof route.** From E500-A04, total deletion excess over c6 is (7-3)12-7·6=6. Seven nonnegative integer excesses sum to 6, so at least one is zero; E500-B03 identifies the deletion.

**Falsifier.** An optimal seven-cover with all seven deletions above six edges.

**Verification route.** Enumerate deletion sizes of any witness; formal proof uses only debt identity and c6.

**Lean mission.** `optimalSeven_contains_rotorDeletion`

**Novelty queries.**
- `every optimal seven cover contains M2`
- `deletion debt rotor core`

**Dependencies.** `E500-A04`, `E500-B03`, `E500-B08`

**Flagship relation.** Explains why all n=7 optima inherit the same ground-state core.

---

## E500-B10 — Sharp Seven-State Deletion Spectrum Witness

**Status:** `COMPUTATIONAL_WITNESS_THIS_RUN`  
**Authority:** `V2_REPLAY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `70/100`  
**Claim hash:** `066577d784c6a588aad7159f99d787a7dcde52b306bb08592f4d0134cdc72618`

**Statement.** There exists an optimal seven-vertex cover with deletion-excess spectrum
\[
\{0,1,1,1,1,1,1\}
\]
over the six-vertex optimum.

**Proof route.** Use the explicit 12-edge witness whose degree sequence is \(6,5,5,5,5,5,5\); deletion size is 12-d(v).

**Falsifier.** The witness fails coverage, has another degree sequence, or is not optimal.

**Verification route.** Included witness checker plus E500-B08.

**Lean mission.** `exists_optimalSeven_deletionSpectrum_0_1x6`

**Novelty queries.**
- `seven vertex optimum one rotor deletion spectrum`
- `n=7 Turan alternative optimum deletion deck`

**Flagship relation.** Sharpens the optimal-deletion count bound.

---

## E500-B11 — Exact Eight-Vertex Covering Number

**Status:** `PROVED_FROM_RECURRENCE_AND_WITNESS`  
**Authority:** `COURT_READY_AFTER_BASE`  
**Novelty:** `UNRUN`  
**Structural leverage:** `95/100`  
**Claim hash:** `5071c292c54a76a31b168a6d78d055a460142939efce50c8343f7807005dcab9`

**Statement.** \[
c_8=20.
\]

**Proof route.** Lower bound E500-A10 gives c8≥ceil(8·12/5)=20. Verify the explicit 20-edge witness.

**Falsifier.** A cover with at most19 edges or invalid witness.

**Verification route.** Included witness checker; lower proof is arithmetic from E500-B08.

**Lean mission.** `coverNumber_eight_eq_twenty`

**Novelty queries.**
- `c8=20 Turan 3 4 covering`
- `eight vertex minimum triple cover every four-set`

**Dependencies.** `E500-A10`, `E500-B08`

**Flagship relation.** Adds an exact frontier value with a tiny proof.

---

## E500-B12 — Optimal Eight-States Have Four Optimal Deletions

**Status:** `PROVED_SHARP_BOUND`  
**Authority:** `COURT_READY_AFTER_BASE`  
**Novelty:** `UNRUN`  
**Structural leverage:** `86/100`  
**Claim hash:** `1b3d3b8df8d95bbe0f5dec3df5948b485b7b72742a6f374908bbe05c782da4f9`

**Statement.** Every optimal eight-vertex cover has at least four optimal seven-vertex deletions. Moreover an explicit optimum in the packet has exactly four.

**Proof route.** Debt is Δ7=5·20-8·12=4; E500-A08 gives at least 8-4=4 optimal deletions. The witness degree sequence \(8,8,8,8,7,7,7,7\) has exactly four deletions of size12.

**Falsifier.** An optimum with fewer than four optimal deletions, or failure of the witness.

**Verification route.** Included degree/deletion checker.

**Lean mission.** `optimalEight_optimalDeletionCount_ge_four_sharp`

**Novelty queries.**
- `eight vertex optimum four optimal deletions`
- `inheritance debt c7 c8 sharp`

**Dependencies.** `E500-A08`, `E500-B08`, `E500-B11`

**Flagship relation.** Exact cross-order state-geometry theorem.

---

## E500-B13 — Exact Nine-Vertex Covering Number

**Status:** `PROVED_FROM_RECURRENCE_AND_WITNESS`  
**Authority:** `COURT_READY_AFTER_BASE`  
**Novelty:** `UNRUN`  
**Structural leverage:** `95/100`  
**Claim hash:** `8e48d35e750655a87fb80561cfd913b38752aa1579131b6e9e46180b6bd7c538`

**Statement.** \[
c_9=30.
\]

**Proof route.** Lower bound E500-A10 gives c9≥ceil(9·20/6)=30. Verify the explicit 30-edge witness.

**Falsifier.** A cover with at most29 edges or invalid witness.

**Verification route.** Included witness checker.

**Lean mission.** `coverNumber_nine_eq_thirty`

**Novelty queries.**
- `c9=30 Turan 3 4 covering`
- `nine vertex minimum triple cover every four-set`

**Dependencies.** `E500-A10`, `E500-B11`

**Flagship relation.** Extends the exact staircase.

---

## E500-B14 — Nine-Vertex Full Heredity and Regularity

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY_AFTER_BASE`  
**Novelty:** `UNRUN`  
**Structural leverage:** `92/100`  
**Claim hash:** `2f248a38754fa505e0580ade11d306b0964fc35b5f744d4c43c390b17e8d6546`

**Statement.** Every optimal nine-vertex cover is 10-regular, and every one of its nine vertex deletions is an optimal eight-vertex cover.

**Proof route.** q8=20/56=5/14 and q9=30/84=5/14, so E500-A06 and A07 apply.

**Falsifier.** An optimal nine-cover with a nonoptimal deletion or nonconstant degree.

**Verification route.** Finite c8,c9 certificates plus symbolic theorem.

**Lean mission.** `optimalNine_fullyHereditary_regular10`

**Novelty queries.**
- `nine vertex Turan cover fully hereditary`
- `c8 c9 density plateau regularity`

**Dependencies.** `E500-A06`, `E500-A07`, `E500-B11`, `E500-B13`

**Flagship relation.** A strong equality-case theorem extracted from the plateau.

---

## E500-B15 — Two-Rotor Five-Overlap Gluing

**Status:** `FINITE_EXHAUSTIVE_THIS_RUN`  
**Authority:** `V2_REPLAY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `88/100`  
**Claim hash:** `9cfa682182448082a3a0928cc30da7a8cb856a90ac32ad61d1d27b56d42912aa`

**Statement.** Fix two six-vertex supports in a seven-vertex universe sharing five vertices. There are 30 compatible labeled induced \(M_2\)-pairs, one orbit under support-preserving isomorphisms, and every pair extends to a 12-edge seven-cover.

**Proof route.** Enumerate all 30 labelings on each support, require equality on the shared five-set, canonicalize, and brute-force the five free triples.

**Falsifier.** A compatible pair needing more or fewer than 12 total edges, or a second orbit.

**Verification route.** Included finite overlap checker.

**Lean mission.** `twoRotors_fiveOverlap_uniqueOrbit_completion12`

**Novelty queries.**
- `two M2 overlap five vertices completion`
- `rotor gluing seven vertex Turan`

**Flagship relation.** Positive gluing theorem contrasting the costly H1 collision.

---

## E500-B16 — H1–Rotor Four-Overlap Classification

**Status:** `FINITE_EXHAUSTIVE_THIS_RUN`  
**Authority:** `V2_REPLAY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `98/100`  
**Claim hash:** `836c9c5a28410319a631ba7863a875b104ef5e6117ea2dcfae9cf468378e3394`

**Statement.** Fix a five-set and six-set sharing four vertices in a seven-vertex universe. Among 15 labeled \(H_1\) states and 30 labeled \(M_2\) states, exactly 12 induced-compatible pairs exist. They form one support-preserving orbit, and the shared four-set is necessarily \(B_2\).

**Proof route.** Enumerate labelings, compare exact induced edge sets on the shared root, and canonicalize under S4×S2.

**Falsifier.** A different compatible count, a second orbit, or a non-B2 shared root.

**Verification route.** Included overlap census.

**Lean mission.** `H1_rotor_fourOverlap_uniqueOrbit`

**Novelty queries.**
- `H1 M2 compatible overlap B2 root`
- `Razborov obstruction rotor collision`

**Dependencies.** `E500-B07`

**Flagship relation.** Compresses all smallest collisions to one finite type.

---

## E500-B17 — H1–Rotor Collision Minimum

**Status:** `PROVED_BY_FINITE_CENSUS_AND_HUMAN_REPAIR`  
**Authority:** `COURT_READY_AFTER_FINITE_ROOT`  
**Novelty:** `UNRUN`  
**Structural leverage:** `100/100`  
**Claim hash:** `3d2a8f502a8770d16b493971d7c4a01b56ecdc10a493ab47a7e6aa4c693ce48d`

**Statement.** Every seven-vertex cover containing induced \(H_1\) and induced \(M_2\) on supports sharing four vertices has at least 13 edges; 13 is attainable.

**Proof route.** By E500-B16 reduce to one canonical overlap with 10 forced edges. Six four-sets remain uncovered. The free triples form a 9-vertex hitting instance: the four middle constraints require both a 5-side and a 6-side repair, while either outer constraint requires a third triple. Three explicit repair triples attain the bound.

**Falsifier.** A 12-edge completion of the canonical overlap.

**Verification route.** Included brute-force checker for all 12 labelings and a printed canonical repair table.

**Lean mission.** `H1_rotor_collision_min_thirteen`

**Novelty queries.**
- `13 edge H1 M2 collision theorem`
- `seven vertex rooted collision Turan 3 4`

**Dependencies.** `E500-B16`

**Flagship relation.** First exact collision penalty on the residual frontier.

---

## E500-B18 — Canonical Collision Repair Classification

**Status:** `FINITE_EXHAUSTIVE_THIS_RUN`  
**Authority:** `V2_REPLAY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `75/100`  
**Claim hash:** `b8820c9a590f538069511db2d6bf8c1b9a50e7528acdebb7097e86005ac85d2e`

**Statement.** For a canonical \(H_1/M_2\) overlap, the residual repair number is 3. Exactly three labeled minimum repair sets exist, forming two orbits under the stabilizer of the forced overlap.

**Proof route.** Enumerate subsets of the nine free triples and test the six uncovered four-sets.

**Falsifier.** A fourth minimum repair, a two-triple repair, or a different stabilizer-orbit count.

**Verification route.** Included exhaustive repair checker.

**Lean mission.** `canonicalCollision_minRepairs_three_twoOrbits`

**Novelty queries.**
- `minimum repair sets H1 M2 collision`
- `collision transversal number three hypergraph`

**Dependencies.** `E500-B17`

**Flagship relation.** Generates equality cases for Lean/novelty checking.

---

## E500-B19 — H2/H3–Rotor Four-Overlap Impossibility

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `88/100`  
**Claim hash:** `11bf2ef315f183f60e4b59e4fcc48e44cc60d4ccbef87474fc803f6cf78ea2ed`

**Statement.** No induced \(H_2\) or \(H_3\) and induced \(M_2\) can have supports intersecting in four vertices.

**Proof route.** Every four-set of H2 spans 3 or 4 edges; every four-set of H3 spans 3 or 4; every four-set of M2 spans 1 or 2. Induced restrictions on the intersection cannot agree.

**Falsifier.** A compatible four-vertex induced restriction.

**Verification route.** Direct profile checker.

**Lean mission.** `H2_H3_rotor_fourOverlap_impossible`

**Novelty queries.**
- `H2 M2 overlap impossible`
- `H3 M2 shared four vertices`

**Dependencies.** `E500-B07`

**Flagship relation.** Proves H1 is uniquely capable of the smallest ground/obstruction collision.

---

## E500-B20 — Razborov Obstruction Extension Numbers

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `92/100`  
**Claim hash:** `db7b9c17d2fc4ea100f884938422fead431bb44fb1f2c8caa9c9fb9658c4cf12`

**Statement.** For the one-point extension operator,
\[
\phi(H_1)=2,\qquad \phi(H_2)=2,\qquad \phi(H_3)=1.
\]
Thus their minimum six-vertex covering halos have 8, 10, and 10 edges.

**Proof route.** Compute minimum pair covers of the complement triples: H1 has four absent triples hit by two pairs; H2 has two absent triples with no common pair; H3 has one absent triple.

**Falsifier.** A smaller pair cover or an invalid displayed cover.

**Verification route.** Brute-force all subsets of the ten pairs.

**Lean mission.** `Razborov_obstruction_extensionNumbers`

**Novelty queries.**
- `H1 H2 H3 pair cover extension number`
- `six vertex halo Razborov configurations`

**Flagship relation.** Isolates H1 as the only locally sub-target obstruction.

---

# C — Extension, repair, and negative theorems

## E500-C01 — Exact One-Point Extension Operator

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `100/100`  
**Claim hash:** `d5a88673ffe63947cb32f9e1fd7efff7b9fc2191aa824714e39a0e2af5c99afa`

**Statement.** Let \(M\) be a four-set cover on V and \(H=\binom V3\setminus M\). Adding a new vertex x requires selecting a pair family \(F\subseteq\binom V2\). The extension \(M\cup\{xab:ab\in F\}\) is a cover iff F contains at least one pair of every triple in H. Hence the minimum extension cost is the pair-cover number \(\tau_2(H)\).

**Proof route.** Inspect each new four-set {x,a,b,c}; it is already covered by abc∈M, otherwise one of xab,xac,xbc must be selected.

**Falsifier.** A new four-set violating the pair-cover equivalence.

**Verification route.** Direct checker over all triples and pairs.

**Lean mission.** `onePointExtension_eq_pairCover`

**Novelty queries.**
- `one vertex extension hypergraph pair cover`
- `dimension descent Turan covering`

**Flagship relation.** Exact lower-dimensional operator for state fertility.

---

## E500-C02 — Triangle-Support Complement Formula

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `92/100`  
**Claim hash:** `f4967d47899d3f10782cd792ba93bbb8568fdd5b2f53c83339dc7b9a808107f9`

**Statement.** For \(G=\binom V2\setminus F\),
\[
\tau_2(H)=\binom n2-\max\{|E(G)|:K_3(G)\subseteq M\}.
\]

**Proof route.** F meets every retained triple H iff every triangle whose three pairs avoid F belongs to M.

**Falsifier.** A graph/pair-cover pair violating complementarity.

**Verification route.** Direct graph-triangle checker.

**Lean mission.** `extensionCost_eq_totalPairs_sub_maxSupportedGraph`

**Novelty queries.**
- `triangle support graph extension operator`
- `pair cover complement graph Turan`

**Dependencies.** `E500-C01`

**Flagship relation.** Connects hypergraph extension to ordinary graph extremal theory.

---

## E500-C03 — Extension Defect and Slack Drift

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `90/100`  
**Claim hash:** `011d63416907572dadd9d32f8e4f963812e0cbf8720de3b8c88c07e46d909696`

**Statement.** For an optimal n-cover M define
\[
\sigma(M)=\tau_2(\binom V3\setminus M)-(c_{n+1}-c_n)\ge0.
\]
The cheapest child has exactly \(\sigma(M)\) excess edges above \(c_{n+1}\). More generally, if M has slack s, child slack is
\[
s' = s+\tau_2(H)-(c_{n+1}-c_n).
\]

**Proof route.** Child size is |M|+extension cost; subtract the next optimum.

**Falsifier.** A child whose computed slack differs from the formula.

**Verification route.** Exact finite edge-count checker.

**Lean mission.** `extensionDefect_eq_childSlack`

**Novelty queries.**
- `extension defect optimal hypergraph state`
- `near-optimal slack drift pair cover`

**Dependencies.** `E500-C01`

**Flagship relation.** Grades fertility instead of a binary fertile/sterile label.

---

## E500-C04 — Graph-Generated Covering Classification

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `95/100`  
**Claim hash:** `43be8df220de46fbdecee11d790c7b0f414ae321c4472d06d6d4af5180dbcf62`

**Statement.** If \(M=K_3(G)\) and M covers every four-set, then \(\overline G\) is a star plus isolated vertices. Conversely every such complement gives a cover.

**Proof route.** If the complement contains two disjoint edges, their four endpoints contain no independent triple and hence G has no triangle; if it contains a triangle, adjoining any fourth vertex also blocks an independent triple. A graph with matching number≤1 and no triangle is a star plus isolates.

**Falsifier.** A non-star complement whose G-triangles cover all four-sets.

**Verification route.** Enumerate all graphs through n=7; formal graph proof is elementary.

**Lean mission.** `graphGenerated_cover_iff_complement_star`

**Novelty queries.**
- `triangles cover every four-set complement star`
- `graph generated Turan covering classification`

**Flagship relation.** A negative theorem killing exact graph generation.

---

## E500-C05 — Graph-Generated Density Boundary

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `88/100`  
**Claim hash:** `8b432d8dbc8931b747ced556cb91d7a83e9f22e1acc0ae3af0dfb3774e151018`

**Statement.** Every graph-generated four-set cover satisfies
\[
|K_3(G)|\ge\binom{n-1}{3},
\]
so its density tends to 1, not 4/9.

**Proof route.** Use E500-C04. A complement star with k leaves leaves all triples outside the center and C(n-1-k,2) center-triangles; minimum is k=n-1.

**Falsifier.** A graph-generated cover below the bound.

**Verification route.** Symbolic count plus finite graph enumeration.

**Lean mission.** `graphGenerated_cover_density_tends_one`

**Novelty queries.**
- `graph-generated covering density one`
- `triangle hypergraph cannot achieve Turan 4/9`

**Dependencies.** `E500-C04`

**Flagship relation.** Exact rejection boundary for the high-utilization route.

---

## E500-C06 — Bad-Four-Set Residual Theorem

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `90/100`  
**Claim hash:** `00196cb1257346759d52f3beb1c5fed88f14730e0d43d92ceb7262437ae38e4e`

**Statement.** If \(K_3(G)\subseteq M\) and \(R=M\setminus K_3(G)\), then R meets every four-set on which G has no triangle.

**Proof route.** Such a four-set is not covered by the supported triangles, but M covers it, so one of its triples lies in R.

**Falsifier.** A triangle-free-in-G four-set with no residual triple.

**Verification route.** Direct set-difference checker.

**Lean mission.** `residual_covers_triangleFreeFourSets`

**Novelty queries.**
- `support graph residual repair bad four-sets`
- `triangle repair decomposition Turan`

**Flagship relation.** Correct replacement for the refuted graph-generation hypothesis.

---

## E500-C07 — Bad Four-Set Graph Characterization

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `80/100`  
**Claim hash:** `87a60cb8acd5a1bd5c790fca6b93bffab5df9677898936e77804c3fe017742be`

**Statement.** A graph F on a four-set has no independent triple iff it contains a triangle or two disjoint edges.

**Proof route.** If F is triangle-free and has no matching of size2, all edges share a common vertex, leaving the other three vertices independent. The converse is immediate.

**Falsifier.** A four-vertex graph outside the two classes with independence number≤2.

**Verification route.** Enumerate all 11 unlabeled four-vertex graphs.

**Lean mission.** `fourGraph_noIndependentTriple_iff_triangle_or_2K2`

**Novelty queries.**
- `four vertex graph no independent triple K3 2K2`
- `bad four-set characterization`

**Flagship relation.** Finite graph alphabet for residual repair.

---

## E500-C08 — Disjoint-Edge Bad-Set Bound

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `84/100`  
**Claim hash:** `bb8fb1aff06ed67b68a137463d7f64f65ca606ed8878a214054ec50b71ff0ced`

**Statement.** For a graph F, let \(\mathcal B(F)\) be four-sets with no independent triple. Then
\[
|\mathcal B(F)|\ge \frac13\left[\binom{e(F)}2-\sum_v\binom{d_F(v)}2\right].
\]

**Proof route.** The bracket counts unordered disjoint edge pairs. Each such pair forces a bad four-set, and a four-set contains at most three perfect matchings.

**Falsifier.** A graph violating the disjoint-edge count or multiplicity three.

**Verification route.** Direct graph enumeration for small n.

**Lean mission.** `badFourSets_ge_disjointEdgePairs_div_three`

**Novelty queries.**
- `disjoint edges force bad four-set`
- `matching supersaturation residual covering`

**Dependencies.** `E500-C07`

**Flagship relation.** Coarse but exact residual lower bound.

---

## E500-C09 — Independent-Triple Repair Variational Principle

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `93/100`  
**Claim hash:** `2fa6de3d99a55ec07719df9245d89e0b356156b82af9cc88af711c42ce4e2e75`

**Statement.** For a graph F, let \(i_3(F)\) be its independent triples and \(\rho(F)\) the minimum number of additional triples covering all four-sets with no independent triple. Then
\[
c_n=\min_F\bigl(i_3(F)+\rho(F)\bigr).
\]

**Proof route.** For any F, independent triples plus a minimum repair form a cover. Conversely choose F=K_n, for which i3=0 and rho=c_n.

**Falsifier.** A graph functional value below c_n or failure of the K_n reverse inequality.

**Verification route.** Finite ILP comparison for n≤7.

**Lean mission.** `coverNumber_eq_min_independentTriples_add_repair`

**Novelty queries.**
- `graph variational principle Turan 3 4`
- `independent triples plus repair covering`

**Flagship relation.** Exact but degenerate reformulation; useful only with structural restrictions.

---

## E500-C10 — Fractional Repair of the Complete Graph

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `92/100`  
**Claim hash:** `81555ef2388bebf8e7a277baa8d12dec36223899ff76c215274e710ac050d68c`

**Statement.** For F=K_n, the fractional triple cover of all four-sets has value
\[
\rho^*(K_n)=\frac14\binom n3.
\]

**Proof route.** Uniform weight 1/4 is feasible. Summing all four-set constraints gives (n-3)sum_T z_T≥C(n,4), yielding the matching lower bound C(n,3)/4.

**Falsifier.** A fractional solution below the incidence lower bound.

**Verification route.** Rational LP dual checker.

**Lean mission.** `fractional_completeRepair_eq_quarter`

**Novelty queries.**
- `fractional covering all four-sets by triples 1/4`
- `LP relaxation Turan 3 4`

**Flagship relation.** Provides the exact fractional baseline.

---

## E500-C11 — Fractional-Shortcut Sterility

**Status:** `PROVED_NEGATIVE_THEOREM`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `100/100`  
**Claim hash:** `1482ff62d5d4adaaec2e395a7888d72ab592941df22f8ce42d1c8f67accca05a`

**Statement.** The universal inequality
\[
i_3(F)+\rho^*(F)\ge(4/9-o(1))\binom n3
\]
is false: \(F=K_n\) gives exactly \(\frac14\binom n3\).

**Proof route.** Apply E500-C10 and i3(K_n)=0.

**Falsifier.** The complete-graph calculation fails.

**Verification route.** Exact rational check.

**Lean mission.** `fractionalRepair_cannot_close_fourNinths`

**Novelty queries.**
- `fractional flag repair fails Turan 3 4`
- `integrality gap four-set covering`

**Dependencies.** `E500-C10`

**Flagship relation.** Kills a tempting close route and identifies integrality as load-bearing.

---

## E500-C12 — 16/9 Integrality-Gap Equivalence

**Status:** `PROVED_EQUIVALENCE`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `100/100`  
**Claim hash:** `07aa02900508c92bbc4f0d302058d55e52a78e3a38600bd203949bf4d1fe48ed`

**Statement.** For F=K_n,
\[
\frac{\rho(K_n)}{\rho^*(K_n)}=4q_n.
\]
Therefore Turán’s conjecture is equivalent to this integrality-gap ratio tending to \(16/9\).

**Proof route.** rho(K_n)=c_n by definition and E500-C10 gives rho*=C(n,3)/4.

**Falsifier.** A mismatch in the exact ratio or density equivalence.

**Verification route.** Exact c_n and rational replay.

**Lean mission.** `turanConjecture_iff_completeRepairGap_tends_16over9`

**Novelty queries.**
- `16/9 integrality gap Turan 3 4`
- `four-set triple cover LP gap`

**Dependencies.** `E500-C10`

**Flagship relation.** A sharp alternate headline for the conjecture.

---

## E500-C13 — General One-Point Dimension Descent

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `88/100`  
**Claim hash:** `047791bbe9f7d3cac951bf03cba27164820acab89d5b9333c1cee1579025ab56`

**Statement.** For an \((r,k)\)-cover M on V, adding a new vertex x reduces to selecting \((r-1)\)-sets that meet every \((k-1)\)-set S for which M contains no r-subset of S.

**Proof route.** Inspect each new k-set {x}∪S. It is covered either by an old r-edge inside S or by x joined to a selected (r-1)-set inside S.

**Falsifier.** A new k-set violating the equivalence.

**Verification route.** Generic finite-set checker and Lean specialization.

**Lean mission.** `general_onePointExtension_dimensionDescent`

**Novelty queries.**
- `covering design one point extension dimension descent`
- `r k cover extension lower uniformity`

**Flagship relation.** Transfers the extension blade across covering-design problems.

---

# D — Rooted obstruction package

## E500-D01 — Razborov Obstruction Four-Set Profiles

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `82/100`  
**Claim hash:** `c0dff514c8223781e1f3629fa66a34529ed23f223aeb097d142215528fa05b24`

**Statement.** The induced four-set edge-count profiles are
\[
H_1:4^1\,2^4,\qquad H_2:4^1\,3^4,\qquad H_3:4^3\,3^2.
\]

**Proof route.** Delete each vertex from the explicit edge sets of H1,H2,H3.

**Falsifier.** A deletion with a different edge count.

**Verification route.** Included profile checker against source-bound definitions.

**Lean mission.** `Razborov_H_profiles`

**Novelty queries.**
- `H1 H2 H3 four-set profiles`
- `Razborov forbidden configurations deletion deck`

**Flagship relation.** Explains why only H1 shares a four-root with M2.

---

## E500-D02 — Unique Shared Root of H1 and M2

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `98/100`  
**Claim hash:** `446800942b645deaa559262ba043e246c2e8ed6b45a1f27c8864ca85b58f53ab`

**Statement.** The only four-vertex induced type that can occur as a restriction of both \(H_1\) and \(M_2\) is \(B_2\), the two-edge type with a shared pair.

**Proof route.** H1 four-restrictions are K4^3 or B2; M2 restrictions have one or two edges, and its two-edge restrictions are B2.

**Falsifier.** A common restriction of another type.

**Verification route.** Direct profile and isomorphism checker.

**Lean mission.** `H1_M2_commonFourRoot_iff_B2`

**Novelty queries.**
- `shared root H1 M2 B2`
- `rooted flag Razborov M2 H1`

**Dependencies.** `E500-B07`, `E500-D01`

**Flagship relation.** Pins the residual frontier to one rooted alphabet.

---

## E500-D03 — Root Multiplicity Counts

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `86/100`  
**Claim hash:** `55ffd9ef09fa7ef74993213b1e60e784ca681ea00c43748af974e8b5e9aa9664`

**Statement.** Every induced \(H_1\) contains exactly four \(B_2\) four-subsets; every induced \(M_2\) contains exactly three.

**Proof route.** Use E500-D01 and E500-B07.

**Falsifier.** A copy with another number of B2 restrictions.

**Verification route.** Direct induced-subset count.

**Lean mission.** `H1_has_four_B2_roots_M2_has_three`

**Novelty queries.**
- `B2 root multiplicity H1 M2`
- `rooted copy count Turan obstruction`

**Dependencies.** `E500-D01`, `E500-B07`

**Flagship relation.** Normalizes rooted density chain rules.

---

## E500-D04 — Rooted Incidence Chain Rules

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `90/100`  
**Claim hash:** `7961992c069d9e09c76cb7122502a99ec700b04c34cf9933dd8fcd1dc352e706`

**Statement.** Let \(h(Q)\) count outside vertices extending an induced \(B_2\) root Q to \(H_1\), and \(m(Q)\) count outside vertex-pairs extending Q to \(M_2\). Then
\[
\sum_Q h(Q)=4N(H_1),\qquad \sum_Q m(Q)=3N(M_2),
\]
where copies and roots are counted as unlabeled vertex subsets with their induced type.

**Proof route.** Double count (H1-copy,B2-root) and (M2-copy,B2-root) incidences using E500-D03.

**Falsifier.** An induced-copy census violating the incidence equalities.

**Verification route.** Finite induced-subgraph counter.

**Lean mission.** `rooted_extension_incidence_H1_M2`

**Novelty queries.**
- `rooted extension count H1 M2 B2`
- `flag chain rule shared root`

**Dependencies.** `E500-D03`

**Flagship relation.** Exact bridge from global copy densities to one root space.

---

## E500-D05 — Collision–Segregation Covariance Inequality

**Status:** `PROVED_ANALYTIC`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `76/100`  
**Claim hash:** `6c12375c2166d3af97c2f7085bb99dddb5fc15fcc13c1f564d7dedc306955dc7`

**Statement.** For normalized nonnegative root functions h,m,
\[
\mathbb E[hm]=\mathbb Eh\,\mathbb Em+\operatorname{Cov}(h,m),
\]
and
\[
\mathbb Eh\,\mathbb Em-\mathbb E[hm]\le
\sqrt{\operatorname{Var}(h)\operatorname{Var}(m)}.
\]
Thus suppressing mixed extensions below the independent-product rate forces rooted variance.

**Proof route.** Center h and m and apply Cauchy–Schwarz.

**Falsifier.** A pair of finite functions violating covariance algebra.

**Verification route.** Rational finite-vector checker.

**Lean mission.** `collision_or_rootVariance`

**Novelty queries.**
- `collision segregation covariance rooted flags`
- `H1 M2 extension anticorrelation`

**Flagship relation.** Analytic PSD skeleton for a rooted flag certificate.

---

## E500-D06 — Published Conditional Closure Package

**Status:** `PUBLISHED_SOURCE_BOUND`  
**Authority:** `PUBLISHED`  
**Novelty:** `UNRUN`  
**Structural leverage:** `100/100`  
**Claim hash:** `9f3dd326385f0f1b1422d80ec165890bd8e87a9cea9df69490dcc1be9a7523d3`

**Statement.** Razborov proved
\[
\pi_{\min}(I_4^3,H_1,H_2,H_3)=4/9
\]
and
\[
\pi_{\min}(I_4^3,M_2)\ge0.4557.
\]

**Proof route.** External published flag-algebra/indirect-interpretation results; not reproved in this packet.

**Falsifier.** A source mismatch or failed independent verification of the cited certificates.

**Verification route.** Bind to Razborov, arXiv:1210.4605 / published version; local novelty checker should mark these as known.

**Lean mission.** `source_bound_Razborov_conditional_results`

**Novelty queries.**
- `Razborov H1 H2 H3 4/9 M2 0.4557`

**Flagship relation.** Any sub-4/9 phase must retain both M2 behavior and at least one H_i behavior.

---

## E500-D07 — H2/H3 Local Halo Surplus

**Status:** `PROVED_IN_PACKET`  
**Authority:** `COURT_READY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `87/100`  
**Claim hash:** `517a11151bd4a1fffe6616771b4adb6ae8080c9b4f20d424d0c652ea77960212`

**Statement.** Any six-vertex cover containing induced \(H_2\) or induced \(H_3\) has at least 10 edges, exceeding the six-vertex 4/9 target \(80/9\). An \(H_1\)-containing six-cover may have 8 edges.

**Proof route.** Apply the extension numbers in E500-B20 to the fixed five-edge counts 8,9,6.

**Falsifier.** A smaller halo cover.

**Verification route.** Brute pair-cover enumeration.

**Lean mission.** `H2_H3_halos_above_target_H1_below`

**Novelty queries.**
- `Razborov obstruction halo surplus`
- `H1 cheap obstruction H2 H3 expensive`

**Dependencies.** `E500-B20`

**Flagship relation.** Reduces the cheap local obstruction to H1.

---

# S — Novelty/Lean-ready theorem candidates

## E500-S01 — Human Rotor Rigidity

**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Authority:** `PROPOSAL_ONLY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `80/100`  
**Claim hash:** `336d2dd771a9f43305aabc448403fb0dffb864fcaf7ef499f3abd4b66c171d9b`

**Statement.** Every six-edge cover on six vertices admits a unique partition into three pair-codegree-2 pairs and is exactly the cyclic pair rotor.

**Proof route.** Derive 3-regularity from five-deletion minima; prove every pair has positive codegree, the three codegree-2 pairs are disjoint, then recover the directed cycle.

**Falsifier.** A six-edge cover not admitting the rotor partition.

**Verification route.** Formalize a human proof or let Lean discharge the finite statement with native_decide.

**Lean mission.** `human_rotor_rigidity`

**Novelty queries.**
- `Human Rotor Rigidity`
- `Every six-edge cover on six vertices admits a unique partition into three pair-codegree-2 pairs and is exactly the cyclic pair rotor.`

**Flagship relation.** Standalone theorem candidate or load-bearing close lemma.

---

## E500-S02 — Optimal Seven-State Deletion-Spectrum Classification

**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Authority:** `PROPOSAL_ONLY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `80/100`  
**Claim hash:** `fef88abab966e26f15bd2cbf2225bbc662fc71109dc6d6b8b3538229470f5ce7`

**Statement.** Classify every possible multiset \(\{|M-v|-6:v\in V(M)\}\) among 12-edge seven-covers and every isomorphism orbit realizing it.

**Proof route.** Enumerate all optimal orbits with canonical augmentation; use sum=6 and local rotor constraints to prune.

**Falsifier.** An optimal orbit outside the classification.

**Verification route.** SAT/ILP enumeration with isomorphism certificates; Lean checks each representative.

**Lean mission.** `classify_optimalSeven_deletionSpectra`

**Novelty queries.**
- `Optimal Seven-State Deletion-Spectrum Classification`
- `Classify every possible multiset \(\{|M-v|-6:v\in V(M)\}\) among 12-edge seven-covers and every isomorphism orbit realizing it.`

**Flagship relation.** Standalone theorem candidate or load-bearing close lemma.

---

## E500-S03 — Optimal Eight-State Deletion-Spectrum Classification

**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Authority:** `PROPOSAL_ONLY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `80/100`  
**Claim hash:** `c188939a91b73048ec48d3ac7bd0e44718bf774326ab2a1464dda3ff2ed2c606`

**Statement.** Classify every optimal eight-cover by its deletion-excess spectrum over c7; total excess is 4 and at least four deletions are optimal.

**Proof route.** Enumerate optimal orbits and combine with the debt identity.

**Falsifier.** An optimum outside the finite list.

**Verification route.** Canonical SAT enumeration.

**Lean mission.** `classify_optimalEight_deletionSpectra`

**Novelty queries.**
- `Optimal Eight-State Deletion-Spectrum Classification`
- `Classify every optimal eight-cover by its deletion-excess spectrum over c7; total excess is 4 and at least four deletions are optimal.`

**Flagship relation.** Standalone theorem candidate or load-bearing close lemma.

---

## E500-S04 — Seven-Optimum Fertility Separation

**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Authority:** `PROPOSAL_ONLY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `80/100`  
**Claim hash:** `ff3ec97c7d851d84526b278660f405ca3c8ec0241b5fbaa0ce95195693d10fd9`

**Statement.** The pair-cover extension number \(\tau_2(\binom{[7]}3\setminus M)\) separates the Turán-type and non-Turán optimal seven-vertex orbits, or else all optima share an exact reproductive phenotype.

**Proof route.** Enumerate all optimal seven-orbits, solve every pair-cover extension problem, and compare child orbits.

**Falsifier.** Two claimed-separated states with equal phenotype, or an unlisted state.

**Verification route.** Exact pair-cover ILPs and canonical child classification.

**Lean mission.** `optimalSeven_fertilityPhenotype`

**Novelty queries.**
- `Seven-Optimum Fertility Separation`
- `The pair-cover extension number \(\tau_2(\binom{[7]}3\setminus M)\) separates the Turán-type and non-Turán optimal seven-vertex orbits, or else all optima share an exact reproductive phenotype.`

**Flagship relation.** Standalone theorem candidate or load-bearing close lemma.

---

## E500-S05 — Rotor-Overlap Transition Graph

**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Authority:** `PROPOSAL_ONLY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `80/100`  
**Claim hash:** `ef1ef24c7707f8581df01814d623616eae5887689d6a22f12cdd3f64ad539fe7`

**Statement.** The graph whose nodes are labeled M2 states and whose edges are compatible five-overlaps has a determinable component structure, spectrum, and exact liftability to optimal seven-covers.

**Proof route.** Build the finite transition graph from E500-B15 and compute its invariants.

**Falsifier.** A transition or lift contradicting the computed graph.

**Verification route.** Pure finite enumeration; Lean can check adjacency.

**Lean mission.** `rotorOverlap_transitionGraph`

**Novelty queries.**
- `Rotor-Overlap Transition Graph`
- `The graph whose nodes are labeled M2 states and whose edges are compatible five-overlaps has a determinable component structure, spectrum, and exact liftability to optimal seven-covers.`

**Flagship relation.** Standalone theorem candidate or load-bearing close lemma.

---

## E500-S06 — H1–Rotor Collision Supersaturation

**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Authority:** `PROPOSAL_ONLY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `80/100`  
**Claim hash:** `cdab799c27db1de91154ffbdffbab5bd577b4689dd40faef3926556eda52ec38`

**Statement.** Find the sharp lower bound on the number of 13-edge collision seven-sets forced by prescribed induced densities of H1 and M2.

**Proof route.** Express collisions over B2 roots and solve the finite rooted flag/LP extremal problem.

**Falsifier.** A large cover with the prescribed densities and fewer collisions.

**Verification route.** Flag algebra or finite moment LP with rational certificate.

**Lean mission.** `H1_M2_collision_supersaturation`

**Novelty queries.**
- `H1–Rotor Collision Supersaturation`
- `Find the sharp lower bound on the number of 13-edge collision seven-sets forced by prescribed induced densities of H1 and M2.`

**Flagship relation.** Standalone theorem candidate or load-bearing close lemma.

---

## E500-S07 — Rooted Collision-or-Charge Lemma

**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Authority:** `PROPOSAL_ONLY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `80/100`  
**Claim hash:** `854860832a02eaeabf25cd478b96696dc431939d3dc57b3846396d5563eb7349`

**Statement.** Every overlap of B2-rooted H1- and M2-extension flags either determines coherent orientation data or has a certified positive local excitation charge.

**Proof route.** Enumerate all rooted flags through order 7 or 8 and classify their unions.

**Falsifier.** A zero-charge incompatible rooted flag.

**Verification route.** Exact flag census plus SAT completion certificates.

**Lean mission.** `B2_orient_or_charge`

**Novelty queries.**
- `Rooted Collision-or-Charge Lemma`
- `Every overlap of B2-rooted H1- and M2-extension flags either determines coherent orientation data or has a certified positive local excitation charge.`

**Flagship relation.** Standalone theorem candidate or load-bearing close lemma.

---

## E500-S08 — Zero-Cost Defect Classification

**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Authority:** `PROPOSAL_ONLY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `80/100`  
**Claim hash:** `f5e0ea455f9c14871b7166a095a77cfe1d9c6bc51b021054947077be2d518be2`

**Statement.** Classify the least B2-rooted local states that evade both direct collision charge and coherent orientation reconstruction.

**Proof route.** Use the dual support of a failed minimal rooted SDP.

**Falsifier.** A smaller or additional zero-cost defect.

**Verification route.** Order-7/8 marginal-extension LP.

**Lean mission.** `classify_zeroCost_B2_defects`

**Novelty queries.**
- `Zero-Cost Defect Classification`
- `Classify the least B2-rooted local states that evade both direct collision charge and coherent orientation reconstruction.`

**Flagship relation.** Standalone theorem candidate or load-bearing close lemma.

---

## E500-S09 — B2-Rooted 4/9 Certificate

**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Authority:** `PROPOSAL_ONLY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `80/100`  
**Claim hash:** `93d766b4244a13bdb67b571fa5bb0439ab8297e4d621bfcc9152a35c3ad68559`

**Statement.** There exists a rational flag-algebra identity rooted at B2, using H1-, M2-, and defect-extension flags, that proves covering density at least 4/9.

**Proof route.** Solve the designed SDP; rationally reconstruct PSD matrices and verify every type coefficient.

**Falsifier.** No feasible certificate at the stated order/basis.

**Verification route.** Independent flag tables, exact LDLᵀ, and local formal-kernel bridge.

**Lean mission.** `B2_rooted_fourNinths_certificate`

**Novelty queries.**
- `B2-Rooted 4/9 Certificate`
- `There exists a rational flag-algebra identity rooted at B2, using H1-, M2-, and defect-extension flags, that proves covering density at least 4/9.`

**Flagship relation.** Standalone theorem candidate or load-bearing close lemma.

---

## E500-S10 — Collision-or-Template Stability

**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Authority:** `PROPOSAL_ONLY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `80/100`  
**Claim hash:** `3f8278eb4fc232616c9a45b4f78210239d6724dd77b21e13c21819fc9257733f`

**Statement.** Positive densities of both H1 and M2 force either positive density of costly compatible B2-rooted collisions or o(n^3)-closeness to a 4/9-controlled Fon-der-Flaass/Turán phase.

**Proof route.** Prove rooted phase separation plus an orientation/partition reconstruction theorem.

**Falsifier.** A sequence with positive H1/M2 densities, negligible collisions, and no controlled template.

**Verification route.** Graphon/flag compactness followed by finite reconstruction certificates.

**Lean mission.** `collision_or_template_stability`

**Novelty queries.**
- `Collision-or-Template Stability`
- `Positive densities of both H1 and M2 force either positive density of costly compatible B2-rooted collisions or o(n^3)-closeness to a 4/9-controlled Fon-der-Flaass/Turán phase.`

**Flagship relation.** Standalone theorem candidate or load-bearing close lemma.

---

## E500-S11 — Ground–Obstruction Repulsion Constant

**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Authority:** `PROPOSAL_ONLY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `80/100`  
**Claim hash:** `bba5f5b62c82075041f0f5c6ed13ff6cbc9a950ad1759f92be6fff09cf90daf7`

**Statement.** Determine the sharp number of M2 ground extensions destroyed, on average, by one H1 extension over a shared B2-root neighborhood.

**Proof route.** Enumerate overlapping root neighborhoods and optimize the joint extension counts.

**Falsifier.** A configuration exceeding the proposed coexistence bound.

**Verification route.** Rooted finite LP or exhaustive local census.

**Lean mission.** `ground_obstruction_repulsion_constant`

**Novelty queries.**
- `Ground–Obstruction Repulsion Constant`
- `Determine the sharp number of M2 ground extensions destroyed, on average, by one H1 extension over a shared B2-root neighborhood.`

**Flagship relation.** Standalone theorem candidate or load-bearing close lemma.

---

## E500-S12 — Local Potential at Minimal Scale

**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Authority:** `PROPOSAL_ONLY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `80/100`  
**Claim hash:** `e259823d5a6ddb8f1fb7fd124fa1d27864f6c36cbb06f9db5d3ca173ba1894fd`

**Statement.** Determine the least k for which a rational telescoping potential on k-vertex covering types proves
\(\mathbb E\epsilon_5\ge13/9\).

**Proof route.** Run certificate-growth from k=6 upward, extracting the dual escape state at every failure.

**Falsifier.** A globally extendable pseudo-distribution below 13/9 at all tested scales.

**Verification route.** Exact rational LP/SDP plus k→k+1 marginal extension tests.

**Lean mission.** `least_localPotential_scale`

**Novelty queries.**
- `Local Potential at Minimal Scale`
- `Determine the least k for which a rational telescoping potential on k-vertex covering types proves`

**Flagship relation.** Standalone theorem candidate or load-bearing close lemma.

---

## E500-S13 — Equality Classification for the Deletion Recurrence

**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Authority:** `PROPOSAL_ONLY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `80/100`  
**Claim hash:** `6ffce3a24c816ac5745ebce8b29d5507ec6f6d963e0ef6d3c18c7e56e05b174c`

**Statement.** Classify all n for which
\[
c_{n+1}=\frac{n+1}{n-2}c_n
\]
and all optimal states on each plateau.

**Proof route.** Combine divisibility, regularity, full heredity, and finite extension searches.

**Falsifier.** An unclassified plateau or optimum.

**Verification route.** Exact c_n table plus orbit enumeration.

**Lean mission.** `classify_coverDensity_plateaux`

**Novelty queries.**
- `Equality Classification for the Deletion Recurrence`
- `Classify all n for which`

**Flagship relation.** Standalone theorem candidate or load-bearing close lemma.

---

## E500-S14 — First Nonhereditary Optimal State

**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Authority:** `PROPOSAL_ONLY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `80/100`  
**Claim hash:** `596702d8e60b30a84af15480420f2b9cd2fa0162c14c4bee12e72b96e73be296`

**Statement.** Find the smallest n for which an optimal n-cover has no optimal (n-1)-vertex deletion, or prove no such n up to a certified bound.

**Proof route.** Enumerate optimum state spaces and deletion graphs.

**Falsifier.** An earlier nonhereditary optimum.

**Verification route.** Canonical augmentation with deletion certificates.

**Lean mission.** `first_nonhereditary_optimal_cover`

**Novelty queries.**
- `First Nonhereditary Optimal State`
- `Find the smallest n for which an optimal n-cover has no optimal (n-1)-vertex deletion, or prove no such n up to a certified bound.`

**Flagship relation.** Standalone theorem candidate or load-bearing close lemma.

---

## E500-S15 — Codegree-Chamber Stability

**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Authority:** `PROPOSAL_ONLY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `80/100`  
**Claim hash:** `9ce2e85f18144b5b8059989bcad71fe3805c1045027f1ad439b2e1755ffb7d2d`

**Statement.** Near-minimum covers have pair-codegree vectors lying in finitely many normalized chambers, one of which contains every asymptotically fertile phase.

**Proof route.** Mine exact optima and near-optima; formulate a stability inequality from the overlap ledger.

**Falsifier.** A near-minimum sequence outside all chambers.

**Verification route.** ILP census, flag algebra, and novelty comparison.

**Lean mission.** `codegree_chamber_stability`

**Novelty queries.**
- `Codegree-Chamber Stability`
- `Near-minimum covers have pair-codegree vectors lying in finitely many normalized chambers, one of which contains every asymptotically fertile phase.`

**Flagship relation.** Standalone theorem candidate or load-bearing close lemma.

---

## E500-S16 — Repair Integrality-Gap Stability

**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Authority:** `PROPOSAL_ONLY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `80/100`  
**Claim hash:** `182847f778be3bd002b604374cc061371ce0b9ea99dfe29694cb4693cef34db4`

**Statement.** Classify graph/repair systems whose integral-to-fractional repair ratio approaches 16/9 and prove that every near-extremal cover induces one of these systems.

**Proof route.** Study LP dual supports, rounding obstructions, and local frustration states.

**Falsifier.** A near-16/9 system outside the classification.

**Verification route.** Exact LP certificates and finite obstruction enumeration.

**Lean mission.** `repair_gap_stability_16over9`

**Novelty queries.**
- `Repair Integrality-Gap Stability`
- `Classify graph/repair systems whose integral-to-fractional repair ratio approaches 16/9 and prove that every near-extremal cover induces one of these systems.`

**Flagship relation.** Standalone theorem candidate or load-bearing close lemma.

---

## E500-S17 — General Covering-State Automaton

**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Authority:** `PROPOSAL_ONLY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `80/100`  
**Claim hash:** `2b94dbcb123196ca9bc5309fc9efad3954840f3ba2c48fb5539d73957d1ce404`

**Statement.** For fixed r<k, construct the cross-order automaton of optimal and bounded-slack (r,k)-covers under one-point dimension descent, and characterize when a finite recurrent core controls the asymptotic density.

**Proof route.** Generalize deletion debt and extension descent; prove a finite-state closure theorem under explicit hypotheses.

**Falsifier.** A system satisfying the hypotheses but with a different asymptotic density.

**Verification route.** Formal abstract theorem plus finite campaign instantiations.

**Lean mission.** `general_covering_state_automaton`

**Novelty queries.**
- `General Covering-State Automaton`
- `For fixed r<k, construct the cross-order automaton of optimal and bounded-slack (r,k)-covers under one-point dimension descent, and characterize when a finite recurrent core controls the asymptotic density.`

**Flagship relation.** Standalone theorem candidate or load-bearing close lemma.

---

## E500-S18 — Exact n=14 Frontier and Orbit Geometry

**Status:** `UNPROVED_CHECKABLE_TARGET`  
**Authority:** `PROPOSAL_ONLY`  
**Novelty:** `UNRUN`  
**Structural leverage:** `80/100`  
**Claim hash:** `35beeed816dfdaafc21111d9ed3efcfd39a553bb75e782312505d2bca7c852be`

**Statement.** Determine \(c_{14}\), enumerate all optimum isomorphism classes, construct their trade/deletion/extension graphs, and identify which known construction families they inhabit.

**Proof route.** Symmetry-broken SAT/ILP with proof certificates and independent canonicalization.

**Falsifier.** A better witness or missed orbit.

**Verification route.** DRAT/LRAT or certified branch-and-bound plus separate verifier.

**Lean mission.** `exact_n14_covering_frontier`

**Novelty queries.**
- `Exact n=14 Frontier and Orbit Geometry`
- `Determine \(c_{14}\), enumerate all optimum isomorphism classes, construct their trade/deletion/extension graphs, and identify which known construction families they inhabit.`

**Flagship relation.** Standalone theorem candidate or load-bearing close lemma.

---

# Forced-close programs

## CLOSE-01 — Five-State Excitation Certificate

**Proof program.**
1. Use E500-A15 to reduce 4/9 to mean five-excitation ≥13/9.
2. Enumerate k-vertex covering types and construct a rational telescoping potential.
3. Verify every local coefficient and the global cancellation identity.
4. Conclude c_n≥(4/9-o(1))C(n,3).

**Single load-bearing gap.** Existence of a finite local potential reaching 13/9.

**Falsifier.** An extendable type distribution with mean excitation below 13/9 satisfying every admitted local identity.

**Next executable attack.** Run order-7 then order-8 rational LP/SDP; extract dual escape support.

---

## CLOSE-02 — 16/9 Integrality-Gap Close

**Proof program.**
1. Use E500-C12 to rewrite the conjecture as an LP integrality-gap limit.
2. Classify local fractional ground states and integral rounding obstructions.
3. Prove each unit of local compatibility frustration contributes enough global integral excess.
4. Sum to obtain gap ≥16/9-o(1).

**Single load-bearing gap.** A quantitative local-to-global rounding/frustration inequality.

**Falsifier.** A realizable cover sequence with integrality gap below 16/9 and no detected local obstruction.

**Next executable attack.** Compute exact primal/dual optima and obstruction profiles for n≤14.

---

## CLOSE-03 — Razborov Double-Conditional Close

**Proof program.**
1. Invoke the published H1,H2,H3-free 4/9 theorem and M2-free 0.4557 theorem.
2. Use E500-D07 to charge H2/H3 locally.
3. Reduce the cheap residual frontier to H1 versus M2 over B2.
4. Prove collisions or segregation both pay enough to reach 4/9.

**Single load-bearing gap.** Quantitative B2-rooted collision-or-template theorem.

**Falsifier.** A sub-4/9 limit object with positive H1/M2 densities, negligible charged collisions, and no controlled template.

**Next executable attack.** Designed B2-rooted flag SDP with exact marginal extension checks.

---

## CLOSE-04 — B2-Rooted Rational Certificate

**Proof program.**
1. Enumerate all admissible B2-rooted flags through order7.
2. Use H1, M2, and only dual-returned defect flags as a PSD basis.
3. Solve for a rational identity rho-4/9 = PSD + nonnegative type coefficients.
4. Independently verify multiplication tables, coefficients, and PSD factors.

**Single load-bearing gap.** Feasibility of the exact finite rational SDP.

**Falsifier.** An order-7 dual pseudo-distribution extendable to every tested higher order and below 4/9.

**Next executable attack.** Solve minimal block; if failure, test order-8 extendability and add the separating inequality.

---

## CLOSE-05 — Optimal-State Geometry Close

**Proof program.**
1. Enumerate exact and bounded-slack optimum state spaces across orders.
2. Use deletion debt and pair-cover extension to construct the viability transition system.
3. Prove every recurrent class has missing density at least4/9.
4. Exhibit a recurrent class attaining4/9.

**Single load-bearing gap.** A finite or controllable recurrent-core theorem covering every near-optimal sequence.

**Falsifier.** An asymptotically near-optimal sequence with no representation in the transition system.

**Next executable attack.** Classify fertility and child orbits of all n=7 and n=8 optima.

---

## CLOSE-06 — Exact Finite Staircase Close

**Proof program.**
1. Certify c_s for a growing sequence of s.
2. Show q_s approaches4/9 with explicit error bounds.
3. Apply E500-A02 to all larger n.
4. Combine with the lower construction.

**Single load-bearing gap.** A scalable exact-certification method whose normalized bounds converge to4/9.

**Falsifier.** Finite values or bounds plateau strictly below4/9 without a structural recursion.

**Next executable attack.** n=14 exact frontier plus recursion/stability extraction, not raw enumeration alone.

---

# Promotion order

1. Run the included verifier. Promote its elementary and finite results only after independent replay.
2. Send claim hashes individually to the novelty checker; never novelty-check only titles.
3. Formalize the generic identities first: A01, A02, A04–A08, A11–A16, A19–A20, C01, C04, C07.
4. Formalize finite results with `native_decide` or certificate bridges: B01–B03, B08, B11, B13, B16–B19.
5. Run the highest-close-leverage novelty missions first: B08, B14, B17, C04, C12, D02, S06–S12.
6. Keep all historical collisions: a known theorem can still supply a stronger formulation, proof, equality classification, or formalization contribution.

# Source boundary

- Encirclement + RSI Discovery Engine permanent blueprint (uploaded source).
- Math Encirclement Engine build-and-proof plan (uploaded source).
- Erdős #738 × #595 cross-encirclement theorem forge (uploaded source and theorem-card precedent).
- Alexander Razborov, *On Turan's (3,4)-problem with forbidden configurations*, arXiv:1210.4605, for H1/H2/H3, M2 uniqueness, and the published conditional density theorems.
