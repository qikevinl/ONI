# Autodidact

> **Ultimate Goal:** Build a self-directed learning system that adapts to how each individual learns — making complex knowledge accessible through personalized visualizations, pacing, and pathways.

The `autodidact` module is the educational arm of the ONI Framework. It's not just documentation — it's a living system for learning and teaching neurosecurity concepts, built on the principle that **education should adapt to the learner, not the other way around**.

---

## The Vision

```
┌─────────────────────────────────────────────────────────────────┐
│                    AUTODIDACT ECOSYSTEM                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │                   LEARNER PROFILE                        │   │
│   │   • Learning style (visual/verbal/kinesthetic)          │   │
│   │   • Pace & comprehension tracking                       │   │
│   │   • Knowledge graph (what you already know)             │   │
│   │   • Preferences (animation speed, detail level)         │   │
│   └─────────────────────────────────────────────────────────┘   │
│                            │                                    │
│                            ▼                                    │
│   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐          │
│   │  LEARNVIZ   │   │ ONI ACADEMY │   │ NEUROSCIENCE│          │
│   │  Adaptive   │◀──│  Structured │◀──│   RESEARCH  │          │
│   │  Visuals    │   │  Curriculum │   │  Foundation │          │
│   └─────────────┘   └─────────────┘   └─────────────┘          │
│         │                 │                 │                   │
│         └─────────────────┼─────────────────┘                   │
│                           ▼                                     │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │              PERSONALIZED LEARNING PATH                 │   │
│   │   • Auto-adjusting difficulty                           │   │
│   │   • Visualizations tailored to your style               │   │
│   │   • Pacing based on your comprehension                  │   │
│   │   • Prerequisites auto-detected from knowledge graph    │   │
│   └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│   [100% Local — Your learning data never leaves your machine]   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Components

### 1. LearnViz — Adaptive Visualization Engine

**Purpose:** Generate educational visualizations that adapt to individual learning behaviors.

**Current (v0.1):**
- Concept → Code → Video pipeline
- Pattern-based concept classification
- 4 Manim templates (binary search, sorting, Pythagorean, trees)
- Local rendering with Manim

**Future (v0.4+):**
- Learner profiles with style/pace tracking
- Visualizations that adjust to YOUR learning patterns
- Local LLM integration for custom explanations
- Interactive mode with Q&A

**Location:** [`learnviz/`](./learnviz/)

```bash
# Example usage
cd learnviz
python learnviz.py "Explain binary search" --render
```

---

### 2. ONI Academy — Structured Curriculum

**Purpose:** Provide structured learning paths for neurosecurity concepts, from basics to advanced.

**What it offers:**
- Learning modules (14-layer model, coherence metric, neural firewall, etc.)
- Interactive web tools (no installation required)
- Python API for programmatic access
- CLI for quick exploration

**Location:** [`oni-academy/`](./oni-academy/)

```bash
# Install
pip install oni-academy

# List modules
oni-academy list

# Launch UI
oni-academy ui
```

**Web Tools (no install):**
- [Coherence Metric Playground](https://qikevinl.github.io/ONI/visualizations/01-coherence-metric-playground.html)
- [ONI Layer Explorer](https://qikevinl.github.io/ONI/visualizations/02-oni-layer-explorer.html)
- [NSAM Checkpoint Simulator](https://qikevinl.github.io/ONI/visualizations/04-nsam-checkpoint-simulator.html)

---

### 3. Neuroscience-BCI — Research Foundation

**Purpose:** Personal research repository for understanding the biological substrate that BCIs interface with.

**What it contains:**
- Brain region documentation (motor cortex, limbic system, etc.)
- BCI research notes (how electrodes work, signal decoding)
- Visualization projects (Blender 3D, Manim 2D)
- Key questions the research aims to answer

**Location:** [`neuroscience-bci/`](./neuroscience-bci/)

**Why it matters:** You can't secure what you don't understand. This research feeds directly into ONI Academy content and LearnViz visualizations.

---

## How They Align

```
┌──────────────────────────────────────────────────────────────────┐
│                     KNOWLEDGE FLOW                               │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│   NEUROSCIENCE-BCI                                               │
│   ┌────────────────────────────┐                                 │
│   │ • Raw research notes       │                                 │
│   │ • Brain region anatomy     │                                 │
│   │ • "Figure out what I       │                                 │
│   │    don't know"             │                                 │
│   └────────────┬───────────────┘                                 │
│                │ (research matures into curriculum)              │
│                ▼                                                 │
│   ONI ACADEMY                                                    │
│   ┌────────────────────────────┐                                 │
│   │ • Structured modules       │                                 │
│   │ • Learning paths           │                                 │
│   │ • Interactive web tools    │                                 │
│   │ • pip-installable package  │                                 │
│   └────────────┬───────────────┘                                 │
│                │ (curriculum generates visualizations)           │
│                ▼                                                 │
│   LEARNVIZ                                                       │
│   ┌────────────────────────────┐                                 │
│   │ • Adaptive visualizations  │                                 │
│   │ • Learner profiles         │                                 │
│   │ • Custom pacing/style      │                                 │
│   │ • Local-first, private     │                                 │
│   └────────────────────────────┘                                 │
│                                                                  │
│   ════════════════════════════════════════════════════           │
│   ULTIMATE OUTPUT: Personalized learning experience              │
│   that adapts to each individual's cognitive patterns            │
│   ════════════════════════════════════════════════════           │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### The Feedback Loop

