# Erdős #500 — Deletion, Density and Inheritance Toolkit

**Author:** Jared Wilder  
**Public release:** 2026-09-10

This is the scope-preserving extraction of the 76-record theorem-forge packet. Internal status labels are preserved; `UNPROVED_CHECKABLE_TARGET` means exactly that. Nothing in this file is promoted to a solution of Erdős #500 merely because it appears in the packet.

## `E500-A01` — Complement Covering Duality

**Status:** `PROVED_IN_PACKET`

Let \(c_n\) be the minimum size of a family \(M\subseteq\binom{[n]}3\) meeting every four-set in a contained triple. Then
\[
\operatorname{ex}_3(n,K_4^{(3)})=\binom n3-c_n.
\]

## `E500-A02` — Finite-to-Global Density Transfer

**Status:** `PROVED_IN_PACKET`

If \(M\) covers every four-set on \(n\) vertices and \(4\le s\le n\), then
\[
\frac{|M|}{\binom n3}\ge \frac{c_s}{\binom s3}.
\]

## `E500-A03` — Monotonicity of Normalized Covering Numbers

**Status:** `PROVED_IN_PACKET`

The sequence \(q_n=c_n/\binom n3\) is nondecreasing for \(n\ge4\).

## `E500-A04` — Deletion-Excess Identity

**Status:** `PROVED_IN_PACKET`

For an \((n+1)\)-vertex four-set cover \(M\), define
\(\delta_M(v)=|M-v|-c_n\ge0\). Then
\[
\sum_v\delta_M(v)=(n-2)|M|-(n+1)c_n.
\]
For optimal \(M\), the right side is the state-independent inheritance debt \(\Delta_n\).

## `E500-A05` — Density-Increment Identity

**Status:** `PROVED_IN_PACKET`

With \(\Delta_n=(n-2)c_{n+1}-(n+1)c_n\),
\[
q_{n+1}-q_n=
\frac{6\Delta_n}{(n-2)(n-1)n(n+1)}.
\]

## `E500-A06` — Plateau–Full-Heredity Equivalence

**Status:** `PROVED_IN_PACKET`

For \(n\ge4\), \(q_{n+1}=q_n\) iff every vertex deletion of every optimal \((n+1)\)-vertex cover is an optimal n-vertex cover.

## `E500-A07` — Plateau Regularity

**Status:** `PROVED_IN_PACKET`

If \(q_{n+1}=q_n\), every optimal \((n+1)\)-vertex cover is regular of degree \(c_{n+1}-c_n\).

## `E500-A08` — Optimal-Deletion Count Bound

**Status:** `PROVED_IN_PACKET`

For optimal \(M\) on \(n+1\) vertices, if \(z(M)\) is the number of optimal n-vertex deletions, then
\[
z(M)\ge n+1-\Delta_n.
\]

## `E500-A09` — Cumulative Inheritance-Debt Expansion

**Status:** `PROVED_IN_PACKET`

For \(N>n_0\),
\[
q_N=q_{n_0}+\sum_{n=n_0}^{N-1}
\frac{6\Delta_n}{(n-2)(n-1)n(n+1)}.
\]

## `E500-A10` — Deletion-Averaging Recurrence

**Status:** `PROVED_IN_PACKET`

For \(n\ge4\),
\[
c_{n+1}\ge \left\lceil\frac{n+1}{n-2}\,c_n\right\rceil.
\]

## `E500-A11` — Four-Set Coverage-Waste Identity

**Status:** `PROVED_IN_PACKET`

For a cover \(M\), let \(r(S)=|M\cap\binom S3|\), \(a_j=|\{S:r(S)=j\}|\), and
\[
W(M)=(n-3)|M|-\binom n4.
\]
Then
\[
W(M)=a_2+2a_3+3a_4.
\]

## `E500-A12` — Pair-Overlap Ledger

**Status:** `PROVED_IN_PACKET`

Let \(d_M(xy)\) be pair codegree. Then
\[
W(M)=\sum_{xy}\binom{d_M(xy)}2-a_3-3a_4.
\]

