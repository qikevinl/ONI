# AGENTS.md — Knowledge Compounding for Drafts Repository

> **Purpose:** Persistent learnings from working sessions. AI agents read this file at the start of each session to benefit from discovered patterns, decisions, and pending work.

**Last Updated:** 2026-02-02
**Sessions Tracked:** 1

---

## Session Memory

> **Quick context for session continuity.** Update this section at the end of each session.

### Current Workstreams

| Workstream | Status | Last Activity | Notes |
|------------|--------|---------------|-------|
| **QIF Deep Dive & Fixes** | Active | 2026-02-02 | Critical math fixes applied (phase variance, transport entropy, normalization) |
| **Brand Strategy** | Draft v0.2 | 2026-02-02 | QInnovate/Mindloft/QIF hierarchy defined |
| **QIF Whitepaper (Quarto)** | Active | 2026-02-02 | Monolithic .qmd exists, 14 chapter stubs empty, needs expansion |
| **Truth Propagation** | Planning | 2026-02-02 | PROPAGATION.md created, workflow defined but not yet fully exercised |
| **QIF Lab** | Active | 2026-02-02 | Equations, tests, synthetic data — core implementations live here |

### User Preferences & Decisions

| Preference | Decision | Date |
|------------|----------|------|
| **QIF pronunciation** | "CHIEF" (Quantum Indeterministic Framework) | 2026-02-02 |
| **Brand hierarchy** | QInnovate > Mindloft > QIF (nested, not parallel) | 2026-02-02 |
| **QI double meaning** | Kevin Qi's surname + Quantum Indeterminacy variable | 2026-02-02 |
| **Truth flow direction** | QIF-TRUTH.md → repo docs → blogs (never backwards) | 2026-02-02 |
| **Package names** | Keep `oni-*` for now, don't rename to `qif-*` yet | 2026-02-02 |

### Pending Items

| Item | Priority | Context |
|------|----------|---------|
| **Whitepaper fixes from deep dive** | High | Zeno-BCI claim needs reframing, no-cloning overstated, missing Related Work |
| **Whitepaper chapter stubs** | Medium | 14 empty .qmd files need content from monolithic source |
| **Missing interactive visualizations** | Medium | QI Equation Calculator, Decoherence Explorer not yet built |
| **ONI repo sync** | Medium | coherence.py, layers.py still NEEDS_SYNC per QIF-TRUTH.md S6 |
| **Blog sync** | Low | 2 blogs still marked REVIEW in truth doc |
| **Domain purchase** | Decision needed | qinnovate.com + mindloft.org recommended in brand strategy |
| **Org structure** | Decision needed | Personal project vs nonprofit vs LLC |
| **Falsifiability section** | Medium | Whitepaper needs explicit section on what would disprove QIF |

### Recent Session Context

**2026-02-02 Session:**
- Ran 4-agent deep dive on QIF whitepaper (math, code, docs, empirical validity)
- Applied critical fixes: transport variance mean→sum, phase variance→circular with π² scaling, σ²τ renamed to Hτ, Candidate 1 normalization enforced
- Created BRAND-STRATEGY.md v0.2 (QInnovate/Mindloft/QIF hierarchy)
- Committed all changes to drafts repo
- Added Quarto whitepaper build outputs and WIP 3D model to tracking

---

## Directory Guide

> **What lives where in the drafts repo.**

