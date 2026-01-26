# ONI Demo Video - Session Notes
**Date:** 2026-01-26
**Session Summary:** Major video scene updates and script revisions

---

## COMPLETED WORK

### 1. TitleScene.tsx
- Added orbiting electron animation around ONI letters
- Electron orbits horizontally, dips into the "O" center
- Blue electron with glowing trail effect
- Changed ONI text to solid white (removed gradient)
- Updated tagline: "OPEN **NEURO**SECURITY INTEROPERABILITY" (NEURO is bold)
- Removed "No brains left behind" tagline

### 2. ProblemScene.tsx
- Made "ONI Framework" full-screen reveal
- ONI and Framework same size (140px)
- Added left-to-right animated gradient on ONI (darker blue → white)
- Gradient flows/animates to become bluer over time
- Staggered reveal: "Introducing" → "ONI Framework" → typing effect for bottom text
- Bottom text: "A unified neurosecurity stack for the next era of computing"

### 3. LayersScene.tsx (Complete Rewrite)
- Intro text: "14 layers spanning silicon to synapse"
- Phase 1 (frames 0-150): Intro animation
- Phase 2 (frames 150-450): Pan through L1-L7 with OSI model labels
  - Header: "SILICON LAYERS (L1-L7) — CLASSICAL OSI MODEL"
  - Each layer shows OSI mapping (Physical, Data Link, Network, etc.)
- Phase 3 (frames 450-750): L8 Neural Gateway zoom with dramatic glow
  - Header: "★ NEURAL GATEWAY — THE BRIDGE ★"
  - Scale up to 1.8x with pulsing glow effect
- Phase 4 (frames 750-1050): Pan through L9-L14 biology layers
  - Header: "BIOLOGY LAYERS (L9-L14) — NEURAL PROCESSING"
- Phase 5 (frames 1050-1200): Full stack view

### 4. CoherenceScene.tsx
- Fixed coherence formula to: **Cₛ = e^(−(σ²φ + σ²τ + σ²γ))**
- Updated component cards to show: σ²φ, σ²τ, σ²γ (variance notation)
- Added phase transitions:
  - Coherence section: frames 0-500
  - Scale-Frequency section: frames 500+
- Added `coherenceFadeOut` for smooth transitions between phases
- Added Scale-Frequency Invariant visualization:
  - Title: "Scale-Frequency Invariant"
  - Formula: f × S ≈ k
  - Animated bars showing Scale (10→1000), Frequency (100→1 Hz)
  - k constant stays ~1000 (invariant indicator)
- Fixed interactive demo callout animation timing

### 5. CoherenceGauge.tsx
- Formula correct: `C<sub>s</sub> = e<sup>−(σ²φ + σ²τ + σ²γ)</sup>`
- Updated component breakdown to show variance symbols (σ²φ, σ²τ, σ²γ)
- Values now show inverse relationship with coherence

### 6. script.ts (Narration Script)
- Updated coherence section with threshold/defense mechanism language
- Added Scale-Frequency narration
- Removed "All open source. All verifiable." from TARA section
- Extended "...and you" line timing for emphasis (frames 5460-5700)
- Adjusted all frame timings for ~3:53 runtime

---

## TODO - PENDING WORK

### High Priority

1. **Coherence Threshold Defense Visualization**
   - [ ] Look up specific threshold value in ONI docs
   - [ ] Add visual when coherence drops below threshold
   - [ ] Show shield/alert animation for defense mechanism activation
   - [ ] Include examples: MRI interference, electromagnetic disruption, injection attacks
   - [ ] Reference oni-academy documentation for specific examples

2. **"...and you" Animation Enhancement**
   - [ ] Implement slow pan-in effect
   - [ ] Make text white for emphasis
   - [ ] Extend hold time for dramatic effect

3. **Remove TARA "100% open source" Text**
   - [ ] Find and remove from TaraScene.tsx (if it exists)
   - [ ] Script already updated

4. **Header Text Update**
   - [ ] Change "ONI Neural Security" → "ONI Neural Security Suite"
   - [ ] Match GitHub Pages: https://qikevinl.github.io/ONI/

5. **Scale-Frequency Detailed Visualization**
   - [ ] Create dedicated visualization explaining the concept
   - [ ] Show how f × S ≈ k works in neural contexts
   - [ ] Add to appropriate location in video

### Files to Check for Threshold Values
- `/oni/MAIN/oni-framework/COHERENCE.md`
- `/oni/MAIN/oni-framework/ONI_LAYERS.md`
- `/oni/autodidact/oni-academy/` (course materials)
- `/oni/docs/` (GitHub Pages source)
- `/oni/README.md`

---

## KEY FORMULAS (Verified Correct)

### Coherence Score
```
Cₛ = e^(−(σ²φ + σ²τ + σ²γ))

Where:
- σ²φ = Phase Variance (neural oscillation alignment)
- σ²τ = Timing Variance (temporal jitter precision)
- σ²γ = Frequency Variance (band-specific stability)
```

### Scale-Frequency Invariant
```
f × S ≈ k

Where:
- f = Frequency (Hz)
- S = Scale
- k = Invariant constant

As scale increases, frequency decreases proportionally.
The product remains constant - a fingerprint of healthy neural activity.
```

---

## GIT COMMANDS TO SAVE

Run these commands to commit all changes:

```bash
cd /Users/mac/Documents/PROJECTS/@qikevinl/oni/video/demo

git add src/scenes/TitleScene.tsx
git add src/scenes/ProblemScene.tsx
git add src/scenes/LayersScene.tsx
git add src/scenes/CoherenceScene.tsx
git add src/components/CoherenceGauge.tsx
git add src/data/script.ts
git add SESSION_NOTES.md

git commit -m "ONI Demo Video: Major scene updates and script revisions

Scenes Updated:
- TitleScene: Orbiting electron, solid white ONI, bold NEURO tagline
- ProblemScene: Full-screen ONI Framework reveal with animated gradient
- LayersScene: Complete rewrite with L1-L14 animation, L8 Gateway emphasis
- CoherenceScene: Fixed formula, added Scale-Frequency visualization

Formula Corrections:
- Coherence: Cₛ = e^(−(σ²φ + σ²τ + σ²γ))
- Scale-Frequency: f × S ≈ k

Script Updates:
- Added threshold/defense mechanism narration
- Removed '100% open source' from TARA section
- Extended '...and you' for emphasis
- Adjusted timing to ~3:53 runtime

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"

git push origin main
```

---

## NEXT SESSION CHECKLIST

1. [ ] Find coherence threshold value in docs
2. [ ] Implement threshold defense visualization
3. [ ] Update header to "ONI Neural Security Suite"
4. [ ] Create "...and you" pan-in animation
5. [ ] Remove TARA open source text from scene
6. [ ] Create detailed Scale-Frequency visualization
7. [ ] Test all scenes in Remotion Studio
8. [ ] Generate voiceover with ElevenLabs
9. [ ] Final render and GitHub Pages integration

---

*Notes created by Claude Opus 4.5 - Session 2026-01-26*
