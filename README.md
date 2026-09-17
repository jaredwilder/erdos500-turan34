# Erdős #500 — Turán (3,4)

**Jared Wilder**

Structural identities, finite targets, and exact reformulations for the Turán (3,4) covering problem.

Let `c_n` be the minimum number of triples meeting every four-set on `n` vertices, and define

\[
q_n=\frac{c_n}{\binom n3}.
\]

## Deletion debt and density increments

The program uses the exact deletion debt

\[
\Delta_n=(n-2)c_{n+1}-(n+1)c_n
\]

and the identity

\[
q_{n+1}-q_n=
\frac{6\Delta_n}{(n-2)(n-1)n(n+1)}.
\]

For an optimal `(n+1)`-vertex cover `M`, the same quantity is

\[
\Delta_n=\sum_v (|M-v|-c_n).
\]

Hence

\[
q_{n+1}=q_n
\iff
\text{every vertex deletion of every optimum is optimal}.
\]

On a plateau, every optimum is regular of degree `c_{n+1}-c_n`.

## Five-set excitation

For

\[
\epsilon_5(X)=|M[X]|-3,
\]

one has

\[
\frac{|M|}{\binom n3}
=
\frac3{10}+
\frac1{10}\,\mathbb E_X\epsilon_5(X).
\]

If

\[
\Lambda_s=
\min_M\sum_{X\in\binom{[s]}5}\epsilon_5(X),
\]

then

\[
\Lambda_s=
\binom{s-3}{2}c_s-3\binom s5,
\qquad
\sup_s\frac{\Lambda_s}{\binom s5}
=
\lim_{n\to\infty}(10q_n-3).
\]

This turns the asymptotic Turán problem into an exact excitation/frustration formulation.

## More results

[`A-PROVED-THEOREM-MAP.md`](A-PROVED-THEOREM-MAP.md) collects the wider identity map, including:

- one-point dimension descent;
- extension defect;
- rooted collision identities;
- finite rotor classifications;
- the `16/9` integrality-gap equivalence.

The normalized-density monotonicity input is the classical Katona–Nemetz–Simonovits averaging mechanism. Small exact covering numbers are cross-checked against the known literature.

## Verification

GitHub CI verifies recovered source hashes and record counts and replays the finite packet in a disposable environment.

Run locally:

```sh
python verification/verify_source_packet.py
python verification/replay_packet.py --receipt verification/local-replay.json
```

## Repository map

- `program/` — theorem and finite-target package
- `formal-mirrors/` — matching formal material
- `records/` — compact #500 records
- `verification/` — source and finite replay tooling

The full Turán (3,4) problem remains open; this repository isolates exact structure that any eventual solution must account for.