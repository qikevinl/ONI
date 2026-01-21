# ONI Framework Publishing Instructions

## Overview

This document provides standardized instructions for Claude to follow when extracting, formatting, and uploading new content publications to the ONI Framework repository.

---

## Repository Structure

```
MAIN/
└── publications/
    ├── PAPER_TEMPLATE_APA.md          # APA formatting template
    ├── PUBLISHING_INSTRUCTIONS.md     # This file
    ├── coherence-metric/
    │   ├── Medium-Coherence_Metric.md
    │   └── Coherence_Metric_Detailed_Paper.md
    ├── neural-firewall/
    │   ├── Medium-Neural_Firewall.md
    │   └── Neural_Firewall_Architecture_Paper.md
    ├── neural-ransomware/
    │   ├── Medium-Neural_Ransomware.md
    │   └── Neural_Ransomware_Paper.md
    ├── oni-framework/
    │   ├── Medium-ONI_Framework.md
    │   └── The Organic Network Interface (ONI) Framework.md
    └── scale-frequency/
        ├── Medium-Scale_Frequency.md
        └── Scale_Frequency_Paper.md
```

---

## File Naming Conventions

### Medium Posts
- Format: `Medium-[Topic_Name].md`
- Examples:
  - `Medium-Coherence_Metric.md`
  - `Medium-Neural_Firewall.md`
  - `Medium-Scale_Frequency.md`

### Technical Papers
- Format: `[Topic_Name]_Paper.md` or `[Topic_Name]_Detailed_Paper.md`
- Examples:
  - `Neural_Ransomware_Paper.md`
  - `Coherence_Metric_Detailed_Paper.md`

### Folder Names
- Use lowercase with hyphens
- Descriptive of the topic
- Examples: `coherence-metric`, `neural-firewall`, `scale-frequency`

---

## Content Types

### 1. Medium Posts (`Medium-*.md`)
**Purpose:** Accessible, engaging content for general audience publication on Medium.

**Characteristics:**
- Conversational tone
- Uses storytelling and analogies
- Shorter paragraphs for web readability
- Includes section breaks (`• • •` or `---`)
- 5-15 minute read time (1,500-4,000 words)

**Required Front Matter:**
```yaml
---
title: "Article Title"
date: [Publication date in RFC 2822 format]
url: [Medium URL if published]
tags: ['tag1', 'tag2', 'tag3']
---
```

### 2. Technical Papers (`*_Paper.md`)
**Purpose:** Rigorous academic-style documentation with full citations and mathematical detail.

**Characteristics:**
- Formal academic tone
- APA 7th edition formatting (see PAPER_TEMPLATE_APA.md)
- Detailed mathematical formulations
- Comprehensive references section
- Tables with bold numbers, italic titles

**Required Sections:**
1. Abstract (with keywords)
2. Introduction
3. [Methods/Framework/Analysis sections]
4. Discussion
5. Limitations
6. Future Work
7. Conclusion
8. References
9. Acknowledgments

---

## Publishing Workflow

### Step 1: Content Extraction
When extracting content from a new source:

1. **Identify the source type:**
   - Medium RSS feed
   - Draft document
   - Conversation notes
   - Research synthesis

2. **Determine publication category:**
   - Which existing topic folder does this belong to?
   - Does it require a new topic folder?

3. **Extract and clean:**
   - Remove conversion artifacts
   - Fix encoding issues (em-dashes, quotes, etc.)
   - Preserve meaningful formatting

### Step 2: Formatting

**For Medium Posts:**
```markdown
---
title: "[Title]"
date: [Date]
url: [URL if available]
tags: ['tag1', 'tag2']
---

# [Title]

## [Subtitle if applicable]

[Content with proper markdown formatting]
```

**For Technical Papers:**
- Follow `PAPER_TEMPLATE_APA.md` exactly
- Use bold table numbers: `**Table 1**`
- Use italic table titles: `*Table Title*`
- Include standard acknowledgments

### Step 3: Quality Checks

Before committing:

1. **Verify file naming:**
   - Medium files: `Medium-[Topic].md`
   - Papers: `[Topic]_Paper.md`

2. **Check formatting consistency:**
   - Tables formatted correctly
   - Headers hierarchy proper
   - No orphaned formatting

3. **Validate references:**
   - APA format for papers
   - Working URLs where applicable

4. **Review acknowledgments:**
   - Use standard acknowledgments text from template

### Step 4: Commit and Push

```bash
git add .
git commit -m "Add [Topic] publication

- [Brief description of content]
- [Type: Medium/Paper/Both]

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>"

git push
```

---

## Standard Acknowledgments

Include this in all technical papers:

> The author wishes to acknowledge the support of colleagues and mentors in the development of this work. Initial research validation was conducted through LMArena (LMSYS, 2024-2025), enabling cross-model verification of hypotheses and findings to mitigate single-model bias. Deep research synthesis and writing assistance was provided by Claude (Anthropic, 2025). All original ideas, theoretical frameworks, analyses, and conclusions are the author's own.

---

## Common Tasks

### Adding a New Topic

1. Create folder: `publications/[topic-name]/`
2. Add Medium post: `Medium-[Topic_Name].md`
3. Add technical paper: `[Topic_Name]_Paper.md`
4. Update README.md with new links

### Updating Existing Content

1. Read current file to understand structure
2. Make edits preserving formatting
3. Update any affected cross-references
4. Commit with descriptive message

### Converting Draft to Publication

1. Extract content from source
2. Apply appropriate template (Medium or Paper)
3. Add proper front matter/metadata
4. Quality check formatting
5. Place in correct folder with correct naming

---

## Checklist for New Publications

- [ ] Content extracted and cleaned
- [ ] Placed in correct topic folder
- [ ] File named correctly (`Medium-*.md` or `*_Paper.md`)
- [ ] Front matter/metadata complete
- [ ] Formatting consistent with existing publications
- [ ] Tables numbered with bold numbers, italic titles
- [ ] References in APA format (papers only)
- [ ] Acknowledgments included (papers only)
- [ ] README.md updated if needed
- [ ] Committed with proper message format

---

*Instructions Version: 1.0*
*Last Updated: January 21, 2026*
*Series: ONI Framework Publications*
