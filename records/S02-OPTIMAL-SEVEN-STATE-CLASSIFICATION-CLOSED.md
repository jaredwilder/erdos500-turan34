# Erdős #500 — S02 Optimal Seven-State Classification CLOSED

**Author:** Jared Wilder  
**Public classification release:** 2026-09-11  
**Former status:** `UNPROVED_CHECKABLE_TARGET`  
**Current status:** `EXACT_FINITE_CLASSIFICATION`

## Result

Up to isomorphism there are exactly **four** optimal 12-edge 3-uniform covers of all four-sets on seven vertices.

Their deletion-excess spectra over the six-vertex optimum `c_6=6` are exactly

```text
(0,0,0,1,1,2,2),
(0,0,1,1,1,1,2),
(0,1,1,1,1,1,1),
```

with the last spectrum realized by **two non-isomorphic** optima.

The four automorphism-group orders are

```text
24, 4, 4, 6,
```

so their labeled orbit sizes under `S_7` are

```text
210, 1260, 1260, 840.
```

Hence the total number of labeled optimal seven-vertex covers is

```text
3570.
```

## Why the classification is exhaustive

Let `M` be any optimal seven-vertex cover, so `|M|=c_7=12`.

Every vertex deletion `M-v` is a six-vertex cover and therefore has at least `c_6=6` edges. On the other hand, each triple survives exactly four of the seven vertex deletions, so

```text
sum_v |M-v| = 4|M| = 48.
```

If all seven deletions had at least seven edges, this sum would be at least 49. Therefore some vertex deletion has exactly six edges and is optimal on six vertices.

By the human rotor-rigidity theorem (`S01-HUMAN-ROTOR-RIGIDITY-CLOSED.md`), every six-edge optimum is the rotor `M2` up to relabeling. Thus every optimal seven-cover can be relabeled so that deleting vertex 6 leaves

```text
M2 = {012,013,045,145,234,235}.
```

## Exact extension reduction

Let

```text
H = C([6],3) \ M2.
```

There are 14 residual triples. Any edge of the seven-cover containing the new vertex 6 has the form

```text
6ab
```

for a pair `ab` among the old six vertices.

The one-point extension criterion says that the pair family `F` must meet every residual triple in `H`. Since the final cover has 12 edges and `M2` already has six, `F` has exactly six pairs.

There are only

```text
C(15,6)=5005
```

six-pair families to test. Exact enumeration finds precisely

```text
25
```

anchored pair families satisfying the extension condition.

Quotienting the resulting 25 anchored covers by all `7!` vertex permutations yields exactly four isomorphism classes.

## Orbit data

One canonical representative for each class is listed below.

### Orbit 1

Deletion-excess spectrum:

```text
(0,0,0,1,1,2,2)
```

Automorphism order: `24`  
Labeled orbit size: `210`

```text
012 013 014 023 024 056
123 124 156 256 345 346
```

### Orbit 2

Deletion-excess spectrum:

```text
(0,0,1,1,1,1,2)
```

Automorphism order: `4`  
Labeled orbit size: `1260`

```text
012 013 014 023 045 056
123 145 156 235 246 346
```

### Orbit 3

Deletion-excess spectrum:

```text
(0,1,1,1,1,1,1)
```

Automorphism order: `4`  
Labeled orbit size: `1260`

```text
012 013 014 023 056 123
156 245 246 256 345 346
```

### Orbit 4

Deletion-excess spectrum:

```text
(0,1,1,1,1,1,1)
```

Automorphism order: `6`  
Labeled orbit size: `840`

```text
012 013 023 045 046 056
124 135 146 236 256 345
```

## Independent double-count check

The spectrum zeros count rotor deletions. Counting `(labeled optimum, rotor deletion)` pairs from the orbit classification gives

```text
210*3 + 1260*2 + 1260*1 + 840*1 = 5250.
```

Counting from the anchored construction gives

```text
7 choices of deleted vertex
* 30 labeled six-vertex rotors
* 25 valid anchored extensions
= 5250.
```

The two counts agree exactly.

## Reproducibility

`verify_s02_optimal_seven.py` performs the entire classification in pure Python:

1. enumerates all 5005 six-pair extensions of a fixed rotor;
2. retains the 25 valid extensions;
3. checks every resulting 12-edge family covers all 35 four-sets;
4. computes deletion-excess spectra;
5. canonicalizes under all `7!` relabelings;
6. computes automorphism orders and labeled orbit sizes;
7. checks the 5250 double-count identity.

No external MILP/SAT solver is required for this classification.