## `E500-A13` — Five-Set Minimum

**Status:** `PROVED_IN_PACKET`

Every five vertices in a four-set cover span at least three selected triples, and three is attainable.

## `E500-A14` — Five-State Ground Classification

**Status:** `PROVED_IN_PACKET`

For a five-set \(X\), map each selected triple \(T\subset X\) to its complementary pair \(X\setminus T\). A three-triple family covers all four-faces iff the resulting three-edge graph is \(P_3\sqcup K_2\). Thus the minimum five-state is unique up to isomorphism.

## `E500-A15` — Five-Set Excitation Identity

**Status:** `PROVED_IN_PACKET`

Define \(\epsilon_5(X)=|M[X]|-3\). Then
\[
\binom{n-3}{2}|M|=3\binom n5+\sum_{X\in\binom V5}\epsilon_5(X),
\]
and therefore
\[
\frac{|M|}{\binom n3}=\frac3{10}+\frac1{10}\mathbb E_X\epsilon_5(X).
\]

## `E500-A16` — Local Waste–Excitation Identity

**Status:** `PROVED_IN_PACKET`

For every five-set \(X\),
\[
\sum_{\substack{S\subset X\\|S|=4}}(r(S)-1)=1+2\epsilon_5(X).
\]

## `E500-A17` — Frustration Hierarchy Formula

**Status:** `PROVED_IN_PACKET`

Let
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

## `E500-A18` — Centered Integral Form

**Status:** `PROVED_IN_PACKET`

For indicator variables \(x_T\in\{0,1\}\), put \(z_T=4x_T-1\in\{-1,3\}\). The covering constraints become
\[
\sum_{T\in\binom S3}z_T\ge0\quad\forall S\in\binom V4,
\]
and the conjectured bound is equivalent to
\[
\sum_Tz_T\ge\left(\frac79-o(1)\right)\binom n3.
\]

## `E500-A19` — General Local-Density Transfer for Covering Designs

**Status:** `PROVED_IN_PACKET`

For \(r<k\), let \(c_n^{r,k}\) be the minimum number of r-sets meeting every k-set. Every n-vertex \((r,k)\)-cover M and every \(k\le s\le n\) satisfy
\[
\frac{|M|}{\binom nr}\ge\frac{c_s^{r,k}}{\binom sr}.
\]

## `E500-A20` — General Deletion Debt and Plateau Rigidity

**Status:** `PROVED_IN_PACKET`

For an optimal \((r,k)\)-cover \(M\) on \(n+1\) vertices,
\[
\sum_v(|M-v|-c_n^{r,k})=(n+1-r)c_{n+1}^{r,k}-(n+1)c_n^{r,k}.
\]
A normalized-density plateau holds iff every deletion is optimal; on a plateau every optimum is regular of degree \(c_{n+1}^{r,k}-c_n^{r,k}\).

## `E500-B01` — Exact Small Values c4,c5,c6

**Status:** `FINITE_EXHAUSTIVE_THIS_RUN`

\[
c_4=1,\qquad c_5=3,\qquad c_6=6.
\]

## `E500-B02` — Unique Five-Vertex Optimum Orbit

**Status:** `FINITE_EXHAUSTIVE_THIS_RUN`

There are exactly 30 labeled three-edge covers on five vertices, forming one isomorphism orbit with representative
\[
\{012,013,234\}.
\]

## `E500-B03` — Unique Six-Vertex Rotor Orbit

**Status:** `FINITE_EXHAUSTIVE_THIS_RUN`

There are exactly 30 labeled six-edge covers on six vertices, forming one isomorphism orbit represented by
\[
M_2=\{012,013,045,145,234,235\}.
\]

## `E500-B04` — Rotor Pair Construction

**Status:** `PROVED_IN_PACKET`

Partition six vertices into pairs \(A,B,C\), orient them cyclically \(A\to B\to C\to A\), and take all triples consisting of one full pair plus one vertex from its successor pair. The resulting six triples cover every four-set.

## `E500-B05` — Rotor Automorphism Group

