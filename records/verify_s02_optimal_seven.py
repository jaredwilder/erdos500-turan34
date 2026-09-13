#!/usr/bin/env python3
"""Exact replay for Erdős #500 target S02.

Classifies all optimal 12-edge 3-uniform covers of the 4-sets on 7 vertices.
The reduction uses the proved fact that every optimum has a six-vertex rotor
deletion. Fixing that deletion leaves only C(15,6)=5005 pair families to test.

Pure Python; no external solver is used.
"""

from collections import Counter, defaultdict
from itertools import combinations, permutations
from math import factorial

M2 = frozenset({
    (0,1,2),(0,1,3),(0,4,5),(1,4,5),(2,3,4),(2,3,5)
})


def is_cover(n, M):
    M = set(M)
    return all(
        any(tuple(sorted(t)) in M for t in combinations(S, 3))
        for S in combinations(range(n), 4)
    )


def degrees(n, M):
    return [sum(v in e for e in M) for v in range(n)]


def deletion_excess_spectrum(M):
    # c_6 = 6 and |M| = 12, so |M-v|-6 = 6-d(v).
    return tuple(sorted(6 - d for d in degrees(7, M)))


def canonical(M, perms7):
    best = None
    for p in perms7:
        img = tuple(sorted(tuple(sorted(p[v] for v in e)) for e in M))
        if best is None or img < best:
            best = img
    return best


def automorphism_order(M, perms7):
    target = frozenset(M)
    total = 0
    for p in perms7:
        img = frozenset(tuple(sorted(p[v] for v in e)) for e in M)
        if img == target:
            total += 1
    return total


def main():
    assert is_cover(6, M2)
    assert len(M2) == 6

    pairs = list(combinations(range(6), 2))
    residual_triples = [t for t in combinations(range(6), 3) if t not in M2]
    assert len(pairs) == 15
    assert len(residual_triples) == 14

    valid_pair_families = []
    for F in combinations(pairs, 6):
        Fs = set(F)
        if all(any(p in Fs for p in combinations(t, 2)) for t in residual_triples):
            valid_pair_families.append(F)

    assert len(valid_pair_families) == 25

    covers = []
    for F in valid_pair_families:
        M = frozenset(set(M2) | {tuple(sorted((6,) + p)) for p in F})
        assert len(M) == 12
        assert is_cover(7, M)
        covers.append(M)

    spectra = Counter(deletion_excess_spectrum(M) for M in covers)
    expected_anchored_spectra = Counter({
        (0,0,0,1,1,2,2): 3,
        (0,0,1,1,1,1,2): 12,
        (0,1,1,1,1,1,1): 10,
    })
    assert spectra == expected_anchored_spectra

    perms7 = list(permutations(range(7)))
    orbit_members = defaultdict(list)
    for M in covers:
        orbit_members[canonical(M, perms7)].append(M)

    assert len(orbit_members) == 4

    rows = []
    for canon, anchored in sorted(orbit_members.items()):
        rep = frozenset(canon)
        aut = automorphism_order(rep, perms7)
        orbit_size = factorial(7) // aut
        spectrum = deletion_excess_spectrum(rep)
        rows.append((spectrum, len(anchored), aut, orbit_size, canon))

    summary = sorted((spec, anchored, aut, orbit) for spec, anchored, aut, orbit, _ in rows)
    expected_summary = sorted([
        ((0,0,0,1,1,2,2), 3, 24, 210),
        ((0,0,1,1,1,1,2), 12, 4, 1260),
        ((0,1,1,1,1,1,1), 6, 4, 1260),
        ((0,1,1,1,1,1,1), 4, 6, 840),
    ])
    assert summary == expected_summary

    labeled_total = sum(orbit for _, _, _, orbit, _ in rows)
    assert labeled_total == 3570

    # Double-count (labeled optimum, rotor deletion) pairs.
    lhs = sum(orbit * spectrum.count(0) for spectrum, _, _, orbit, _ in rows)
    rhs = 7 * 30 * 25
    assert lhs == rhs == 5250

    print("PASS")
    print("anchored_pair_families = 25")
    print("isomorphism_classes = 4")
    print("deletion_excess_spectra =")
    for spec, anchored, aut, orbit, canon in rows:
        print(f"  spectrum={spec} anchored={anchored} aut={aut} labeled_orbit={orbit}")
        print(f"    representative={canon}")
    print("labeled_optimal_7_covers = 3570")
    print("rotor_deletion_double_count = 5250")


if __name__ == "__main__":
    main()
