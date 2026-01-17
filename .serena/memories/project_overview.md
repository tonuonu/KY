# KY - Korteriühistu Legal Repository

## Purpose
Searchable archive of Estonian apartment association (korteriühistu) legal documents. Law treated like software - versioned, searchable, cross-referenced.

## Structure

### laws/ - Estonian Laws
Converter: `.github/scripts/xml_to_md.py`
- Auto-runs via GitHub Actions on `.akt` push
- Supports superscript sections (§ 64¹ → #para64b1)

| ID | Abbr | Law |
|----|------|-----|
| 103042025002 | TsMS | Tsiviilkohtumenetluse seadustik |
| 104122024003 | AOSRakS | Asjaõigusseaduse rakendamise seadus |
| 111112025002 | AOS | Asjaõigusseadus |
| 114032025004 | AdvS | Advokatuuriseadus |
| 123122022004 | KrtS | Korteriomandi- ja korteriühistuseadus |
| 123122022015 | MTÜS | Mittetulundusühingute seadus |
| 131122024048 | TsÜS | Tsiviilseadustiku üldosa seadus |

File formats: `.akt` (XML source), `.pdf` (official), `.md` (LLM-friendly, auto-generated)

### court/ - Court Cases
Organized by case number:
- **2-23-16691/** - Main case: Võistluse tn 6 KÜ vs Tycoon OÜ (all 3 court levels)
- **2-23-3752/** - Hagi tagamise tühistamine (2024-04-15)
- **2-24-3226/** - Tycoon OÜ kandeavaldus (2025-02-20)
- **bar-complaint/** - Complaint against advocate Daniil Savitski
  - complaint-savitski.pdf
  - attachments/ (court docs, hearing audio, screenshots)

### analysis/ - Legal Analysis
- 2-23-16691-overview.md - Case overview
- 2-23-16691-summary.md - Lessons learned
- 2-23-16691-accounting-issues.md - KÜ accounting methodology problems
- 2-23-16691-legal-principles.md - KrtS and TsÜS principles
- petrov-representation.md - Y. Petrovi representation dispute
- savitski-knowledge.md - Advocate Savitski's knowledge of registry status

### bylaws/ - KÜ Bylaws
Three versions: 2019, 2023, 2024 (current)

## Document Formats
- Laws: XML (.akt) → Markdown (.md) via xml_to_md.py
- Court docs: PDF, DOCX, TXT
- Analysis: Markdown
- Signed docs: .asice