**Status:** `FINITE_EXHAUSTIVE_THIS_RUN`

The automorphism group of \(M_2\) has order 24 and is isomorphic to
\[
(C_2)^3\rtimes C_3,
\]
where the three involutions swap vertices inside the rotor pairs and \(C_3\) cyclically permutes the pairs.

## `E500-B06` — Rotor Degree and Pair-Codegree Profile

**Status:** `PROVED_IN_PACKET`

In \(M_2\), every vertex has degree 3. Exactly three disjoint pairs have codegree 2, and the other twelve pairs have codegree 1. The codegree-2 pairs form the rotor perfect matching.

## `E500-B07` — Rotor Four-Set and Deletion Profiles

**Status:** `PROVED_IN_PACKET`

Every five-vertex deletion of \(M_2\) has exactly three edges. Among its fifteen four-sets, twelve span one edge and three span two; the three two-edge four-sets are precisely unions of two rotor pairs and are copies of \(B_2\).

## `E500-B08` — Exact Seven-Vertex Covering Number

**Status:** `PROVED_FROM_FINITE_BASE_AND_WITNESS`

The minimum seven-vertex covering number is
\[
c_7=12.
\]

## `E500-B09` — Every Optimal Seven-State Contains a Rotor Deletion

**Status:** `PROVED_IN_PACKET`

Every 12-edge seven-vertex cover has at least one vertex whose deletion is \(M_2\).

## `E500-B10` — Sharp Seven-State Deletion Spectrum Witness

**Status:** `COMPUTATIONAL_WITNESS_THIS_RUN`

There exists an optimal seven-vertex cover with deletion-excess spectrum
\[
\{0,1,1,1,1,1,1\}
\]
over the six-vertex optimum.

## `E500-B12` — Optimal Eight-States Have Four Optimal Deletions

**Status:** `PROVED_SHARP_BOUND`

Every optimal eight-vertex cover has at least four optimal seven-vertex deletions. Moreover an explicit optimum in the packet has exactly four.

## `E500-B14` — Nine-Vertex Full Heredity and Regularity

**Status:** `PROVED_IN_PACKET`

Every optimal nine-vertex cover is 10-regular, and every one of its nine vertex deletions is an optimal eight-vertex cover.

## `E500-B15` — Two-Rotor Five-Overlap Gluing

**Status:** `FINITE_EXHAUSTIVE_THIS_RUN`

Fix two six-vertex supports in a seven-vertex universe sharing five vertices. There are 30 compatible labeled induced \(M_2\)-pairs, one orbit under support-preserving isomorphisms, and every pair extends to a 12-edge seven-cover.

## `E500-B16` — H1–Rotor Four-Overlap Classification

**Status:** `FINITE_EXHAUSTIVE_THIS_RUN`

Fix a five-set and six-set sharing four vertices in a seven-vertex universe. Among 15 labeled \(H_1\) states and 30 labeled \(M_2\) states, exactly 12 induced-compatible pairs exist. They form one support-preserving orbit, and the shared four-set is necessarily \(B_2\).

## `E500-B17` — H1–Rotor Collision Minimum

**Status:** `PROVED_BY_FINITE_CENSUS_AND_HUMAN_REPAIR`

Every seven-vertex cover containing induced \(H_1\) and induced \(M_2\) on supports sharing four vertices has at least 13 edges; 13 is attainable.

## `E500-B18` — Canonical Collision Repair Classification

**Status:** `FINITE_EXHAUSTIVE_THIS_RUN`

For a canonical \(H_1/M_2\) overlap, the residual repair number is 3. Exactly three labeled minimum repair sets exist, forming two orbits under the stabilizer of the forced overlap.

## `E500-B19` — H2/H3–Rotor Four-Overlap Impossibility

**Status:** `PROVED_IN_PACKET`

No induced \(H_2\) or \(H_3\) and induced \(M_2\) can have supports intersecting in four vertices.

## `E500-B20` — Razborov Obstruction Extension Numbers

**Status:** `PROVED_IN_PACKET`

