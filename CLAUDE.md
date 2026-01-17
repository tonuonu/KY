# KY - Korteriühistu Legal Repository

This repository contains legal documents related to Estonian apartment associations (korteriühistud), including court judgments, bylaws, and related legal materials.

## Purpose

Serve as a searchable archive of legal documents for reference and analysis. Law is treated like software - versioned, searchable, and cross-referenced.

## Structure

```
├── analüüs/                    # Legal analysis threads (õiguslikud analüüsid)
├── kohus/                      # Court judgments and proceedings
│   ├── 2-23-16691-*            # Main case: Võistluse tn 6 KÜ vs Tycoon OÜ
│   ├── Kaebus advokatuurile/   # Complaint to bar association
│   │   └── kaebus/             # Attachments (Lisa 1-6)
│   └── Aivar Orukaselt/        # Related case documents
├── põhikirjad/                 # Bylaws (põhikirjad)
├── seadused/                   # Laws (future)
├── lepingud/                   # Contracts (future)
└── protokollid/                # Meeting minutes (future)
```

## File Types

- `.md` - Markdown (preferred, searchable)
- `.txt` - Plain text conversions
- `.pdf` - Original court documents
- `.docx` - Original court documents
- `.asice` - Digitally signed Estonian documents
- `.mp3` - Court hearing recordings

## Document Naming Convention

### Court Judgments
`{case-number}-{court-level}.md`
- Case number: e.g., `2-23-16691`
- Court levels: `maakohus`, `ringkonnakohus`, `riigikohus`

### Bylaws
`{organization}-pohikiri-{date}.md`
- Date format: `YYYY-MM-DD`

## For AI Assistants

### Working with this repository
1. Documents are in Estonian
2. Legal references follow Estonian citation format
3. Cross-reference laws using RT (Riigi Teataja) codes
4. Preserve section numbering (§, punkt, lõige)

### Key Estonian Legal Terms
- **KÜ** - Korteriühistu (apartment association)
- **KrtS** - Korteriomandi- ja korteriühistuseadus
- **TsÜS** - Tsiviilseadustiku üldosa seadus
- **VÕS** - Võlaõigusseadus
- **TsMS** - Tsiviilkohtumenetluse seadustik
- **põhikiri** - bylaws/articles of association
- **üldkoosolek** - general meeting
- **majanduskava** - economic plan/budget

### Document Analysis Tasks
- Find legal basis citations (seaduse viited)
- Extract court reasoning (kohtu põhjendused)
- Compare bylaw versions
- Identify precedents

## CI/CD

See issue #1 for PDF/DOCX to Markdown conversion pipeline.

## Language

Serena language: `markdown`
