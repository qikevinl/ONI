# Claude AI Instructions for ONI Framework Repository

> This file provides instructions for Claude to follow when assisting with the ONI Framework repository. Read this file at the start of any session involving content creation, publishing, or repository maintenance.

---

## Quick Reference

| Resource | Location | Purpose |
|----------|----------|---------|
| APA Template | `MAIN/publications/PAPER_TEMPLATE_APA.md` | Formatting for technical papers |
| Publishing Instructions | `MAIN/publications/PUBLISHING_INSTRUCTIONS.md` | Step-by-step publishing workflow |
| This File | `README.AI.md` | Claude-specific instructions |

---

## Repository File Tree

```
ONI/
├── README.md                          # Main repository documentation
├── README.AI.md                       # Claude AI instructions (this file)
├── ABOUT.md                           # Author bio
├── CONTRIBUTING.md                    # Contribution guidelines
├── LICENSE                            # Apache 2.0 License
│
└── MAIN/
    └── publications/
        ├── PAPER_TEMPLATE_APA.md      # APA 7th edition template
        ├── PUBLISHING_INSTRUCTIONS.md # Publishing workflow guide
        │
        ├── coherence-metric/
        │   ├── Medium-Coherence_Metric.md
        │   └── Coherence_Metric_Detailed_Paper.md
        │
        ├── neural-firewall/
        │   ├── Medium-Neural_Firewall.md
        │   └── Neural_Firewall_Architecture_Paper.md
        │
        ├── neural-ransomware/
        │   ├── Medium-Neural_Ransomware.md
        │   └── Neural_Ransomware_Paper.md
        │
        ├── oni-framework/
        │   ├── Medium-ONI_Framework.md
        │   └── ONI_Framework_Paper.md
        │
        └── scale-frequency/
            ├── Medium-Scale_Frequency.md
            └── Scale_Frequency_Paper.md
```

---

## Naming Conventions

### Folder Names
- **Format:** lowercase with hyphens
- **Examples:** `coherence-metric`, `neural-firewall`, `scale-frequency`

### File Names

| Type | Format | Example |
|------|--------|---------|
| Medium Posts | `Medium-[Topic_Name].md` | `Medium-Coherence_Metric.md` |
| Technical Papers | `[Topic_Name]_Paper.md` | `Neural_Ransomware_Paper.md` |
| Detailed Papers | `[Topic_Name]_Detailed_Paper.md` | `Coherence_Metric_Detailed_Paper.md` |
| Templates | `[NAME]_TEMPLATE_[TYPE].md` | `PAPER_TEMPLATE_APA.md` |
| Instructions | `[NAME]_INSTRUCTIONS.md` | `PUBLISHING_INSTRUCTIONS.md` |

### Topic Name Rules
- Use PascalCase with underscores between words
- Match folder name but with underscores instead of hyphens
- Examples:
  - Folder: `coherence-metric` → File: `Coherence_Metric`
  - Folder: `neural-firewall` → File: `Neural_Firewall`

---

## Workflow Instructions

### When Adding New Content

1. **Read the template first:**
   ```
   Read: MAIN/publications/PAPER_TEMPLATE_APA.md
   Read: MAIN/publications/PUBLISHING_INSTRUCTIONS.md
   ```

2. **Create topic folder (if new topic):**
   ```bash
   mkdir MAIN/publications/[topic-name]
   ```

3. **Create files with correct naming:**
   - Medium post: `Medium-[Topic_Name].md`
   - Technical paper: `[Topic_Name]_Paper.md`

4. **Apply proper formatting:**
   - Medium: Conversational, storytelling, web-optimized
   - Paper: APA 7th edition, formal, with references

5. **Update README.md** (see section below)

6. **Commit with proper message format**

---

## README.md Update Protocol

**After every commit that adds or modifies content, update README.md:**

### Step 1: Locate the Topics & Documents Section
Find the section starting with `## Topics & Documents`

### Step 2: Add/Update Table Entry
For each topic, maintain this format:

```markdown
### [Emoji] [Topic Name]

[Brief description of topic area]

| Document | Summary |
|----------|----------|
| [Medium-Topic_Name](MAIN/publications/topic-folder/Medium-Topic_Name.md) | *One-line description* |
| [Topic_Name Paper](MAIN/publications/topic-folder/Topic_Name_Paper.md) | *One-line description* |
```

### Step 3: Update Footer Stats
Update the document count at the bottom:
```markdown
*Documents: [X] | Topics: [Y]*
```

### Step 4: Update Date
```markdown
*Last update: YYYY-MM-DD*
```

---

## Standard Acknowledgments

Use this text in all technical papers:

> The author wishes to acknowledge the support of colleagues and mentors in the development of this work. Initial research validation was conducted through LMArena (LMSYS, 2024-2025), enabling cross-model verification of hypotheses and findings to mitigate single-model bias. Deep research synthesis and writing assistance was provided by Claude (Anthropic, 2025). All original ideas, theoretical frameworks, analyses, and conclusions are the author's own.

---

## Commit Message Format

```
[Action] [Topic/Scope]: Brief description

- Bullet point details
- What changed
- Why it changed

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

### Action Verbs
- `Add` - New content
- `Update` - Modified content
- `Fix` - Corrections
- `Reorganize` - Structural changes
- `Remove` - Deletions

---

## Quality Checklist

Before committing, verify:

- [ ] File naming follows conventions
- [ ] Folder naming follows conventions
- [ ] Medium posts have proper front matter (title, date, tags)
- [ ] Papers follow APA template structure
- [ ] Tables use bold numbers (`**Table 1**`) and italic titles
- [ ] References are in APA format
- [ ] Acknowledgments section included (papers only)
- [ ] README.md updated with new links
- [ ] Document count updated in README.md footer
- [ ] Date updated in README.md footer

---

## Common Tasks Reference

### Extract Content from Medium RSS
1. Fetch content from RSS feed URL
2. Extract title, date, URL, tags
3. Clean formatting artifacts
4. Save as `Medium-[Topic_Name].md`

### Convert Draft to Paper
1. Apply `PAPER_TEMPLATE_APA.md` structure
2. Add Abstract with keywords
3. Number sections
4. Format tables (bold numbers, italic titles)
5. Add References in APA format
6. Add standard Acknowledgments

### Add New Topic
1. Create folder: `MAIN/publications/[topic-name]/`
2. Create Medium file: `Medium-[Topic_Name].md`
3. Create Paper file: `[Topic_Name]_Paper.md`
4. Add section to README.md Topics & Documents
5. Update document count

### Rename/Reorganize Files
1. Use git mv for tracked files
2. Update all links in README.md
3. Verify no broken links
4. Commit with descriptive message

---

## Error Prevention

### Common Mistakes to Avoid
1. **Wrong naming:** Don't use dates in filenames (use `Medium-*` prefix instead)
2. **Missing updates:** Always update README.md after adding content
3. **Inconsistent formatting:** Always check template before writing
4. **Broken links:** Use relative paths from repository root
5. **Wrong table format:** Numbers are BOLD, titles are ITALIC

### If Unsure
1. Read `MAIN/publications/PUBLISHING_INSTRUCTIONS.md`
2. Check existing files for examples
3. Ask user for clarification before proceeding

---

*Version: 1.0*
*Last Updated: January 21, 2026*
*For: Claude AI Assistant*