For the one-point extension operator,
\[
\phi(H_1)=2,\qquad \phi(H_2)=2,\qquad \phi(H_3)=1.
\]
Thus their minimum six-vertex covering halos have 8, 10, and 10 edges.

## `E500-C01` — Exact One-Point Extension Operator

**Status:** `PROVED_IN_PACKET`

Let \(M\) be a four-set cover on V and \(H=\binom V3\setminus M\). Adding a new vertex x requires selecting a pair family \(F\subseteq\binom V2\). The extension \(M\cup\{xab:ab\in F\}\) is a cover iff F contains at least one pair of every triple in H. Hence the minimum extension cost is the pair-cover number \(\tau_2(H)\).

## `E500-C02` — Triangle-Support Complement Formula

**Status:** `PROVED_IN_PACKET`

For \(G=\binom V2\setminus F\),
\[
\tau_2(H)=\binom n2-\max\{|E(G)|:K_3(G)\subseteq M\}.
\]

## `E500-C03` — Extension Defect and Slack Drift

**Status:** `PROVED_IN_PACKET`

For an optimal n-cover M define
\[
\sigma(M)=\tau_2(\binom V3\setminus M)-(c_{n+1}-c_n)\ge0.
\]
The cheapest child has exactly \(\sigma(M)\) excess edges above \(c_{n+1}\). More generally, if M has slack s, child slack is
\[
s' = s+\tau_2(H)-(c_{n+1}-c_n).
\]

## `E500-C04` — Graph-Generated Covering Classification

**Status:** `PROVED_IN_PACKET`

If \(M=K_3(G)\) and M covers every four-set, then \(\overline G\) is a star plus isolated vertices. Conversely every such complement gives a cover.

## `E500-C05` — Graph-Generated Density Boundary

**Status:** `PROVED_IN_PACKET`

Every graph-generated four-set cover satisfies
\[
|K_3(G)|\ge\binom{n-1}{3},
\]
so its density tends to 1, not 4/9.

## `E500-C06` — Bad-Four-Set Residual Theorem

**Status:** `PROVED_IN_PACKET`

If \(K_3(G)\subseteq M\) and \(R=M\setminus K_3(G)\), then R meets every four-set on which G has no triangle.

## `E500-C07` — Bad Four-Set Graph Characterization

**Status:** `PROVED_IN_PACKET`

A graph F on a four-set has no independent triple iff it contains a triangle or two disjoint edges.

## `E500-C08` — Disjoint-Edge Bad-Set Bound

**Status:** `PROVED_IN_PACKET`

For a graph F, let \(\mathcal B(F)\) be four-sets with no independent triple. Then
\[
|\mathcal B(F)|\ge \frac13\left[\binom{e(F)}2-\sum_v\binom{d_F(v)}2\right].
\]

## `E500-C09` — Independent-Triple Repair Variational Principle

**Status:** `PROVED_IN_PACKET`

For a graph F, let \(i_3(F)\) be its independent triples and \(\rho(F)\) the minimum number of additional triples covering all four-sets with no independent triple. Then
\[
c_n=\min_F\bigl(i_3(F)+\rho(F)\bigr).
\]

## `E500-C10` — Fractional Repair of the Complete Graph

**Status:** `PROVED_IN_PACKET`

For F=K_n, the fractional triple cover of all four-sets has value
\[
\rho^*(K_n)=\frac14\binom n3.
\]

## `E500-C11` — Fractional-Shortcut Sterility

**Status:** `PROVED_NEGATIVE_THEOREM`

The universal inequality
\[
i_3(F)+\rho^*(F)\ge(4/9-o(1))\binom n3
\]
is false: \(F=K_n\) gives exactly \(\frac14\binom n3\).

## `E500-C12` — 16/9 Integrality-Gap Equivalence

**Status:** `PROVED_EQUIVALENCE`

For F=K_n,
\[
\frac{\rho(K_n)}{\rho^*(K_n)}=4q_n.
\]
Therefore Turán’s conjecture is equivalent to this integrality-gap ratio tending to \(16/9\).

