# Erdős #500 — S01 Human Rotor Rigidity CLOSED

**Author:** Jared Wilder  
**Public proof release:** 2026-09-11  
**Former status:** `UNPROVED_CHECKABLE_TARGET`  
**Current status:** `PROVED`

## Theorem

Every six-edge 3-uniform hypergraph on six vertices that meets every four-set in a contained edge is, up to relabeling, the cyclic pair rotor

```text
M2 = {012,013,045,145,234,235}.
```

Equivalently, every optimum for the six-vertex covering problem has a unique partition of the vertices into three pair-codegree-2 pairs, and the six hyperedges are obtained by orienting those three pairs in a directed 3-cycle and taking each full pair together with either vertex of its successor pair.

## Proof

Let `M` be a six-edge cover on six vertices.

### 1. Every five-vertex deletion is optimal

For each vertex `v`, the deletion `M-v` is a cover on the remaining five vertices, hence

```text
|M-v| >= c5 = 3.
```

Each triple of `M` survives exactly three of the six vertex deletions, so

```text
sum_v |M-v| = 3|M| = 18.
```

There are six summands, each at least 3, and their sum is 18. Therefore

```text
|M-v| = 3
```

for every `v`.

The three-edge five-vertex optimum is unique up to isomorphism, with representative

```text
H1 = {012,013,234}.
```

Its vertex-degree multiset is

```text
(2,2,2,2,1).
```

### 2. The six-vertex cover is 3-regular

Since

```text
|M-v| = |M| - d_M(v) = 3,
```

we have

```text
d_M(v)=3
```

for every vertex `v`.

### 3. Pair-codegree 2 defines a perfect matching

Fix `v`. For every other vertex `u`, deleting `v` removes exactly `lambda(v,u)` edges incident with `u`. Hence

```text
d_{M-v}(u) = 3 - lambda(v,u).
```

But the degree multiset in `M-v` is `(2,2,2,2,1)`. Therefore, among the five vertices `u!=v`, exactly one satisfies

```text
lambda(v,u)=2,
```

and the other four satisfy

```text
lambda(v,u)=1.
```

Thus every vertex has a unique codegree-2 partner. Symmetry of codegree makes these partnerships three disjoint pairs; call them

```text
A, B, C.
```

All cross-pairs between distinct matched pairs have codegree exactly 1.

### 4. Every hyperedge contains exactly one full matched pair

Each of the three matched pairs has codegree 2, so there are

```text
3*2 = 6
```

incidences `(matched pair, hyperedge containing it)`.

A triple cannot contain two disjoint matched pairs, because that would require four vertices. Hence each hyperedge contains at most one matched pair.

There are six hyperedges and six matched-pair incidences, so every hyperedge contains exactly one full matched pair.

Consequently the two edges containing a matched pair consist of that pair plus two third vertices chosen from `B union C` (and cyclically).

### 5. The pair-level orientation is forced

For two matched pairs `A` and `B`, let `t_AB` be the number of the two `A`-edges whose third vertex lies in `B`. Thus `t_AB` is 0, 1, or 2.

The four vertex-pairs joining `A` to `B` all have codegree 1. Edges based at `A` contribute `2 t_AB` such cross-pair incidences, while edges based at `B` contribute `2 t_BA`. Therefore

```text
t_AB + t_BA = 2.                (1)
```

The case

```text
t_AB = t_BA = 1
```

is impossible. Indeed, suppose the `A`-edge uses `b_i` and the `B`-edge uses `a_j`. Then the cross-pair `{a_j,b_i}` occurs in both edges, while the opposite cross-pair `{a_{1-j},b_{1-i}}` occurs in neither. This contradicts the fact that every `A-B` cross-pair has codegree exactly 1.

Hence for every two matched pairs the only possibilities are

```text
(t_AB,t_BA) = (2,0) or (0,2).
```

Orient `A -> B` when `t_AB=2`. Each matched pair has exactly two hyperedges total, so each pair-node has exactly one successor among the other two pair-nodes.

A tournament on three vertices in which every vertex has outdegree 1 is the directed 3-cycle. Therefore, after relabeling the pairs,

```text
A -> B -> C -> A.
```

The six hyperedges are exactly the two triples consisting of each full pair plus either vertex of its successor pair. This is the rotor construction `M2`.

The theorem follows.

## Consequences

- The optimum six-vertex orbit is unique without exhaustive enumeration.
- The three codegree-2 pairs are intrinsically recoverable from the hypergraph, so the rotor pair partition is unique.
- The automorphism structure `(C2)^3 semidirect C3` is transparent from the pair swaps and cyclic rotation.

The existing finite enumeration of 30 labeled optima remains a useful independent regression check, but it is no longer load-bearing for rigidity.
