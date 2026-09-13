# Erdős #500 — exact seven-vertex H1/M2 rooted-collision suite

**Status:** exact finite classification suite inside the Turán `(3,4)` program.  
**Parent problem:** OPEN.  
**Novelty:** UNRUN in the source packet; no priority claim here.

This page promotes three high-value finite results that were previously easy to miss inside the 76/78-record theorem-forge program. It uses the source package's `H1`, `M2`, and `B2` rooted-state nomenclature; the canonical definitions and full enumerators are preserved under `program/`.

## Theorem 1 — four-overlap classification

Fix a five-vertex `H1` support and a six-vertex `M2` (rotor) support inside a seven-vertex universe, with the two supports sharing exactly four vertices.

Among the source package's

- **15 labeled `H1` states**, and
- **30 labeled `M2` states**,

there are exactly

\[
\boxed{12}
\]

induced-compatible labeled pairs.

Moreover:

- all 12 lie in **one support-preserving orbit**;
- the common four-set is necessarily the rooted type `B2`.

**Source authority:** `FINITE_EXHAUSTIVE_THIS_RUN / V2_REPLAY` (`E500-B16`).

The falsifier was explicit: any different compatible count, second orbit, or non-`B2` common root kills the theorem.

---

## Theorem 2 — minimum collision cost is 13 edges

Every seven-vertex triple-cover configuration containing an induced `H1` and induced `M2` on supports sharing four vertices has at least

\[
\boxed{13\text{ edges}},
\]

and 13 is attained.

### Proof architecture preserved by the packet

Theorem 1 reduces every compatible overlap to one canonical rooted type. That canonical overlap has:

- **10 forced edges**;
- **6 uncovered four-sets**;
- **9 free repair triples**.

The residual hitting instance has three logically independent demands:

1. the four middle constraints force a repair on the `5`-side;
2. they also force a repair on the `6`-side;
3. either outer constraint forces a third repair triple.

Thus at least three new triples are necessary, giving

\[
10+3=13.
\]

The source packet prints explicit three-triple repairs attaining the bound and brute-force checks all 12 compatible labelings.

**Source authority:** `PROVED_BY_FINITE_CENSUS_AND_HUMAN_REPAIR / COURT_READY_AFTER_FINITE_ROOT` (`E500-B17`).

---

## Theorem 3 — complete minimum-repair classification

For the canonical `H1/M2` four-overlap, the residual repair number is exactly

\[
\boxed{3}.
\]

Among subsets of the nine free repair triples, there are exactly

\[
\boxed{3}
\]

minimum three-triple repairs.

Under the stabilizer of the forced overlap, those three repairs form exactly

\[
\boxed{2\text{ orbits}}.
\]

**Source authority:** `FINITE_EXHAUSTIVE_THIS_RUN / V2_REPLAY` (`E500-B18`).

The exhaustive falsifier was: a two-triple repair, a fourth minimum repair, or a different stabilizer-orbit count.

---

## Why this matters structurally

The suite says that the smallest `H1`/rotor collision is not a diffuse family of unrelated local accidents:

1. every compatible four-overlap collapses to **one rooted orbit**;
2. that orbit carries an exact **three-edge penalty** above its 10 forced edges;
3. the equality cases themselves are completely classified by three repairs in two symmetry orbits.

This gives a finite local obstruction/equality theory suitable for later gluing, stability, and formalization arguments.

The neighboring source theorem `E500-B15` gives the contrasting positive result for two `M2` rotors sharing five vertices: one orbit and a 12-edge completion. Thus the expensive `H1/M2` four-overlap is a genuinely different local collision species.

---

## Scope boundary

Nothing here proves the Turán `(3,4)` density conjecture or a new global extremal bound. These are exact seven-vertex rooted classifications inside the program.

The original source table records Lean **missions** for these statements, but a mission name is not itself kernel authority. This page therefore preserves the finite-replay / human-repair authority actually earned by the source packet.

## Canonical source records

- `E500-B16` — H1–Rotor Four-Overlap Classification
- `E500-B17` — H1–Rotor Collision Minimum
- `E500-B18` — Canonical Collision Repair Classification

See:

- `program/original-forge-2026-08-04/ERDOS-500-THEOREM-RECORDS.jsonl`
- the recovered theorem-forge packet under `program/`
- replay receipts under `verification/`