## `E500-C13` — General One-Point Dimension Descent

**Status:** `PROVED_IN_PACKET`

For an \((r,k)\)-cover M on V, adding a new vertex x reduces to selecting \((r-1)\)-sets that meet every \((k-1)\)-set S for which M contains no r-subset of S.

## `E500-D01` — Razborov Obstruction Four-Set Profiles

**Status:** `PROVED_IN_PACKET`

The induced four-set edge-count profiles are
\[
H_1:4^1\,2^4,\qquad H_2:4^1\,3^4,\qquad H_3:4^3\,3^2.
\]

## `E500-D02` — Unique Shared Root of H1 and M2

**Status:** `PROVED_IN_PACKET`

The only four-vertex induced type that can occur as a restriction of both \(H_1\) and \(M_2\) is \(B_2\), the two-edge type with a shared pair.

## `E500-D03` — Root Multiplicity Counts

**Status:** `PROVED_IN_PACKET`

Every induced \(H_1\) contains exactly four \(B_2\) four-subsets; every induced \(M_2\) contains exactly three.

## `E500-D04` — Rooted Incidence Chain Rules

**Status:** `PROVED_IN_PACKET`

Let \(h(Q)\) count outside vertices extending an induced \(B_2\) root Q to \(H_1\), and \(m(Q)\) count outside vertex-pairs extending Q to \(M_2\). Then
\[
\sum_Q h(Q)=4N(H_1),\qquad \sum_Q m(Q)=3N(M_2),
\]
where copies and roots are counted as unlabeled vertex subsets with their induced type.

## `E500-D05` — Collision–Segregation Covariance Inequality

**Status:** `PROVED_ANALYTIC`

For normalized nonnegative root functions h,m,
\[
\mathbb E[hm]=\mathbb Eh\,\mathbb Em+\operatorname{Cov}(h,m),
\]
and
\[
\mathbb Eh\,\mathbb Em-\mathbb E[hm]\le
\sqrt{\operatorname{Var}(h)\operatorname{Var}(m)}.
\]
Thus suppressing mixed extensions below the independent-product rate forces rooted variance.

## `E500-D06` — Published Conditional Closure Package

**Status:** `PUBLISHED_SOURCE_BOUND`

Razborov proved
\[
\pi_{\min}(I_4^3,H_1,H_2,H_3)=4/9
\]
and
\[
\pi_{\min}(I_4^3,M_2)\ge0.4557.
\]

## `E500-D07` — H2/H3 Local Halo Surplus

**Status:** `PROVED_IN_PACKET`

Any six-vertex cover containing induced \(H_2\) or induced \(H_3\) has at least 10 edges, exceeding the six-vertex 4/9 target \(80/9\). An \(H_1\)-containing six-cover may have 8 edges.

# Open checkable targets retained from the packet

The following entries are not theorems. They are kept public so the exact proof debt survives rather than being rediscovered.

## `E500-S01` — Human Rotor Rigidity

**Status:** `UNPROVED_CHECKABLE_TARGET`

Every six-edge cover on six vertices admits a unique partition into three pair-codegree-2 pairs and is exactly the cyclic pair rotor.

## `E500-S02` — Optimal Seven-State Deletion-Spectrum Classification

**Status:** `UNPROVED_CHECKABLE_TARGET`

Classify every possible multiset \(\{|M-v|-6:v\in V(M)\}\) among 12-edge seven-covers and every isomorphism orbit realizing it.

## `E500-S03` — Optimal Eight-State Deletion-Spectrum Classification

**Status:** `UNPROVED_CHECKABLE_TARGET`

Classify every optimal eight-cover by its deletion-excess spectrum over c7; total excess is 4 and at least four deletions are optimal.

## `E500-S04` — Seven-Optimum Fertility Separation

**Status:** `UNPROVED_CHECKABLE_TARGET`

The pair-cover extension number \(\tau_2(\binom{[7]}3\setminus M)\) separates the Turán-type and non-Turán optimal seven-vertex orbits, or else all optima share an exact reproductive phenotype.

