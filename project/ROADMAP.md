# Roadmap

> **Auto-generated from [prd.json](prd.json)** — do not edit directly.
> Last updated: 2026-02-04 22:51

## Progress

| Total | Completed | Pending | Rate |
|-------|-----------|---------|------|
| 46 | 40 | 6 | 87% |

```
[█████████████████░░░] 86%
```

## Pending Tasks

- 🟡 **changelog-creation**: Create CHANGELOG.md at repository root
- 🟠 **python-code-sync**: Verify oni-framework/oni/layers.py matches corrected ONI model
- 🟡 **moabb-coherence-benchmark**: Benchmark coherence metric (Cₛ) accuracy against real MOABB EEG data
  - Depends on: moabb-adapter-implementation
- 🟡 **moabb-attack-scenarios**: Create real-signal attack scenarios using MOABB data
  - Depends on: moabb-adapter-implementation
- 🟠 **brainflow-integration**: Add BrainFlow integration for real-time hardware support. BrainFlow provides uniform API for 20+ biosensor boards (OpenBCI, Muse, BrainBit, etc). Use as primary data acquisition layer for live Cₛ(S) computation.
  - Depends on: layer-aware-coherence-implementation
- 🟠 **layer-aware-coherence-implementation**: Implement the unified layer-aware coherence metric Cₛ(S) in Python. Core equation: Cₛ(S) = e^(−Σ_f w(f,S)·(σ²φ(f) + σ²τ(f) + σ²γ(f))). Requires: (1) per-frequency STFT decomposition, (2) per-frequency variance computation for phase/transport/gain, (3) weighting function w(f,S) with configurable layer spatial scales, (4) real-time scoring pipeline. Use BrainFlow or Neuromore for data acquisition, MOABB for offline validation.
  - Depends on: moabb-coherence-benchmark

## Future Work

### 🚧 Federated AI Training for Privacy-Preserving Neural Security

Implement federated learning architecture where AI models train locally on user devices, sharing only encrypted gradients with central servers. TARA portal receives only mathematical scores (Cₛ, Δ, σ)—never raw neural data. This enables collective learning while preserving individual privacy.

**Rationale:** Current centralized ML approaches require raw data transmission, creating privacy risks. Federated learning enables model improvement without data exposure. This aligns with ONI's core principle: your thoughts stay on your device.

**Components:**
- ☐ Local Training Module
- ☐ Gradient Encryption Layer
- ☐ Differential Privacy Integration
- ☑️ Score-Only Transmission Protocol
- ☐ Secure Aggregation Server
- ☑️ Score Anonymization Layer

**Effort:** large
**Timeline:** 6-12 months for MVP
**Feasibility:** in-progress

---

### 📋 Neural Consent Publication Topic

Create publications/neural-consent/ with Blog and TechDoc on consent architecture for BCIs

**Rationale:** Consolidate Lázaro-Muñoz framework integration into publishable content

**Effort:** medium
**Feasibility:** practical

---

### 📋 AI-Based Attack Vector Prediction

Train AI models to predict future BCI attack vectors using ONI framework, biology, physics data

**Rationale:** Proactive defense requires anticipating attacks before they occur

**Effort:** large
**Feasibility:** research-needed

---

### 📋 Update Existing Blogs and Papers

Go back and update all existing blog posts and technical papers with corrected ONI layer model

**Effort:** medium
**Feasibility:** practical

---

### 📋 L11-L14 Standards Development

Develop governance and standards alignment for Layers 11-14 (Cognitive Transport, Cognitive Session, Semantic Layer, Identity Layer). Unlike L1-L7 (IEEE, IETF, NIST SP 800) and L8-L10 (IEC 62443, FDA guidance, NIST CSF), no established standards currently exist for cognitive and identity-layer security. Requires collaboration with Subject Matter Experts (neuroethicists, cognitive scientists, BCI researchers) and engagement with governing agencies (FDA, EU MDR, IEEE emerging working groups, NIST, UNESCO/OECD neuroethics initiatives).

**Rationale:** ONI_LAYERS.md Section 4 'Standards Alignment' notes L11-L14 depend on 'Emerging neuroethics frameworks' which are not yet mature. Framework adoption requires actionable standards at all layers.

**Effort:** large
**Timeline:** external-dependent
**Feasibility:** blocked-external

---

### 📋 The Problem with BCIs: Attack Surfaces Beyond Electrical Monitoring

Research and develop devices/methods that can monitor and protect neural systems at layers that current BCI electrodes cannot access. Electrodes can only interact at the millisecond-scale electrical signaling layer—they cannot detect or address molecular substrate attacks (nutritional depletion, enzymatic inhibition, receptor antagonism) or faster processes (femtosecond enzyme kinetics, nanosecond ion channel gating).

**Rationale:** Current BCIs have a fundamental blind spot: they monitor electrical activity but cannot detect biochemical attacks. An attacker could deplete iron (blocking dopamine synthesis), antagonize receptors (blocking neurotransmitter effects), or poison enzymes (halting production)—and the BCI would only see 'reduced signaling' without understanding the cause. This is a critical gap in neural security.

**Deliverables:**
- ☐ The Problem with BCIs: Why Your Brain Implant Can't See Everything
- ☐ BCI Blind Spots: Attack Surfaces Beyond Electrical Monitoring

**Effort:** large
**Timeline:** 12-24 months
**Feasibility:** research-needed

---

### 📋 Academic Discoverability & SEO for Research

Implement academic metadata and structured data to maximize discoverability by Google Scholar, Semantic Scholar, and research databases. Does NOT involve AI scrapers (GPTBot, CCBot, etc.) — those remain blocked.

**Rationale:** Academic visibility requires proper metadata, not AI crawler access. Google Scholar uses citation meta tags. Semantic Scholar indexes via ORCID/DOI. These are the real levers for research discoverability.

**Deliverables:**
- ☐ Add Google Scholar citation meta tags
- ☐ Add JSON-LD ScholarlyArticle schema
- ☐ Get DOI via Zenodo
- ☐ Create/link ORCID researcher profile
- ☐ Submit to Semantic Scholar
- ☐ Consider arXiv/SSRN preprint

**Effort:** small
**Timeline:** 1-2 weeks after framework finalization
**Feasibility:** practical

---

## Recent Completions

| Task | Completed | Learnings |
|------|-----------|-----------|
| immersive-3d-whitepaper-ui | 2026-02-02 | CSS perspective + rotateY creates convincing curved monit... |
| plotly-interactive-figures | 2026-02-02 | Plotly in self-contained Quarto works via include-in-head... |
| auto-dictation-engine | 2026-02-02 | extractReadableText via clone + remove (code, table, .kat... |
| security-hardening-all-sites | 2026-02-02 | GitHub Pages cannot set HTTP headers — must use meta http... |
| qif-neuroethics-document | 2026-02-02 | Quantum biometric data creates a regulatory gap — no exis... |
| qif-lab-readme | 2026-02-02 | README should emphasize the as-code principle — change eq... |
| kokoro-tts-audio-narration | 2026-02-02 | Kokoro TTS (Apache 2.0) is the best open-source option fo... |
| hourglass-scroll-effect | 2026-02-02 | Per-section transforms via getBoundingClientRect() + requ... |
| collapsible-callouts | 2026-02-02 | CSS max-height transitions with overflow:hidden create sm... |
| qif-field-journal | 2026-02-02 | Field notes serve dual purpose: personal journal AND publ... |
