# Erdős #500 — S03 Optimal Eight-State Classification CLOSED

**Author:** Jared Wilder  
**Public classification release:** 2026-09-11  
**Former status:** `UNPROVED_CHECKABLE_TARGET`  
**Current status:** `EXACT_FINITE_CLASSIFICATION`

## Result

Up to isomorphism there are exactly **six** optimal 20-edge 3-uniform covers of all four-sets on eight vertices.

Their deletion-excess spectra over the seven-vertex optimum `c_7=12` are exactly

```text
(0,0,0,0,0,0,2,2),
(0,0,0,0,0,1,1,2),
(0,0,0,0,1,1,1,1).
```

The third spectrum is realized by four non-isomorphic optima.

The six automorphism-group orders are

```text
72, 4, 4, 8, 8, 4,
```

so their labeled orbit sizes are

```text
560, 10080, 10080, 5040, 5040, 10080.
```

Hence there are exactly

```text
40,880
```

labeled optimal eight-vertex covers.

## Why anchoring an optimal seven-deletion is exhaustive

Let `M` be an optimal eight-vertex cover, so `|M|=c_8=20`.

Each triple survives exactly five of the eight vertex deletions, hence

```text
sum_v |M-v| = 5|M| = 100.
```

Every deletion is a seven-vertex cover and therefore has at least `c_7=12` edges. The baseline contribution is `8*12=96`, leaving total deletion excess exactly 4.

Consequently at least four deletions are optimal seven-vertex covers.

Thus every optimal eight-cover can be relabeled so that deleting the new vertex leaves one of the four S02 parent orbits.

## Exact one-point extension counts

For a fixed optimal seven-parent `P`, adding a new vertex `x` requires a pair family `F` on the old seven vertices meeting every triple not already selected by `P`.

Since an optimal child has

```text
c_8-c_7 = 20-12 = 8
```

new edges, `F` has eight pairs. There are only

```text
C(21,8)=203490
```

candidate pair families per parent orbit.

For the four S02 parent orbits, exact enumeration gives respectively

```text
20, 9, 5, 0
```

valid optimal extensions.

Hence there are only

```text
34
```

anchored optimal children before quotienting by relabeling.

Canonicalization under all `8!` vertex permutations yields exactly six isomorphism classes.

## Independent double-count check

Let the four S02 labeled orbit sizes be

```text
210, 1260, 1260, 840.
```

Counting `(labeled optimal 8-cover, optimal 7-deletion)` pairs from the parent-extension side gives

```text
8 * (210*20 + 1260*9 + 1260*5 + 840*0)
= 174720.
```

Counting the same pairs from the six S03 child orbits by multiplying each labeled orbit size by the number of zeros in its deletion-excess spectrum also gives

```text
174720.
```

The counts agree exactly.

## Reproducibility

`verify_s03_optimal_eight.py` performs the full classification in pure Python:

1. checks the four S02 parent representatives;
2. enumerates all `C(21,8)` eight-pair one-point extensions of each parent;
3. retains the 34 optimal children;
4. computes deletion-excess spectra;
5. canonicalizes under all `8!` relabelings;
6. computes automorphism orders and labeled orbit sizes;
7. verifies the 174720 double count;
8. additionally computes the minimum extension cost of every S02 parent orbit.

No external MILP/SAT solver is required.