## `E500-S05` — Rotor-Overlap Transition Graph

**Status:** `UNPROVED_CHECKABLE_TARGET`

The graph whose nodes are labeled M2 states and whose edges are compatible five-overlaps has a determinable component structure, spectrum, and exact liftability to optimal seven-covers.

## `E500-S06` — H1–Rotor Collision Supersaturation

**Status:** `UNPROVED_CHECKABLE_TARGET`

Find the sharp lower bound on the number of 13-edge collision seven-sets forced by prescribed induced densities of H1 and M2.

## `E500-S07` — Rooted Collision-or-Charge Lemma

**Status:** `UNPROVED_CHECKABLE_TARGET`

Every overlap of B2-rooted H1- and M2-extension flags either determines coherent orientation data or has a certified positive local excitation charge.

## `E500-S08` — Zero-Cost Defect Classification

**Status:** `UNPROVED_CHECKABLE_TARGET`

Classify the least B2-rooted local states that evade both direct collision charge and coherent orientation reconstruction.

## `E500-S09` — B2-Rooted 4/9 Certificate

**Status:** `UNPROVED_CHECKABLE_TARGET`

There exists a rational flag-algebra identity rooted at B2, using H1-, M2-, and defect-extension flags, that proves covering density at least 4/9.

## `E500-S10` — Collision-or-Template Stability

**Status:** `UNPROVED_CHECKABLE_TARGET`

Positive densities of both H1 and M2 force either positive density of costly compatible B2-rooted collisions or o(n^3)-closeness to a 4/9-controlled Fon-der-Flaass/Turán phase.

## `E500-S11` — Ground–Obstruction Repulsion Constant

**Status:** `UNPROVED_CHECKABLE_TARGET`

Determine the sharp number of M2 ground extensions destroyed, on average, by one H1 extension over a shared B2-root neighborhood.

## `E500-S12` — Local Potential at Minimal Scale

**Status:** `UNPROVED_CHECKABLE_TARGET`

Determine the least k for which a rational telescoping potential on k-vertex covering types proves
\(\mathbb E\epsilon_5\ge13/9\).

## `E500-S13` — Equality Classification for the Deletion Recurrence

**Status:** `UNPROVED_CHECKABLE_TARGET`

Classify all n for which
\[
c_{n+1}=\frac{n+1}{n-2}c_n
\]
and all optimal states on each plateau.

## `E500-S14` — First Nonhereditary Optimal State

**Status:** `UNPROVED_CHECKABLE_TARGET`

Find the smallest n for which an optimal n-cover has no optimal (n-1)-vertex deletion, or prove no such n up to a certified bound.

## `E500-S15` — Codegree-Chamber Stability

**Status:** `UNPROVED_CHECKABLE_TARGET`

Near-minimum covers have pair-codegree vectors lying in finitely many normalized chambers, one of which contains every asymptotically fertile phase.

## `E500-S16` — Repair Integrality-Gap Stability

**Status:** `UNPROVED_CHECKABLE_TARGET`

Classify graph/repair systems whose integral-to-fractional repair ratio approaches 16/9 and prove that every near-extremal cover induces one of these systems.

## `E500-S17` — General Covering-State Automaton

**Status:** `UNPROVED_CHECKABLE_TARGET`

For fixed r<k, construct the cross-order automaton of optimal and bounded-slack (r,k)-covers under one-point dimension descent, and characterize when a finite recurrent core controls the asymptotic density.

## `E500-S18` — Exact n=14 Frontier and Orbit Geometry

**Status:** `UNPROVED_CHECKABLE_TARGET`

Determine \(c_{14}\), enumerate all optimum isomorphism classes, construct their trade/deletion/extension graphs, and identify which known construction families they inhabit.

# Claim boundary

This packet is a toolkit and finite-structure program around the covering formulation of Erdős #500 / Turán (3,4). It is **not a proof of the asymptotic conjecture**. Finite census claims retain their finite authority; source-dependent statements retain their source dependence; the S-series remains explicitly unproved.
