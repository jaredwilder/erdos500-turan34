# Fractional repair and integrality-gap blades for Turán (3,4)

**Problem status:** OPEN.  
**Source authority:** recovered theorem-forge records marked `COURT_READY`.  
**Historical novelty:** `UNRUN` in the recovered source; no priority claim is made here.

This page publishes four exact mathematical blades recovered from the Erdős #500 theorem-forge packet. They do **not** solve Turán's (3,4)-problem. Their purpose is to isolate an exact fractional baseline, kill a tempting fractional shortcut, reformulate the conjecture as an integrality-gap limit, and preserve a simple rooted covariance inequality used by the obstruction program.

## 1. Exact fractional repair of the complete graph — E500-C10

Let `rho*(K_n)` denote the fractional triple-cover value for covering all four-subsets of an `n`-vertex complete graph by triples. Then

\[
\boxed{\rho^*(K_n)=\frac14\binom n3.}
\]

**Proof.** Assign weight `1/4` to every triple. Every four-set contains four triples, so this is feasible. Conversely, sum all four-set covering constraints. Each triple occurs in exactly `n-3` four-sets, hence

\[
(n-3)\sum_T z_T\ge \binom n4.
\]

Therefore

\[
\sum_T z_T\ge \frac{\binom n4}{n-3}=\frac14\binom n3,
\]

which matches the uniform construction.

Recovered status: `PROVED_IN_PACKET`, authority `COURT_READY`.  
Claim hash: `81555ef2388bebf8e7a277baa8d12dec36223899ff76c215274e710ac050d68c`.

## 2. Fractional-shortcut sterility — E500-C11

The prospective universal inequality

\[
i_3(F)+\rho^*(F)\ge \left(\frac49-o(1)\right)\binom n3
\]

is false.

Take `F=K_n`. Then `i_3(K_n)=0`, while the previous theorem gives

\[
\rho^*(K_n)=\frac14\binom n3.
\]

Thus the left side is exactly `1/4 binom(n,3)`, not asymptotically `4/9 binom(n,3)`.

This is a **negative theorem about a proof route**: the naive LP/fractional-repair relaxation cannot by itself deliver the `4/9` target. Integrality is load-bearing.

Recovered status: `PROVED_NEGATIVE_THEOREM`, authority `COURT_READY`.  
Claim hash: `1482ff62d5d4adaaec2e395a7888d72ab592941df22f8ce42d1c8f67accca05a`.

## 3. The `16/9` integrality-gap equivalence — E500-C12

Let `rho(K_n)=c_n` be the integral triple-cover number in the recovered formulation, and define

\[
q_n=\frac{c_n}{\binom n3}.
\]

Since the exact fractional optimum is `binom(n,3)/4`,

\[
\boxed{\frac{\rho(K_n)}{\rho^*(K_n)}=4q_n.}
\]

Consequently the Turán target

\[
q_n\to \frac49
\]

is equivalent to

\[
\boxed{\frac{\rho(K_n)}{\rho^*(K_n)}\to \frac{16}{9}.}
\]

So, in this formulation, Turán's conjecture can be read exactly as an asymptotic **integrality-gap problem over the complete-graph repair instance**.

Recovered status: `PROVED_EQUIVALENCE`, authority `COURT_READY`.  
Claim hash: `07aa02900508c92bbc4f0d302058d55e52a78e3a38600bd203949bf4d1fe48ed`.

## 4. Collision–segregation covariance inequality — E500-D05

For normalized nonnegative root functions `h,m`,

\[
\mathbb E[hm]=\mathbb Eh\,\mathbb Em+\operatorname{Cov}(h,m).
\]

Centering the two functions and applying Cauchy–Schwarz gives

\[
\left|\operatorname{Cov}(h,m)\right|
\le
\sqrt{\operatorname{Var}(h)\operatorname{Var}(m)}.
\]

Hence

\[
\boxed{
\mathbb Eh\,\mathbb Em-\mathbb E[hm]
\le
\sqrt{\operatorname{Var}(h)\operatorname{Var}(m)}
}.
\]

In the rooted obstruction language, suppressing mixed extensions below their independent-product rate therefore forces rooted variance somewhere in the pair.

Recovered status: `PROVED_ANALYTIC`, authority `COURT_READY`.  
Claim hash: `6c12375c2166d3af97c2f7085bb99dddb5fc15fcc13c1f564d7dedc306955dc7`.

## Authority / scope boundary

These statements were recovered from `ERDOS-500-ENCIRCLEMENT-THEOREM-FORGE.md` and its theorem-record JSONL. The source itself labels their novelty search as `UNRUN`; this page therefore publishes the mathematics and provenance without claiming historical originality. None of these blades closes Turán (3,4), and this repository continues to mark the parent problem as **OPEN**.