# Erdős #500 finite-state literature reconciliation — 2026-09-11

Author: Jared Wilder

## Purpose

The release-day finite-state program independently reconstructed several exact small covering classifications. A literature collision performed after the reconstruction found that the class counts themselves were already known.

The correct publication boundary is therefore:

- preserve the independent proofs, verifiers, deletion spectra, fertility data and transition machinery;
- do **not** claim historical novelty for the small exact covering numbers or the counts of isomorphism classes listed below;
- treat agreement with the historical enumeration as a strong independent validation event.

## Applegate–Rains–Sloane (2003)

David Applegate, E. M. Rains and N. J. A. Sloane, *On Asymmetric Coverings and Covering Numbers*, Journal of Combinatorial Designs 11 (2003), 218–228, Table IV/V, record:

- `C(7,4,3)=12` and exactly **4** nonisomorphic optimal designs of size 12;
- `C(8,5,4)=20` and exactly **6** nonisomorphic optimal designs of size 20;
- `C(9,6,5)=30`;
- `C(10,7,6)=45` and exactly **20** nonisomorphic optimal designs of size 45.

Under the complement duality used in the Erdős #500 toolkit, these are the same finite covering numbers `c_7,c_8,c_9,c_10` for triple families meeting every four-set.

## Release-day consequences

### S02

`S02-OPTIMAL-SEVEN-STATE-CLASSIFICATION-CLOSED.md` independently recovers the **four** seven-vertex isomorphism classes and gives an elementary anchored-extension proof plus a dependency-free Python verifier.

The count `4` is known from the 2003 enumeration. The release-day value is independent reconstruction, deletion-excess spectra, orbit data, a direct double-count receipt, and a transparent replay path.

### S03

`S03-OPTIMAL-EIGHT-STATE-CLASSIFICATION-CLOSED.md` independently recovers the **six** eight-vertex isomorphism classes and gives a dimension-descent reconstruction from the S02 parents.

The count `6` is known from the 2003 enumeration. Again, the release-day contribution is the independent derivation, deletion spectra, transition counts, orbit data, and verifier.

### S04

`S04-SEVEN-OPTIMUM-FERTILITY-CLASSIFIED.md` studies a different observable: one-point extension cost / reproductive phenotype of the four seven-state classes. The 2003 table above does not by itself classify this fertility statistic.

No historical novelty claim is made here without a dedicated literature search, but S04 is not subsumed merely by the old class-count table.

### S14

The earlier release-day note correctly stopped at `n>=10`, but the exact finite covering number `c_10=45` is already known from the same 2003 source. Therefore `c_10` is **not** a release-day headline target.

Any further S14 progress must concern heredity/transition structure at order 10 or beyond, not rediscovery of the integer 45.

## Current headline boundary

The finite-state machinery is retained because it is useful and independently auditable. Historical novelty is separated from truth.

The active headline program should prioritize genuinely unresolved targets such as `C(13,6,3)`, whose current public bound remains `20 <= C(13,6,3) <= 21`, rather than re-solving small covering numbers already present in the historical design literature.
