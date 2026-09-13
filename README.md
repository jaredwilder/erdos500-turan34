# Erdős #500 — Turán (3,4)

**Author:** Jared Wilder  
**Status:** theorem / finite-target / density-structure research program; the Turán (3,4) problem is **not claimed solved**.

This repository is the canonical public home for the estate's #500 work. The reconstructed program contains **76 records** spanning proved-in-packet results, exact finite targets, structural identities, equivalences, analytic reductions, witnesses/classifications, and negative theorems.

## Structural content

Among the useful recovered mathematics is a density-staircase identity for optimal triple covers, with an exact criterion for density plateaus in terms of vertex-deletion optimality and regularity of optimum covers. The finite and asymptotic lanes are kept separate.

## Source layout

Exact public source bytes are migrated under:

- `program/` — main #500 theorem/finite-target package;
- `formal-mirrors/` — matching `erdos500-*` material from `erdos-theorems`;
- `records/` — compact #500 material already routed through `combinatorial-records`.

No bounded computation is promoted into a global Turán theorem, and historical novelty remains a separate literature question.

## Recovered original source packet — 2026-09-13

This original 78-record source variant complements the existing 76-record reconstructed program. The variants remain separate. Eighteen records are explicitly unproved targets. The standard-library finite checks passed on 2026-09-13; the optional SciPy MILP check was not run. This does not solve the Turan (3,4) problem or establish novelty.

- [Original record table](program/original-forge-2026-08-04/ERDOS-500-THEOREM-RECORDS.jsonl)
- [Source packet](program/original-forge-2026-08-04/)
- [Source hashes and observed status counts](verification/source-packet.json)

Run `python verification/verify_source_packet.py` to verify all recovered source bytes, original JSON manifests when present, and record counts.

### Finite replay

Run `python verification/replay_packet.py --receipt verification/local-replay.json`. The runner uses a temporary copy and preserves the original packet and historical receipts. See the [2026-09-13 replay receipt](verification/replay-2026-09-13.json).
