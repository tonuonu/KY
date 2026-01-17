# KY - Korteriühistu Legal Repository

## Purpose
Searchable archive of Estonian apartment association (korteriühistu) legal documents. Law treated like software - versioned, searchable, cross-referenced.

## Current Content
- **analüüs/** - Legal analysis threads
  - petrov-esindusõigus.md - Y. Petrovi esindusõiguse vaidlus TYCOON OÜ esindamisel
  - savitski-teadmine.md - Advokaat Savitski teadmine Petrovi registristaatusest (2-23-3752, 2-24-3226)
- **kohus/** - Court judgments and related documents
  - Case 2-23-16691 (Võistluse tn 6 KÜ vs Tycoon OÜ) - all 3 court levels
  - **Kaebus advokatuurile/** - Complaint against advocate Daniil Savitski
    - Main complaint PDF
    - kaebus/ - Attachments (Lisa 1-6): court docs, audio recording, screenshots
  - **Aivar Orukaselt/** - Related case documents
    - 2-23-3752 - hagi tagamise tühistamine (15.04.2024)
    - 2-24-3226 - Tycoon OÜ kandeavaldus (20.02.2025)
- **põhikirjad/** - KÜ bylaws (2019, 2023, 2024 versions)
- Root .md files: kokkuvõte, kohtuasja-ülevaade, arvestusmetoodika-probleemid, õiguslikud-põhimõtted

## seadused/ - Estonian Laws

**Converter:** `.github/scripts/xml_to_md.py` (PR #11)

| ID | Lühend | Seadus |
|----|--------|--------|
| 103042025002 | TsMS | Tsiviilkohtumenetluse seadustik |
| 104122024003 | AOSRakS | Asjaõigusseaduse rakendamise seadus |
| 111112025002 | AOS | Asjaõigusseadus |
| 114032025004 | AdvS | Advokatuuriseadus |
| 123122022004 | KrtS | Korteriomandi- ja korteriühistuseadus |
| 123122022015 | MTÜS | Mittetulundusühingute seadus |
| 131122024048 | TsÜS | Tsiviilseadustiku üldosa seadus |

**File formats:**
- `.akt` - Riigi Teataja XML source
- `.pdf` - Official PDF for human reference
- `.md` - LLM-friendly Markdown (auto-generated)

## Document Formats
- Laws: XML (.akt) → Markdown (.md) via xml_to_md.py
- Court docs: PDF
- Analysis: Markdown
