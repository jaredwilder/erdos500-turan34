# Erdős #500 — S14 first-nonhereditary frontier through `n=9`

**Author:** Jared Wilder  
**Public release:** 2026-09-11  
**Former target:** find the smallest `n` for which an optimal `n`-vertex cover has no optimal `(n-1)`-vertex deletion.

## Result

No such example exists for

```text
5 <= n <= 9.
```

Therefore, if an optimal cover with no optimal one-vertex deletion exists, its order satisfies

```text
n >= 10.
```

This is a finite frontier statement, not a global heredity theorem.

## n=5

The exact optimum is `c_5=3` and `c_4=1`.

For a three-edge five-vertex cover, each triple survives exactly two vertex deletions, so

```text
sum_v |M-v| = 2*3 = 6.
```

Every four-vertex deletion is a cover and has at least one edge. Thus the total deletion excess above the baseline `5*c_4=5` is exactly one.

Consequently exactly four deletions have size 1 and are optimal, while the remaining deletion has size 2.

## n=6

The exact optimum is `c_6=6`.

By the human rotor-rigidity theorem, every six-edge optimum is the cyclic pair rotor. Its six vertex deletions all have exactly three edges, hence every deletion is an optimal five-vertex cover.

Thus every optimum has six optimal deletions.

## n=7

The exact S02 classification gives four isomorphism classes of 12-edge optima. Their deletion-excess spectra over `c_6=6` are

```text
(0,0,0,1,1,2,2),
(0,0,1,1,1,1,2),
(0,1,1,1,1,1,1),
(0,1,1,1,1,1,1).
```

Hence the numbers of optimal six-vertex deletions are respectively

```text
3, 2, 1, 1.
```

Every optimal seven-state therefore has at least one optimal deletion.

## n=8

The exact S03 classification gives six isomorphism classes of 20-edge optima. Their possible deletion-excess spectra over `c_7=12` are

```text
(0,0,0,0,0,0,2,2),
(0,0,0,0,0,1,1,2),
(0,0,0,0,1,1,1,1).
```

Thus every optimal eight-state has at least

```text
4
```

optimal seven-vertex deletions; the possible counts are 6, 5, and 4.

## n=9

The exact values are

```text
c_8=20,
c_9=30.
```

Therefore the normalized covering densities agree:

```text
c_8 / C(8,3) = 20/56 = 5/14,
c_9 / C(9,3) = 30/84 = 5/14.
```

This is a density plateau. The deletion-debt identity gives zero total deletion excess, so every deletion of every optimal nine-vertex cover is an optimal eight-vertex cover.

Equivalently every optimum has all nine deletions optimal.

## Frontier

Combining the five cases yields

```text
first possible nonhereditary optimum: n >= 10.
```

The current estate does not contain an exact proof of `c_10`; a feasible 45-edge ten-vertex cover is known from exploratory search, but a timed solver run did not certify optimality. Accordingly this file makes no assertion at `n=10` beyond identifying it as the first unresolved order for S14.

## Reproducibility

- S01 human rotor proof: `S01-HUMAN-ROTOR-RIGIDITY-CLOSED.md`
- S02 exact seven-state verifier: `verify_s02_optimal_seven.py`
- S03 exact eight-state verifier: `verify_s03_optimal_eight.py`

The n=9 conclusion is an exact algebraic consequence of `c_8=20`, `c_9=30`, and the deletion-debt identity.
