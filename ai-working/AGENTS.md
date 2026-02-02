# AGENTS.md — Knowledge Compounding for ai-working/

> **Purpose:** Persistent learnings specific to the QIF research and development workspace. This is where the science happens.

**Last Updated:** 2026-02-02
**Sessions Tracked:** 1

---

## Session Memory

### Current Focus

| Focus Area | Status | Notes |
|------------|--------|-------|
| **QIF Equations** | Code validated | Critical fixes applied 2026-02-02 (phase, transport, normalization) |
| **QIF-TRUTH.md** | Canonical | Updated with circular variance, Hτ rename, normalization table |
| **Whitepaper (Quarto)** | Needs work | Monolithic .qmd exists; 14 chapter stubs empty; physics claims need revision |
| **Brand Strategy** | Draft v0.2 | Ready for Kevin's review and voice refinement |
| **Propagation Protocol** | Defined | PROPAGATION.md created; not yet fully exercised |

### Known Issues (Prioritized)

#### Must Fix Before Publication

| Issue | File(s) | Details |
|-------|---------|---------|
| **Zeno-BCI claim** | QIF-WHITEPAPER.md, whitepaper .qmd | Claims continuous BCI monitoring creates quantum Zeno effect — this is a physics error. Measurement frequency (~1kHz) is too slow relative to decoherence (~fs). Reframe as metaphor or remove. |
| **No-cloning theorem scope** | QIF-WHITEPAPER.md | Overstates application — no-cloning prevents copying unknown quantum states, but BCI signals are classical measurements of quantum processes. Need precise boundary statement. |
| **Missing Related Work** | QIF-WHITEPAPER.md | No Related Work section. Must cite: Martinovic (2012) side-channel BCI, Bonaci (2014) subliminal attacks, Frank et al. (2017) BCI threat model. |
| **References need DOIs** | QIF-WHITEPAPER.md | Several references lack DOIs or have incomplete metadata. |

#### Should Fix