| Stage | Input | Output | Next Stage Uses |
|-------|-------|--------|-----------------|
| **Research** (neuroscience-bci) | Papers, questions, unknowns | Documented knowledge | Academy curriculum |
| **Curriculum** (oni-academy) | Documented knowledge | Structured learning modules | LearnViz topics |
| **Visualization** (learnviz) | Topics + learner profile | Adaptive animations | Learner comprehension |
| **Profile Update** | Comprehension data | Updated learner model | Better visualizations |

---

## Design Principles

### 1. Local-First

All computation and learner data stays on your machine:
- No cloud dependency
- Works offline
- You own your learning data
- Privacy by default

### 2. Adaptive by Default

Every component eventually adapts to the learner:
- Pace: How fast you comprehend
- Style: Visual vs verbal vs kinesthetic
- Depth: Beginner-friendly or expert-level
- History: Skip what you already know

### 3. Open & Extensible

- Add your own research to neuroscience-bci
- Contribute modules to oni-academy
- Create templates for learnviz
- All Apache 2.0 licensed

### 4. Research → Curriculum → Visualization

Knowledge flows from raw research to structured curriculum to adaptive visualizations. Each stage builds on the previous.

---

## Roadmap

### Phase 1: Foundation ✅
- [x] ONI Academy pip package with learning modules
- [x] Interactive web tools (browser-based)
- [x] Neuroscience research repository structure
- [x] LearnViz v0.1 (concept → video pipeline)

### Phase 2: Content Expansion
- [ ] More LearnViz templates (graphs, recursion, physics)
- [ ] Expanded ONI Academy modules
- [ ] Brain region deep dives (motor cortex → full)
- [ ] Cross-linking between components

### Phase 3: LLM Integration
- [ ] Local LLM for custom LearnViz scenes
- [ ] AI tutoring in ONI Academy
- [ ] Research synthesis assistance
- [ ] Natural language → visualization

### Phase 4: Adaptive Learning ⭐ Core Goal
- [ ] Learner profile implementation
- [ ] Pace/style tracking
- [ ] Knowledge graph per user
- [ ] Auto-adjusting difficulty
- [ ] Personalized learning paths

### Phase 5: Full Integration
- [ ] LearnViz ↔ Academy deep integration
- [ ] Research notes auto-generate curriculum
- [ ] Community template sharing (opt-in)
- [ ] Cross-platform sync (still local-first)

---

## File Structure

```
autodidact/
├── README.md                    # This file — ecosystem overview
│
├── learnviz/                    # Adaptive visualization engine
│   ├── README.md                # Vision, implementation, roadmap
│   ├── learnviz.py              # CLI orchestrator
│   ├── analyzer.py              # Concept classification
│   ├── generators/              # Code generators (Manim, Remotion, D3)
│   └── output/                  # Generated scripts
│
├── oni-academy/                 # Structured learning platform
│   ├── README.md                # Package documentation
│   ├── ONI_ACADEMY.md           # Full curriculum guide
│   ├── oni_academy/             # Python package source
│   └── tests/                   # Unit tests
│
├── neuroscience-bci/            # Research foundation
│   ├── README.md                # Research roadmap
│   ├── brain-regions/           # Anatomical documentation
│   │   ├── cerebral-cortex/     # Motor, sensory, visual, etc.
│   │   ├── limbic-system/       # Amygdala, hippocampus
│   │   └── ...                  # Other regions
│   └── visualizing-the-mind/    # BCI zoom animations
│       ├── 3D-mindmapper/       # Blender renders
│       └── 2D-mindmapper/       # Manim animations
│
└── neuroscience-homework-todo/  # Active research tasks
```

---

## Getting Started

### For Learning

```bash
# Install ONI Academy
pip install oni-academy

# Explore modules
oni-academy list
oni-academy ui
```

Or just use the [web tools](https://qikevinl.github.io/ONI/visualizations/) — no installation required.

### For Creating Visualizations

```bash
cd autodidact/learnviz

# Install Manim
pip install manim

# Generate a visualization
python learnviz.py "Binary search algorithm" --render
```

### For Contributing Research

1. Add notes to `neuroscience-bci/brain-regions/[region]/`
2. Use `Notes-[Topic].md` for informal notes
3. Use `Research-[Topic].md` for structured research
4. Tag questions with `[Q]` and unknowns with `[?]`

---

## Philosophy

> *"The best teacher adapts to the student, not the other way around."*

Traditional education assumes everyone learns the same way. Autodidact rejects this assumption. By tracking how you learn — your pace, your preferred modalities, what you already know — we can generate educational experiences tailored specifically to you.

This isn't about replacing teachers. It's about augmenting self-directed learning with tools that understand your unique cognitive patterns.

**The ultimate goal:** Anyone, anywhere, can learn neurosecurity concepts at their own pace, in their own style, without barriers.

---

## Related

- [ONI Framework](../MAIN/) — The security framework these tools teach
- [TARA Platform](../MAIN/tara-nsec-platform/) — Security monitoring & simulation
- [GitHub Pages](https://qikevinl.github.io/ONI/) — Live interactive tools

---

*Part of the ONI Framework*

> *"Autodidact: Learn how you learn, then learn faster."*
