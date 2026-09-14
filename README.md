# Erdős #500 — Turán (3,4)

**Author:** Jared Wilder  
**Status:** theorem / finite-target / density-structure research program; the Turán (3,4) problem is **not claimed solved**.

This repository is the canonical public home for the estate's #500 work. The reconstructed program contains **76 records** spanning proved-in-packet results, exact finite targets, structural identities, equivalences, analytic reductions, witnesses/classifications, and negative theorems.

## Main theorem package

Let `c_n` be the minimum number of triples meeting every four-set on `n` vertices, and put

\[
q_n=\frac{c_n}{\binom n3}.
\]

The standard Katona–Nemetz–Simonovits averaging mechanism gives the normalized-density monotonicity underlying this program; **no novelty claim is made for that classical averaging fact**.

The packet then records the exact deletion debt

\[
\Delta_n=(n-2)c_{n+1}-(n+1)c_n
\]

and the density-increment identity

\[
q_{n+1}-q_n=
\frac{6\Delta_n}{(n-2)(n-1)n(n+1)}.
\]

For an optimal `(n+1)`-vertex cover `M`, the same quantity is the total nonnegative deletion excess:

\[
\Delta_n=\sum_v (|M-v|-c_n).
\]

Consequently a density plateau has an exact structural meaning:

\[
q_{n+1}=q_n
\iff
\text{every vertex deletion of every optimum is optimal}.
\]

On such a plateau every optimum is regular, of degree `c_{n+1}-c_n`.

A second exact coordinate is the five-set excitation. For

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

Thus the Turán (3,4) conjecture is equivalently the assertion that this excitation/frustration supremum is `13/9`. This is an **equivalent reformulation / structural program**, not a solution.

The full theorem identity map, including one-point dimension descent, extension defect, rooted collision identities, finite rotor classifications and the `16/9` integrality-gap equivalence, is in [`A-PROVED-THEOREM-MAP.md`](A-PROVED-THEOREM-MAP.md).

## Prior-art boundary

The small exact covering numbers and class counts are not claimed as new. The repository's literature reconciliation records the Applegate–Rains–Sloane (2003) enumeration for the relevant small orders. The normalized-density averaging/monotonicity mechanism is classical Katona–Nemetz–Simonovits. Independent reconstruction, deletion spectra, transition machinery, exact identities and verifiers are retained because they are auditable research assets; historical novelty of the stronger refinements requires its own targeted literature court.

## Verification

GitHub CI now performs two fresh checks on every push:

1. verifies recovered source bytes, SHA-256 values, record counts and original manifest entries;
2. reruns the dependency-free finite packet in a disposable copy with site packages disabled.

The CI scope is finite/source verification only. It does **not** certify the global conjecture, historical novelty, or every theorem identity independently.

## Source layout

Exact public source bytes are migrated under:

- `program/` — main #500 theorem/finite-target package;
- `formal-mirrors/` — matching `erdos500-*` material from `erdos-theorems`;
- `records/` — compact #500 material already routed through `combinatorial-records`.

No bounded computation is promoted into a global Turán theorem, and historical novelty remains a separate literature question.

## Recovered original source packet — 2026-09-13

This original 78-record source variant complements the existing 76-record reconstructed program. The variants remain separate. Eighteen records are explicitly unproved targets. The standard-library finite checks passed on 2026-09-13; the optional SciPy MILP check was not run. This does not solve the Turán (3,4) problem or establish novelty.

- [Original record table](program/original-forge-2026-08-04/ERDOS-500-THEOREM-RECORDS.jsonl)
- [Source packet](program/original-forge-2026-08-04/)
- [Source hashes and observed status counts](verification/source-packet.json)

Run `python verification/verify_source_packet.py` to verify all recovered source bytes, original JSON manifests when present, and record counts.

### Finite replay

Run `python verification/replay_packet.py --receipt verification/local-replay.json`. The runner uses a temporary copy and preserves the original packet and historical receipts. See the [2026-09-13 replay receipt](verification/replay-2026-09-13.json).
