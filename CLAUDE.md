# KY - Korteriühistu Legal Repository

Searchable archive of Estonian apartment association (korteriühistu) legal documents.

## Structure

```
├── seadused/                   # Estonian laws (7 laws, XML→Markdown)
│   ├── *.akt                   # Riigi Teataja XML source
│   ├── *.md                    # Auto-generated Markdown (LLM-friendly)
│   └── *.pdf                   # Official PDF reference
├── analüüs/                    # Legal analysis threads
│   ├── petrov-esindusõigus.md
│   └── savitski-teadmine.md
├── kohus/                      # Court judgments and proceedings
│   ├── 2-23-16691-*            # Main case: Võistluse tn 6 KÜ vs Tycoon OÜ
│   ├── Kaebus advokatuurile/   # Complaint to bar association
│   └── Aivar Orukaselt/        # Related case documents
├── põhikirjad/                 # KÜ bylaws (2019, 2023, 2024)
├── .serena/                    # Serena AI assistant config
│   └── memories/               # Project knowledge (read these first!)
└── .github/
    ├── scripts/xml_to_md.py    # Law XML→Markdown converter
    └── workflows/              # Auto-conversion on .akt push
```

## File Types

| Extension | Purpose |
|-----------|---------|
| `.akt` | Riigi Teataja XML (source of truth) |
| `.md` | Markdown (LLM-friendly, auto-generated for laws) |
| `.pdf` | Official documents |
| `.asice` | Digitally signed Estonian documents |

## Laws (seadused/)

| Lühend | Seadus | RT ID |
|--------|--------|-------|
| KrtS | Korteriomandi- ja korteriühistuseadus | 123122022004 |
| AOS | Asjaõigusseadus | 111112025002 |
| TsMS | Tsiviilkohtumenetluse seadustik | 103042025002 |
| TsÜS | Tsiviilseadustiku üldosa seadus | 131122024048 |
| AdvS | Advokatuuriseadus | 114032025004 |
| MTÜS | Mittetulundusühingute seadus | 123122022015 |
| AOSRakS | Asjaõigusseaduse rakendamise seadus | 104122024003 |

### Markdown Format
- YAML frontmatter with metadata
- Clickable RT links: `[§ 40](https://www.riigiteataja.ee/akt/KrtS#para40)`
- Superscript support: `§ 64¹` → `#para64b1`
- Structure: osa → peatükk → jagu → paragrahv → lõige → alampunkt

## For AI Assistants

### Serena Memories
Read `.serena/memories/` first for project context:
- `project_overview.md` - Current content and structure
- `law-documentation-strategy.md` - File formats and converter status
- `conventions.md` - Naming conventions

### Key Estonian Legal Terms
- **KÜ** - Korteriühistu (apartment association)
- **põhikiri** - bylaws/articles of association
- **üldkoosolek** - general meeting
- **majanduskava** - economic plan/budget
- **§** - paragrahv (section)
- **lg** - lõige (subsection)
- **p** - punkt (point)

### Working with Laws
1. Use `.md` files for reading/analysis
2. Reference by lühend (e.g., KrtS § 40 lg 1)
3. RT links go directly to Riigi Teataja paragraphs
4. Superscript numbers (§ 64¹) indicate amended sections

### Document Analysis Tasks
- Find legal basis citations (seaduse viited)
- Extract court reasoning (kohtu põhjendused)
- Compare bylaw versions
- Cross-reference between laws

## CI/CD

GitHub Actions auto-converts `.akt` → `.md` on push to `seadused/`.
