# LearnViz - Automated Learning Visualization Pipeline

> **Concept → Code → Video** in one command

An AI-powered pipeline that transforms concept descriptions into educational visualizations using the optimal rendering engine.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        LEARNVIZ PIPELINE                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   [Concept Description]                                          │
│          │                                                       │
│          ▼                                                       │
│   ┌──────────────┐                                               │
│   │   ANALYZER   │ ← Classifies concept type                     │
│   │   (Claude)   │   Selects optimal engine                      │
│   └──────┬───────┘                                               │
│          │                                                       │
│          ├─────────────────┬─────────────────┐                   │
│          ▼                 ▼                 ▼                   │
│   ┌────────────┐   ┌────────────┐   ┌────────────┐               │
│   │   MANIM    │   │  REMOTION  │   │   D3.js    │               │
│   │  Generator │   │  Generator │   │  Generator │               │
│   └─────┬──────┘   └─────┬──────┘   └─────┬──────┘               │
│         │                │                │                      │
│         ▼                ▼                ▼                      │
│   ┌────────────┐   ┌────────────┐   ┌────────────┐               │
│   │   Manim    │   │  Remotion  │   │  Puppeteer │               │
│   │   Render   │   │   Render   │   │   Record   │               │
│   └─────┬──────┘   └─────┬──────┘   └─────┬──────┘               │
│         │                │                │                      │
│         └────────────────┼────────────────┘                      │
│                          ▼                                       │
│                   [MP4/GIF Output]                               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Concept Classification

| Category | Examples | Engine | Why |
|----------|----------|--------|-----|
| **Mathematical** | Pythagorean theorem, derivatives, matrices | Manim | LaTeX, geometric precision |
| **Physics** | Gravity, waves, forces, momentum | Manim | Physics primitives, parametric |
| **Algorithms** | Sorting, trees, graphs, recursion | Manim | Step-by-step animation |
| **Data/Statistics** | Charts, distributions, trends | Remotion | Data-driven, templated |
| **Timelines** | History, processes, workflows | Remotion | Component model |
| **Networks** | Graphs, connections, flows | D3.js | Force layouts |
| **Systems** | Architecture, diagrams | Mermaid→Remotion | Diagram-as-code |

---

## Quick Start

### Prerequisites

```bash
# Manim (for math/physics/algorithms)
pip install manim

# Remotion (for data/timelines)
npm install -g @remotion/cli
npx remotion init

# D3 recording (optional)
npm install puppeteer
```

### Usage

```bash
# Basic usage
python learnviz.py "Explain how binary search works"

# Specify output format
python learnviz.py "Pythagorean theorem proof" --format gif

# Force specific engine
python learnviz.py "Bubble sort" --engine manim

# Interactive mode (step through scenes)
python learnviz.py "Neural network forward propagation" --interactive
```

---

## Pipeline Stages

### Stage 1: Concept Analysis

The analyzer extracts:
- **Type**: What category of concept?
- **Components**: What elements need visualization?
- **Flow**: What's the narrative arc?
- **Complexity**: Simple (1 scene) or multi-part?

### Stage 2: Scene Planning

Generates a structured scene plan:
```json
{
  "title": "Binary Search Algorithm",
  "type": "algorithm",
  "engine": "manim",
  "scenes": [
    {
      "id": 1,
      "name": "setup",
      "description": "Show sorted array with target value",
      "duration": 3
    },
    {
      "id": 2,
      "name": "first_comparison",
      "description": "Compare middle element, highlight",
      "duration": 2
    }
  ]
}
```

### Stage 3: Code Generation

AI generates engine-specific code from the scene plan.

### Stage 4: Rendering

Executes the appropriate render pipeline.

---

## Templates

Pre-built templates for common patterns:

| Template | Use Case | Engine |
|----------|----------|--------|
| `array_visual` | Show array operations | Manim |
| `tree_traversal` | Binary tree animations | Manim |
| `graph_algorithm` | Graph traversal (BFS, DFS) | Manim |
| `function_plot` | Mathematical functions | Manim |
| `proof_steps` | Theorem proofs | Manim |
| `bar_chart_race` | Animated rankings | Remotion |
| `timeline` | Sequential events | Remotion |
| `flowchart` | Process flows | Mermaid→Remotion |
| `network_force` | Network visualization | D3.js |

---

## File Structure

```
learnviz/
├── README.md              # This file
├── learnviz.py            # Main CLI entry point
├── analyzer.py            # Concept classification
├── generators/
│   ├── manim_gen.py       # Manim code generator
│   ├── remotion_gen.py    # Remotion code generator
│   └── d3_gen.py          # D3.js code generator
├── templates/
│   ├── manim/             # Manim scene templates
│   ├── remotion/          # React component templates
│   └── d3/                # D3 visualization templates
├── renderers/
│   ├── manim_render.py    # Manim execution
│   ├── remotion_render.py # Remotion execution
│   └── d3_render.py       # D3 recording
├── output/                # Generated videos
└── tests/                 # Test concepts
```

---

## Example Output

**Input:** `"Explain binary search step by step"`

**Analysis:**
```
Type: algorithm
Engine: manim
Scenes: 5
Duration: ~30 seconds
```

**Generated Code:** See `examples/binary_search.py`

**Output:** `output/binary_search.mp4`

---

## Roadmap

- [x] Architecture design
- [ ] Concept analyzer (Claude integration)
- [ ] Manim code generator
- [ ] Remotion code generator
- [ ] CLI tool
- [ ] Template library (10 common patterns)
- [ ] Voice-over sync
- [ ] Interactive mode

---

## Credits

Built on:
- [Manim Community](https://www.manim.community/) - Mathematical animations
- [Remotion](https://www.remotion.dev/) - React-based video
- [D3.js](https://d3js.org/) - Data visualization
- [3Blue1Brown](https://www.3blue1brown.com/) - Inspiration

---

*Part of the ONI Framework*
