# Neuroscience & BCI Research

> **Purpose:** Personal research and learning repository for neuroscience concepts I need to understand to build the ONI Framework. This is where I figure out things I don't know but need to know.

**This is NOT polished documentation.** It's a working knowledge base for building understanding of the biological substrate that BCIs interface with.

---

## Table of Contents

1. [BCI-Functional Electrode Zone Classification](#bci-functional-electrode-zone-classification)
2. [Kanban](#kanban)
3. [Folder Structure](#folder-structure)
4. [Purpose of Each Folder](#purpose-of-each-folder)
5. [Research Documents](#research-documents)
6. [Key Questions](#key-questions-this-research-aims-to-answer)
7. [Related Projects](#related-projects)
8. [Adding Research](#adding-research)

---

## BCI-Functional Electrode Zone Classification

> **Learning Framework:** Organize brain regions by *what they do* (function) rather than *where they are* (anatomy). This is more practical for understanding electrode placement and BCI security.

### The 10 Key BCI Electrode Zones

| Region | Full Name | ONI Layer | Function | BCI Access | MNI Coords |
|--------|-----------|-----------|----------|------------|------------|
| **M1** | Primary Motor Cortex | L13 (Semantic) | MOTOR | High | (-35,-20,55) |
| **S1** | Primary Somatosensory Cortex | L12 (Session) | SENSORY | High | (-35,-35,50) |
| **PMC** | Premotor Cortex | L13 (Semantic) | EXECUTIVE | High | (-45,5,50) |
| **SMA** | Supplementary Motor Area | L13 (Semantic) | EXECUTIVE | High | (0,-5,60) |
| **PFC** | Prefrontal Cortex | L14 (Identity) | COGNITIVE | High | (35,45,25) |
| **BROCA** | Broca's Area | L14 (Identity) | LANGUAGE | Medium | (-50,20,15) |
| **WERNICKE** | Wernicke's Area | L14 (Identity) | LANGUAGE | Medium | (-55,-55,20) |
| **V1** | Primary Visual Cortex | L12 (Session) | VISUAL | High | (0,-85,5) |
| **A1** | Primary Auditory Cortex | L12 (Session) | AUDITORY | High | (-55,-20,10) |
| **HIPP** | Hippocampus | L11 (Transport) | MEMORY | Medium | (-25,-20,-15) |

### Understanding the Two Classifications

| Classification | What It Tells You | Example |
|----------------|-------------------|---------|
| **ONI Layer** | Functional role in cognitive stack | M1 = L13 (translates intent → motor commands) |
| **BCI Access** | Physical accessibility to electrodes | M1 = High (surface cortex, easy to reach) |

These are **orthogonal** — a region can be L13 (high-level function) but still have High BCI access (easy to reach physically).

---

### Why M1 is L13 (Semantic) Despite High BCI Access

> **Key Insight:** ONI Layer refers to *functional depth* in information processing, not *physical depth* in the brain.

#### The Apparent Paradox

At first glance, it seems contradictory:
- M1 is mapped to **L13 (Semantic Layer)** — a high-level cognitive layer
- M1 has **High BCI Access** — it's on the cortical surface, easy to reach

**This is not a contradiction.** These measure different things:

| Dimension | What It Measures | M1's Position |
|-----------|------------------|---------------|
| **Physical Depth** | Millimeters from skull surface | ~2-4mm (very shallow) |
| **Functional Depth** | Position in information processing hierarchy | High (semantic translation) |

#### The Motor Control Hierarchy

Motor control follows a hierarchical processing cascade (Kandel et al., 2021):

```
L14 (Identity)     PFC: "I want to pick up that cup"
        ↓                    (goal formation, self-model)
L13 (Semantic)     PMC/SMA → M1: "Reach, grasp, lift"
        ↓                    (intent → motor plan → muscle commands)
L12 (Session)      Cerebellum/Basal Ganglia: Timing, coordination
        ↓                    (motor learning, error correction)
L11 (Transport)    Spinal cord: Execute movement
        ↓                    (final motor neuron activation)
        ↓
                   Muscles contract
```

**M1 sits at the semantic boundary** — it's where abstract intentions ("move hand left") get translated into specific neural firing patterns that encode muscle activations. This is *meaning construction* in the motor domain.

#### Scientific Evidence for M1's Semantic Role

1. **Population Coding of Movement Direction**

   Georgopoulos et al. (1986) discovered that M1 neurons encode movement *direction* as a population vector, not individual muscle activations. This means M1 represents the *meaning* of movement (where to go), not just motor commands.

   > "The population vector provides an accurate prediction of movement direction... suggesting that the motor cortex encodes movement parameters at a relatively abstract level."
   > — Georgopoulos, A. P., Schwartz, A. B., & Kettner, R. E. (1986). *Science*, 233(4771), 1416-1419.

2. **Motor Imagery Activates M1**

   Functional imaging studies show M1 activates during *imagined* movement, not just executed movement (Ehrsson et al., 2003). This demonstrates M1's role in representing motor *intent*, not just motor *output*.

   > "Primary motor cortex is activated during motor imagery... supporting the view that M1 is involved in higher-order aspects of motor control."
   > — Ehrsson, H. H., et al. (2003). *Journal of Neurophysiology*, 90(5), 3304-3316.

3. **BCI Decoding Reveals Semantic Content**

   Modern BCIs decode *intended* movements from M1, including movements the patient cannot physically execute (Hochberg et al., 2012). This proves M1 encodes semantic intent, not just muscle commands.

   > "Neural signals from motor cortex can be decoded to determine intended movement... even in patients with tetraplegia who cannot move their limbs."
   > — Hochberg, L. R., et al. (2012). *Nature*, 485(7398), 372-375.

4. **Hierarchical Motor Processing**

   Rizzolatti & Luppino (2001) established that motor cortex is organized hierarchically, with M1 receiving already-processed motor plans from premotor areas:

   > "M1 is not simply the final common pathway for motor commands, but participates in the transformation of motor plans into executable commands."
   > — Rizzolatti, G., & Luppino, G. (2001). *Neuron*, 31(6), 889-901.

#### Why BCI Access is High Despite L13

| Factor | Explanation |
|--------|-------------|
| **Surface location** | M1 is in the precentral gyrus, directly accessible from the skull |
| **Clear somatotopy** | Motor homunculus provides predictable electrode placement |
| **High signal quality** | Large pyramidal neurons produce strong, decodable signals |
| **Decades of research** | Well-characterized, extensive mapping studies |

The motor homunculus (Penfield & Boldrey, 1937) maps specific body parts to specific M1 locations, making electrode targeting straightforward:

```
M1 Somatotopic Organization (Lateral to Medial):
┌─────────────────────────────────────────────────┐
│  Tongue  Face  Hand  Arm  Trunk  Leg  Foot     │
│    ↓      ↓     ↓     ↓     ↓     ↓     ↓      │
│  Lateral ←─────────────────────────→ Medial    │
└─────────────────────────────────────────────────┘
```

#### The Key Distinction

| Concept | Definition | Analogy |
|---------|------------|---------|
| **Functional Depth** | How many processing stages from raw input/output | CEO (high) vs assembly line worker (low) |
| **Physical Depth** | Distance from brain surface in mm | Corner office (surface) vs basement (deep) |

**M1 is like a CEO who works in a ground-floor corner office** — high in the organizational hierarchy (L13), but physically accessible (High BCI Access).

#### Contrast with Deep Brain Structures

| Region | ONI Layer | BCI Access | Physical Depth | Functional Role |
|--------|-----------|------------|----------------|-----------------|
| M1 | L13 (Semantic) | High | 2-4mm | Intent → motor commands |
| VTA | L12-L13 | Low | 70-80mm | Reward, motivation |
| Hippocampus | L11 | Medium | 40-50mm | Memory consolidation |

VTA (Ventral Tegmental Area) is both functionally deep (L12-L13) AND physically deep (70-80mm). M1 is functionally deep but physically shallow.

#### References

- Georgopoulos, A. P., Schwartz, A. B., & Kettner, R. E. (1986). Neuronal population coding of movement direction. *Science*, 233(4771), 1416-1419. https://doi.org/10.1126/science.3749885
- Ehrsson, H. H., Geyer, S., & Naito, E. (2003). Imagery of voluntary movement of fingers, toes, and tongue activates corresponding body-part-specific motor representations. *Journal of Neurophysiology*, 90(5), 3304-3316. https://doi.org/10.1152/jn.01113.2002
- Hochberg, L. R., et al. (2012). Reach and grasp by people with tetraplegia using a neurally controlled robotic arm. *Nature*, 485(7398), 372-375. https://doi.org/10.1038/nature11076
- Rizzolatti, G., & Luppino, G. (2001). The cortical motor system. *Neuron*, 31(6), 889-901. https://doi.org/10.1016/S0896-6273(01)00423-8
- Penfield, W., & Boldrey, E. (1937). Somatic motor and sensory representation in the cerebral cortex of man as studied by electrical stimulation. *Brain*, 60(4), 389-443.
- Kandel, E. R., et al. (2021). *Principles of Neural Science* (6th ed.). McGraw-Hill.

---

### ONI Layer Mappings for All 10 Regions

The same functional-vs-physical principle applies to all BCI electrode zones. Here's why each region maps to its ONI layer:

#### L14 (Identity Layer) — Self, Language, Executive Control

> **L14 Definition:** The highest cognitive layer dealing with self-model, ethics, personal identity, and language that shapes thought.

| Region | Why L14? | Scientific Basis |
|--------|----------|------------------|
| **PFC** (Prefrontal Cortex) | Seat of executive function, self-awareness, and decision-making. Contains the neural substrate for "who you are" | Miller & Cohen (2001): PFC provides top-down control of behavior based on goals and rules. Damage causes personality changes, impaired judgment, loss of self-regulation. |
| **BROCA** (Broca's Area) | Speech *production* — transforms thoughts into language. Language shapes identity and enables self-narrative | Broca (1861): Lesions cause expressive aphasia. Fedorenko et al. (2011): Broca's is critical for syntactic processing, not just speech output. |
| **WERNICKE** (Wernicke's Area) | Speech *comprehension* — extracts meaning from language. Understanding language is fundamental to social identity | Wernicke (1874): Lesions cause receptive aphasia. Hickok & Poeppel (2007): Dual-stream model shows Wernicke's in semantic processing pathway. |

**Why L14 for language?** Language is uniquely human and central to identity. The ability to name oneself, narrate one's life, and communicate thoughts is foundational to personhood. Attacks on L14 (language areas) could alter how a person expresses or understands their own identity.

> "The prefrontal cortex represents the biological substrate of the human capacity to form a sense of self."
> — Miller, E. K., & Cohen, J. D. (2001). *Annual Review of Neuroscience*, 24, 167-202.

---

#### L13 (Semantic Layer) — Intent, Meaning Construction, Motor Planning

> **L13 Definition:** Where abstract intentions get translated into meaningful actions. The bridge between "what I want" and "how to do it."

| Region | Why L13? | Scientific Basis |
|--------|----------|------------------|
| **M1** (Primary Motor Cortex) | Translates motor *intent* into specific movement commands. Encodes movement direction, not individual muscles | Georgopoulos et al. (1986): Population coding shows M1 represents movement meaning, not just muscle activation. See detailed section above. |
| **PMC** (Premotor Cortex) | Plans movements before execution. Encodes *what* action to perform based on context | Wise et al. (1997): PMC neurons encode action selection based on sensory cues. "Premotor cortex is involved in selecting movements, not just preparing them." |
| **SMA** (Supplementary Motor Area) | Sequences complex movements and internally-generated actions. The "choreographer" of movement | Tanji (2001): SMA is critical for organizing sequential movements and self-initiated (vs externally-triggered) actions. |

**Why L13 for motor areas?** These regions don't just fire muscles — they *interpret intent* and *construct meaning* in the motor domain. BCIs decode "move cursor left" from M1, not "contract bicep" — that's semantic-level information.

> "The premotor areas are involved in the cognitive aspects of motor control: selecting actions, planning sequences, and preparing movements based on context."
> — Wise, S. P., et al. (1997). *Annual Review of Neuroscience*, 20, 25-42.

---

#### L12 (Cognitive Session Layer) — Perception, Context, Working Memory

> **L12 Definition:** Maintains perceptual context and working memory. Where sensory streams become coherent experiences.

| Region | Why L12? | Scientific Basis |
|--------|----------|------------------|
| **S1** (Primary Somatosensory Cortex) | Integrates touch into body awareness. Maintains "body schema" — where your limbs are in space | Penfield & Boldrey (1937): Somatotopic organization. Graziano & Botvinick (2002): S1 contributes to body representation, not just touch detection. |
| **V1** (Primary Visual Cortex) | First cortical processing of visual input. Constructs the visual "session" — what you're currently seeing | Hubel & Wiesel (1962, Nobel Prize): V1 extracts edges, orientation, motion — building blocks of visual perception. |
| **A1** (Primary Auditory Cortex) | First cortical processing of sound. Maintains auditory "session" — the soundscape you're experiencing | Kaas & Hackett (2000): A1 creates tonotopic representation, the foundation of auditory perception and context. |

**Why L12 for sensory cortices?** These regions don't just relay signals — they *construct perceptual sessions*. V1 creates your visual experience, S1 creates your body awareness, A1 creates your auditory world. They maintain the *context* in which higher cognition operates.

> "Primary sensory cortices are not passive relays but active constructors of perceptual reality."
> — Kandel, E. R., et al. (2021). *Principles of Neural Science* (6th ed.).

---

#### L11 (Cognitive Transport Layer) — Memory Consolidation, Information Routing

> **L11 Definition:** Reliable transport of cognitive information across time (memory) and brain regions (routing).

| Region | Why L11? | Scientific Basis |
|--------|----------|------------------|
| **HIPP** (Hippocampus) | Consolidates short-term → long-term memory. The "router" that sends memories to cortex for permanent storage | Squire & Zola-Morgan (1991): Hippocampal damage prevents new memory formation. Buzsáki (2015): Hippocampal sharp-wave ripples "transport" memories to cortex during sleep. |

**Why L11 for hippocampus?** The hippocampus is literally a *transport system* for memories. It receives information from all sensory modalities, binds them into episodic memories, and routes them to cortical storage. It ensures *reliable delivery* of cognitive content across time.

> "The hippocampus acts as a temporary memory store, consolidating and transferring information to the neocortex for permanent storage."
> — Squire, L. R., & Zola-Morgan, S. (1991). *Science*, 253(5026), 1380-1386.

---

### Summary: ONI Layer Mapping Logic

| ONI Layer | Cognitive Function | Brain Regions | Key Principle |
|-----------|-------------------|---------------|---------------|
| **L14** (Identity) | Self-model, language, executive control | PFC, BROCA, WERNICKE | "Who am I and what do I want?" |
| **L13** (Semantic) | Intent → action translation, meaning construction | M1, PMC, SMA | "What does this mean and how do I do it?" |
| **L12** (Session) | Perceptual context, working memory | S1, V1, A1 | "What am I experiencing right now?" |
| **L11** (Transport) | Memory routing, information consolidation | HIPP | "How do I store and retrieve this?" |

---

### Additional References for Layer Mappings

- Miller, E. K., & Cohen, J. D. (2001). An integrative theory of prefrontal cortex function. *Annual Review of Neuroscience*, 24, 167-202. https://doi.org/10.1146/annurev.neuro.24.1.167
- Fedorenko, E., et al. (2011). Functional specificity for high-level linguistic processing in the human brain. *PNAS*, 108(39), 16428-16433.
- Hickok, G., & Poeppel, D. (2007). The cortical organization of speech processing. *Nature Reviews Neuroscience*, 8(5), 393-402.
- Wise, S. P., et al. (1997). Premotor and parietal cortex: Corticocortical connectivity and combinatorial computations. *Annual Review of Neuroscience*, 20, 25-42.
- Tanji, J. (2001). Sequential organization of multiple movements: Involvement of cortical motor areas. *Annual Review of Neuroscience*, 24, 631-651.
- Graziano, M. S., & Botvinick, M. M. (2002). How the brain represents the body: Insights from neurophysiology and psychology. *Common Mechanisms in Perception and Action*, 136-157.
- Hubel, D. H., & Wiesel, T. N. (1962). Receptive fields, binocular interaction and functional architecture in the cat's visual cortex. *Journal of Physiology*, 160(1), 106-154.
- Kaas, J. H., & Hackett, T. A. (2000). Subdivisions of auditory cortex and processing streams in primates. *PNAS*, 97(22), 11793-11799.
- Squire, L. R., & Zola-Morgan, S. (1991). The medial temporal lobe memory system. *Science*, 253(5026), 1380-1386.
- Buzsáki, G. (2015). Hippocampal sharp wave-ripple: A cognitive biomarker for episodic memory and planning. *Hippocampus*, 25(10), 1073-1188.

---

### BCI Access Levels

| Level | Meaning | Regions |
|-------|---------|---------|
| **High** | Surface cortex, well-characterized, primary BCI targets | M1, S1, PMC, SMA, PFC, V1, A1 |
| **Medium** | Deeper or more complex access requirements | BROCA, WERNICKE, HIPP |
| **Low** | Deep brain structures, specialized electrodes needed | SNc, VTA, NAc, LC, Raphe |
| **None** | Too deep or risky for current BCI technology | VLPO, LHA |

### Source Files

- **TARA:** `MAIN/tara-nsec-platform/tara_mvp/data/brain_regions.py`
- **ONI Framework:** `MAIN/oni-framework/oni/neuromapping.py`

---

## Kanban

### Backlog
| Task | Description | Priority |
|------|-------------|----------|
| Motor cortex deep dive | Understand electrode placement, neural decoding | High |
| Neurotransmitter systems | DA, 5-HT, NE pathways and cofactors | High |
| BCI-to-neuron zoom animation | Blender/Manim visualization project | Medium |
| Synaptic transmission | How signals cross synapses | Medium |
| Ion channel mechanics | Na+/K+ channels, action potentials | Low |

### In Progress
| Task | Description | Notes |
|------|-------------|-------|
| BCI Mouse Movement | How BCIs decode motor signals | See Research-BCI_Mouse_Movement.md |

### Done
| Task | Completed | Output |
|------|-----------|--------|
| Initial folder structure | 2026-01-26 | Brain region folders created |
| Visualization assets collected | 2026-01-26 | visualizing-the-mind/ |

---

## Folder Structure

```
neuroscience-homework-todo/
├── README.md                           # This file
├── Research-BCI_Mouse_Movement.md      # How BCIs enable cursor/keyboard control
│
├── visualizing-the-mind/               # BCI macro-to-micro zoom animations
│   ├── README.md                       # Project objectives and overview
│   ├── 3D-mindmapper/                  # 3D visualization (Blender)
│   │   └── blender/bci-zoom-3d/        # Photorealistic zoom animation
│   └── 2D-mindmapper/                  # 2D visualization (Manim)
│       └── manim/bci-zoom/             # Scientific dual-axis animation
│
├── bci-electrode-zones/                # ═══ BCI-FUNCTIONAL CLASSIFICATION ═══
│   ├── motor/                          # Movement control
│   │   └── M1 - Primary Motor Cortex/
│   │
│   ├── sensory/                        # Touch, proprioception
│   │   └── S1 - Primary Somatosensory Cortex/
│   │
│   ├── cognitive/                      # Executive function, decision-making
│   │   └── PFC - Prefrontal Cortex/
│   │
│   ├── language/                       # Speech production and comprehension
│   │   ├── BROCA - Broca's Area/
│   │   └── WERNICKE - Wernicke's Area/
│   │
│   ├── visual/                         # Vision processing
│   │   └── V1 - Primary Visual Cortex/
│   │
│   ├── auditory/                       # Hearing processing
│   │   └── A1 - Primary Auditory Cortex/
│   │
│   ├── memory/                         # Memory formation and retrieval
│   │   └── HIPP - Hippocampus/
│   │
│   └── executive/                      # Motor planning and coordination
│       ├── PMC - Premotor Cortex/
│       └── SMA - Supplementary Motor Area/
│
└── brain-regions/                      # ═══ ANATOMICAL CLASSIFICATION ═══
    ├── cerebral-cortex/                # Outer brain layer (higher functions)
    │   ├── motor-cortex/               # Movement control (BCI primary target)
    │   ├── sensory-cortex/             # Touch, proprioception
    │   ├── prefrontal-cortex/          # Executive function, planning
    │   ├── visual-cortex/              # Vision processing
    │   ├── auditory-cortex/            # Hearing processing
    │   └── parietal-cortex/            # Spatial awareness, integration
    │
    ├── cerebellum/                     # Movement coordination, balance
    │
    ├── brainstem/                      # Vital functions
    │   ├── medulla/                    # Heart rate, breathing
    │   ├── pons/                       # Sleep, arousal
    │   └── midbrain/                   # Eye movement, hearing
    │
    ├── limbic-system/                  # Emotion, memory
    │   ├── amygdala/                   # Fear, emotion processing
    │   ├── hippocampus/                # Memory formation
    │   └── cingulate-cortex/           # Decision-making, emotion
    │
    ├── thalamus/                       # Sensory relay station
    ├── hypothalamus/                   # Hormones, homeostasis
    ├── basal-ganglia/                  # Movement initiation, habits
    ├── corpus-callosum/                # Hemispheric communication
    └── neural-pathways/                # Major fiber tracts
```

---

## Purpose of Each Folder

### Two Classification Systems

| Folder | Organization | Best For |
|--------|--------------|----------|
| **bci-electrode-zones/** | By function (what it does) | Learning BCI electrode placement, security analysis |
| **brain-regions/** | By anatomy (where it is) | Understanding brain structure, neuroscience foundations |

### What Goes in Each Region Folder

1. **How it works** — Function, anatomy, connections
2. **Research notes** — Papers, findings, key facts
3. **Questions** — Things to ask researchers/professionals
4. **Unknowns** — What science hasn't figured out yet
5. **BCI relevance** — How this region relates to brain-computer interfaces
6. **Security implications** — Potential vulnerabilities, attack surfaces
7. **ONI layer mapping** — Which layer(s) this region maps to

---

## Research Documents

| Document | Description |
|----------|-------------|
| [Research-BCI_Mouse_Movement.md](./Research-BCI_Mouse_Movement.md) | Deep dive on how BCIs decode motor cortex signals for cursor control |

---

## Key Questions This Research Aims to Answer

1. Where exactly do BCI electrodes sit in the brain?
2. How deep do they go?
3. What signals do they record?
4. How are those signals decoded into actions?
5. What are the current technological limitations?
6. What questions remain unanswered in the field?

---

## Related Projects

- **Visualizations:** [visualizing-the-mind/](./visualizing-the-mind/) — Blender and Manim visualization projects
- **Backlog:** [bci-to-neuron-zoom-rendering](../docs/visualizations/pending/bci-to-neuron-zoom-rendering/) — GitHub Pages pending visualization
- **Video Assets:** `video/bci-zoom/` — Video project files
- **ONI_LAYERS.md:** Biological Foundation section — How this maps to L8-L14
- **oni/neuromapping.py:** Python API for brain region → layer mappings

---

## Adding Research

When adding research to a brain region folder:

1. Create a file named `Notes-[Topic].md` for informal notes
2. Create `Research-[Topic].md` for structured research
3. Include sources with links
4. Tag questions with `[Q]` prefix
5. Tag unknowns with `[?]` prefix

Example:
```markdown
## Motor Cortex Notes

[Q] Why do some neurons respond to imagined movement but not actual movement?

[?] Unknown: The exact mechanism by which motor cortex neurons "know" whether movement is intended vs executed.

Source: Smith et al. (2023) - https://example.com/paper
```

---

*Last Updated: 2026-01-26*