| Issue | File(s) | Details |
|-------|---------|---------|
| **Intro is bullet points** | QIF-WHITEPAPER.md | Introduction section reads as bullet list, not academic prose. |
| **Section ordering** | QIF-WHITEPAPER.md | Classical layers (L1-L7) described before establishing neural context. Consider: motivation → threat model → architecture → equations. |
| **Falsifiability section missing** | QIF-WHITEPAPER.md | Need explicit section: "What would disprove QIF?" with testable predictions. |
| **14 empty chapter stubs** | qif-lab/whitepaper/*.qmd | Chapter files exist but have no content. Need to extract from monolithic .qmd or write fresh. |
| **Missing visualizations** | Planned | QI Equation Calculator (interactive), Decoherence Explorer (time slider) not yet built. |

#### ONI Repo Sync Needed

| Truth Section | Repo File | Status |
|---------------|-----------|--------|
| S3 Coherence | `oni-framework/oni/coherence.py` | NEEDS_SYNC — still uses old formula |
| S2 Layer Model | `oni-framework/oni/layers.py` | NEEDS_SYNC — may reference old naming |
| S4 QI Equation | Blog posts (2) | REVIEW — may reference old σ²τ notation |

---

## QIF Equation Reference (Quick Access)

> These are the canonical equations from QIF-TRUTH.md. If code or docs differ, QIF-TRUTH.md wins.

### Coherence Metric

```
Cₛ = e^(−(σ²ᵩ + Hτ + σ²ᵧ))
```

| Term | Name | Computation | Range |
|------|------|-------------|-------|
| σ²ᵩ | Phase variance | (1 − R)·π² where R = \|mean(e^(iφ))\| | 0 to π² |
| Hτ | Transport entropy | −Σᵢ ln(pᵢ) | 0 to ∞ |
| σ²ᵧ | Gain variance | mean(((a − ā)/ā)²) | 0 to ∞ |

### Decision Matrix

| Cₛ | Auth Valid | Action |
|----|-----------|--------|
| > 0.6 | Yes | ACCEPT |
| > 0.6 | No | REJECT + ALERT |
| 0.3–0.6 | Yes | ACCEPT + FLAG |
| 0.3–0.6 | No | REJECT + ALERT |
| < 0.3 | Any | REJECT + CRITICAL |

### QI Candidate 1 (Additive/Engineering)

```
QI(t) = α·Ĉclass + β·(1 − ΓD(t))·[Q̂i + δ·Q̂entangle] − γ·Q̂tunnel
```

All inputs normalized to [0,1]. Hat notation = normalized. Coefficients uncalibrated.

### QI Candidate 2 (Tensor/Theoretical)

```
S_QI = Cclass · e^(−Squantum)
Squantum = SvN(ρ(t)) + λ·Φtunnel − μ·E(ρAB)
```

Scalar approximation of full tensor product QI = Cclass ⊗ e^(−Squantum).

---

## File Map

| File | Purpose | Truth Priority |
|------|---------|---------------|
| `QIF-TRUTH.md` | **CANONICAL** — all equations, definitions, layer model | 0 (highest) |
| `PROPAGATION.md` | How truth flows to repo and blogs | Protocol |
| `BRAND-STRATEGY.md` | QInnovate/Mindloft/QIF brand hierarchy | Strategy |
| `QIF-WHITEPAPER.md` | Whitepaper narrative draft (Markdown) | Content |
| `QIF-WIKI.md` | Wiki-style quick reference | Reference |
| `QI-EQUATION-RESEARCH.md` | Derivation notes, candidate comparison | Research |
| `qif-lab/` | Python implementations + tests + Quarto | Implementation |
| `qif-lab/src/qif_equations.py` | Core equation code | Implementation |
| `qif-lab/src/synthetic_data.py` | Test scenario generator | Testing |
| `qif-lab/test_equations.py` | Equation test suite | Validation |
| `qif-lab/whitepaper/` | Quarto whitepaper source + builds | Publication |

---

## Critical Discoveries

| Date | Discovery | Impact |
|------|-----------|--------|
| 2026-02-02 | **Phase data requires circular statistics** — linear variance of angles is wrong when phases wrap around 2π. Circular variance (1−R)·π² correctly handles this. | Changed formula in truth doc, code, and all downstream |
| 2026-02-02 | **Transport "variance" is actually entropy** — The −Σᵢ ln(pᵢ) formula is Shannon surprise/entropy, not statistical variance. Calling it σ²τ is misleading. | Renamed to Hτ everywhere. Helps readers understand the math correctly. |
| 2026-02-02 | **Candidate 1 had dimensional inconsistency** — Adding Cₛ (exponential decay [0,1]) + SvN (unbounded entropy) + T (probability [0,1]) doesn't work dimensionally. All terms must be normalized to [0,1] first. | Added normalization requirement with explicit table of methods. Hat notation (Ĉ, Q̂) distinguishes raw from normalized. |
| 2026-02-02 | **Quantum Zeno claim is wrong at BCI timescales** — Zeno effect requires measurement faster than system evolution. BCI measures at ~1kHz; quantum coherence decays in femtoseconds. 12 orders of magnitude gap. | Must reframe in whitepaper — either as analogy/metaphor or remove entirely. |
| 2026-02-02 | **No-cloning theorem is overapplied** — QIF cites no-cloning as protecting neural data, but BCI signals are classical measurements. The protection applies only to the underlying quantum state at the electrode boundary, not to the transmitted data. | Need precise boundary statement in whitepaper. |
| 2026-02-02 | **Decoherence time τ_D is a tunable parameter** — This is a strength, not a weakness. Framework works for any τ_D value. When experiments measure actual decoherence times, plug them in. No code changes needed. | Document this explicitly as a design feature in whitepaper. |

### Patterns

- **Truth-first development**: Change QIF-TRUTH.md → update code → update docs → update blogs. Never reverse.
- **Circular statistics for anything angular**: Phase, direction, orientation — always use circular mean/variance.
- **Name things what they are**: σ²τ was confusing because it's not a variance. Hτ immediately tells you it's entropy.
- **Normalization must be explicit**: If you add terms, they must be in the same units. Document the normalization.
- **Parameters > assumptions**: τ_D, coefficients (α,β,γ,δ), scaling factors — leave them tunable. Hardcoding guesses is worse than parameterizing unknowns.

### Gotchas

- `test_equations.py` had `or True` on a critical assertion — tests that always pass catch nothing. Always review test assertions for tautologies.
- Quarto `_freeze/` directory holds cached computation results — deleting it means re-running all code cells.
- The monolithic whitepaper `.qmd` and the 14 chapter `.qmd` stubs coexist — they're not yet reconciled.
- `auto_publish.py`, `medium_sync.py`, `medium_sync_public.py`, `medium_template_v2.py` — these are publishing automation scripts, not QIF content.
- `resume.md` and `yale-email-draft.md` are personal documents, not QIF research.

---

## Session Protocol

### At Session Start

1. Read this file
2. Read `QIF-TRUTH.md` Section 6 (sync dashboard) — flag anything `NEEDS_SYNC` or `REVIEW`
3. Check **Known Issues** above for current priorities
4. If making equation changes: read `qif-lab/src/qif_equations.py` to understand current implementation

### At Session End

1. Update **Current Focus** statuses
2. Update **Known Issues** (add new, mark resolved)
3. Add discoveries to **Critical Discoveries**
4. Update QIF-TRUTH.md Section 6 if any sync status changed
5. Update parent `drafts/AGENTS.md` Recent Session Context

---

*This file is read by AI agents working on QIF research. Update at session end.*
