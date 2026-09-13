# Erdős #500 — S04 Seven-Optimum Fertility Classified

**Author:** Jared Wilder  
**Public classification release:** 2026-09-11  
**Former status:** `UNPROVED_CHECKABLE_TARGET`  
**Current status:** `EXACT_FINITE_FERTILITY_CLASSIFICATION`

## Result

For the four isomorphism classes of optimal 12-edge seven-vertex covers from S02, let

```text
tau(P)
```

be the minimum number of new edges containing a fresh vertex required to extend the parent `P` to an eight-vertex cover.

The four exact extension costs are

```text
8, 8, 8, 9.
```

Since

```text
c_8-c_7 = 20-12 = 8,
```

the first three parent orbits have optimal eight-vertex children, while the fourth does not.

The numbers of minimum pair families at the minimum cost are

```text
20, 9, 5, 203,
```

respectively.

Thus the fourth parent has minimum child size

```text
12+9 = 21,
```

one edge above optimum.

## Stronger separation: deletion spectrum does not determine fertility

Two of the S02 parent orbits share the same deletion-excess spectrum

```text
(0,1,1,1,1,1,1).
```

Nevertheless their extension behavior differs:

- one has extension cost `8` and exactly **5** optimal anchored children;
- the other has extension cost `9` and therefore **no** optimal eight-child.

So the deletion-excess spectrum alone is not a complete reproductive invariant.

This is a useful obstruction for any attempted finite-state theory based only on deletion spectra: at least one additional structural coordinate is required to predict optimal one-point fertility.

## Exact computation

For a seven-parent `P`, let

```text
H = C([7],3) \ P.
```

Adding a new vertex `x` reduces to choosing a pair family `F` on the seven old vertices meeting every triple in `H`. The extension cost is therefore the pair-cover number

```text
tau_2(H).
```

There are only 21 possible pairs.

- At cost 8, the exhaustive search space is `C(21,8)=203490`.
- The first three parent orbits have 20, 9, and 5 valid pair covers respectively.
- The fourth has none at cost 8.
- At cost 9, the fourth parent has exactly 203 valid pair covers, proving its minimum is 9.

The computation is included in `verify_s03_optimal_eight.py`, which also checks the complete S03 optimal-eight classification.

## Scope

The old S04 wording asked whether a pair-cover extension statistic separates named Turán-type and non-Turán seven-state orbits, or whether all optima share one reproductive phenotype.

The exact finite conclusion now available is stronger in a representation-free sense:

> optimal seven-state reproductive phenotype is **not constant**; exactly one of the four isomorphism classes has extension defect 1, and two classes with identical deletion spectrum have different fertility.

No asymptotic claim is made from this finite separation alone.