```
drafts/
├── AGENTS.md               ← THIS FILE
├── ai-working/             ← QIF research & development (has its own AGENTS.md)
│   ├── QIF-TRUTH.md        ← CANONICAL source of truth for all QIF equations
│   ├── PROPAGATION.md      ← Truth propagation protocol
│   ├── BRAND-STRATEGY.md   ← QInnovate/Mindloft/QIF brand hierarchy
│   ├── QIF-WHITEPAPER.md   ← Whitepaper narrative draft
│   ├── QIF-WIKI.md         ← Wiki-style reference
│   ├── QI-EQUATION-RESEARCH.md ← Equation derivation notes
│   ├── qif-lab/            ← Python implementations + tests
│   ├── Articles/           ← Article drafts
│   ├── Artifacts/          ← Generated artifacts
│   └── Quantum Hacking/    ← Quantum attack research
├── content/                ← Legacy topic drafts (pre-QIF naming)
│   ├── Coherence Metric/
│   ├── Neural Firewalls/
│   ├── Neural Ransomware/
│   ├── Quantum Hacking/
│   ├── Quantum Tunneling VPN/
│   ├── Scale Frequency/
│   └── Tunneling Traversal Time/
├── notes/                  ← Personal notes, Google Docs exports
├── sync/                   ← Medium publishing staging
│   └── Medium/
└── wip/                    ← Active side projects
    ├── Alzheimers- the rest is history/
    ├── CardiacNSIM/
    ├── NeuroSim/
    ├── ONI_Whitepaper_v1.md
    ├── qif-3d-model.html
    └── whitepaper-figures/
```

### Key Relationships

| This File | Feeds Into | Notes |
|-----------|-----------|-------|
| `ai-working/QIF-TRUTH.md` | ONI repo docs, blogs | Canonical truth — all changes start here |
| `ai-working/qif-lab/` | ONI repo `oni-framework/` | Lab implementations validated here first |
| `ai-working/BRAND-STRATEGY.md` | qinnovates.github.io, READMEs | Brand decisions propagate to public sites |
| `content/` topics | ONI `publications/` | Legacy drafts that became ONI publications |
| `wip/` projects | Various repos | Side projects at various stages |

---

## Critical Discoveries

| Date | Learning | Impact |
|------|----------|--------|
| 2026-02-02 | Transport variance was using `np.mean` but QIF-TRUTH.md says `−Σᵢ ln(pᵢ)` (sum) | Fixed in qif_equations.py — affects all coherence calculations |
| 2026-02-02 | Phase variance needs circular statistics (1−R)·π² not linear variance | Fixed — linear variance breaks at 2π wraparound |
| 2026-02-02 | σ²τ is actually Shannon entropy (Hτ), not a statistical variance | Renamed in truth doc and code — prevents conceptual confusion |
| 2026-02-02 | QI Candidate 1 adds terms of different dimensions without normalization | Fixed — all inputs now must be [0,1] normalized with hat notation |
| 2026-02-02 | Test had `or True` making assertion always pass (dead test) | Fixed — replaced with proper deterministic baseline check |
| 2026-02-02 | QIF lives INSIDE Mindloft, not parallel to it | Fixed in brand strategy — nested hierarchy, not siblings |

### Patterns Established

- **QIF-TRUTH.md is always updated FIRST** — code and docs follow, never the reverse
- **Deep dives should use parallel agents** — math, code, docs, empirical validity as separate concerns
- **Brand hierarchy is nested** — QInnovate > Mindloft > QIF (like Google > Android > Pixel)
- **Circular statistics for phase data** — never use linear variance on angular measurements
- **Entropy vs variance naming matters** — Hτ (entropy) communicates the math correctly, σ²τ doesn't

### Gotchas

- The `content/` folder uses legacy ONI topic names — these map to ONI `publications/` folders
- `notes/` contains `.gdoc` files (Google Docs links, not actual content) — don't try to read them
- `sync/Medium/` is for staging Medium posts — don't put final content here
- QIF-TRUTH.md Section 6 tracks sync status — check it before assuming docs are current
- Quarto whitepaper `_freeze/` contains cached figures — don't delete without rebuilding

---

## Session Protocol

### At Session Start

1. Read this file (`drafts/AGENTS.md`)
2. If working on QIF: read `ai-working/AGENTS.md`
3. Check **Pending Items** above
4. Check QIF-TRUTH.md Section 6 sync dashboard if doing QIF work

### At Session End

1. Update **Current Workstreams** status
2. Move completed items out of **Pending Items**
3. Add new discoveries to **Critical Discoveries**
4. Write 3-5 bullet **Recent Session Context**
5. Increment **Sessions Tracked** counter

---

*This file is read by AI agents at session start. Update at session end.*
