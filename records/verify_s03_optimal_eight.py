#!/usr/bin/env python3
"""Exact replay for Erdős #500 targets S03 and the finite core of S04.

Uses the four S02 optimal seven-cover representatives.  For each parent it
enumerates pair families for a one-point extension.  Optimal eight-covers
need 8 new edges because c_8-c_7=20-12=8.

Pure Python; no external solver is used.
"""

from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import factorial

PARENTS = [
    frozenset({(0,1,2),(0,1,3),(0,1,4),(0,2,3),(0,2,4),(0,5,6),
               (1,2,3),(1,2,4),(1,5,6),(2,5,6),(3,4,5),(3,4,6)}),
    frozenset({(0,1,2),(0,1,3),(0,1,4),(0,2,3),(0,4,5),(0,5,6),
               (1,2,3),(1,4,5),(1,5,6),(2,3,5),(2,4,6),(3,4,6)}),
    frozenset({(0,1,2),(0,1,3),(0,1,4),(0,2,3),(0,5,6),(1,2,3),
               (1,5,6),(2,4,5),(2,4,6),(2,5,6),(3,4,5),(3,4,6)}),
    frozenset({(0,1,2),(0,1,3),(0,2,3),(0,4,5),(0,4,6),(0,5,6),
               (1,2,4),(1,3,5),(1,4,6),(2,3,6),(2,5,6),(3,4,5)}),
]

PARENT_LABELED_ORBIT_SIZES = [210, 1260, 1260, 840]


def is_cover(n, M):
    M = set(M)
    return all(
        any(tuple(sorted(t)) in M for t in combinations(S, 3))
        for S in combinations(range(n), 4)
    )


def degrees(n, M):
    return [sum(v in e for e in M) for v in range(n)]


def deletion_excess_spectrum_8(M):
    # |M|=20 and c_7=12, hence |M-v|-12 = 8-d(v).
    return tuple(sorted(8 - d for d in degrees(8, M)))


def valid_extension_pairs(parent, r):
    pairs = list(combinations(range(7), 2))
    pair_index = {p:i for i,p in enumerate(pairs)}
    residual = [t for t in combinations(range(7), 3) if t not in parent]
    requirements = []
    for t in residual:
        mask = 0
        for p in combinations(t, 2):
            mask |= 1 << pair_index[p]
        requirements.append(mask)

    valid = []
    for comb in combinations(range(21), r):
        mask = 0
        for i in comb:
            mask |= 1 << i
        if all(mask & req for req in requirements):
            valid.append(comb)
    return pairs, valid


def child(parent, pairs, comb):
    return frozenset(set(parent) | {tuple(sorted((7,) + pairs[i])) for i in comb})


def canonical(M, perms8, triple_index):
    best = None
    for p in perms8:
        image = tuple(sorted(
            triple_index[tuple(sorted((p[a],p[b],p[c])))]
            for a,b,c in M
        ))
        if best is None or image < best:
            best = image
    return best


def family_from_canonical(canon, triples8):
    return frozenset(triples8[i] for i in canon)


def automorphism_order(M, perms8):
    target = frozenset(M)
    total = 0
    for p in perms8:
        image = frozenset(tuple(sorted((p[a],p[b],p[c]))) for a,b,c in M)
        if image == target:
            total += 1
    return total


def main():
    for parent in PARENTS:
        assert len(parent) == 12 and is_cover(7, parent)

    # Exact one-point fertility at the optimal 8-edge extension level.
    all_children = []
    parent_tags = []
    optimal_extension_counts = []
    min_extension_data = []

    for tag, parent in enumerate(PARENTS, start=1):
        pairs, valid8 = valid_extension_pairs(parent, 8)
        optimal_extension_counts.append(len(valid8))
        for comb in valid8:
            M = child(parent, pairs, comb)
            assert len(M) == 20 and is_cover(8, M)
            all_children.append(M)
            parent_tags.append(tag)

        if valid8:
            min_extension_data.append((8, len(valid8)))
        else:
            pairs9, valid9 = valid_extension_pairs(parent, 9)
            assert pairs9 == pairs
            assert valid9
            min_extension_data.append((9, len(valid9)))

    assert optimal_extension_counts == [20, 9, 5, 0]
    assert min_extension_data == [(8,20),(8,9),(8,5),(9,203)]
    assert len(all_children) == 34

    anchored_spectra = Counter(deletion_excess_spectrum_8(M) for M in all_children)
    assert anchored_spectra == Counter({
        (0,0,0,0,1,1,1,1): 27,
        (0,0,0,0,0,1,1,2): 5,
        (0,0,0,0,0,0,2,2): 2,
    })

    triples8 = list(combinations(range(8), 3))
    triple_index = {t:i for i,t in enumerate(triples8)}
    perms8 = list(permutations(range(8)))

    orbit_members = defaultdict(list)
    orbit_parents = defaultdict(Counter)
    for M, tag in zip(all_children, parent_tags):
        c = canonical(M, perms8, triple_index)
        orbit_members[c].append(M)
        orbit_parents[c][tag] += 1

    assert len(orbit_members) == 6

    rows = []
    for c in sorted(orbit_members):
        rep = family_from_canonical(c, triples8)
        aut = automorphism_order(rep, perms8)
        orbit_size = factorial(8) // aut
        spectrum = deletion_excess_spectrum_8(rep)
        rows.append((spectrum, len(orbit_members[c]), aut, orbit_size, orbit_parents[c], c))

    expected = sorted([
        ((0,0,0,0,0,0,2,2), 2, 72, 560),
        ((0,0,0,0,0,1,1,2), 5, 4, 10080),
        ((0,0,0,0,1,1,1,1), 9, 4, 10080),
        ((0,0,0,0,1,1,1,1), 7, 8, 5040),
        ((0,0,0,0,1,1,1,1), 7, 8, 5040),
        ((0,0,0,0,1,1,1,1), 4, 4, 10080),
    ])
    actual = sorted((s,a,aut,o) for s,a,aut,o,_,_ in rows)
    assert actual == expected

    labeled_total = sum(row[3] for row in rows)
    assert labeled_total == 40880

    # Double-count (labeled optimal 8-cover, optimal 7-deletion) pairs.
    lhs = sum(orbit * spectrum.count(0) for spectrum, _, _, orbit, _, _ in rows)
    rhs = 8 * sum(size * ext for size, ext in zip(PARENT_LABELED_ORBIT_SIZES,
                                                   optimal_extension_counts))
    assert lhs == rhs == 174720

    print("PASS")
    print("optimal extension counts by S02 parent orbit = [20, 9, 5, 0]")
    print("minimum extension data (cost,count) =", min_extension_data)
    print("anchored optimal children = 34")
    print("isomorphism classes = 6")
    print("labeled optimal 8-covers = 40880")
    print("optimal-deletion double count = 174720")
    for spectrum, anchored, aut, orbit, parents, canon in rows:
        print(f"spectrum={spectrum} anchored={anchored} aut={aut} labeled_orbit={orbit} parents={dict(parents)}")
        print(" representative=", tuple(triples8[i] for i in canon))


if __name__ == "__main__":
    main()
