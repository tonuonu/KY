# KY - Korteriühistu Legal Repository

## Purpose
Searchable archive of Estonian apartment association (korteriühistu) legal documents. Law treated like software - versioned, searchable, cross-referenced.

## Current Content

### analüüs/ - Legal analysis
- `2-23-16691-ülevaade.md` - Case overview
- `2-23-16691-kokkuvõte.md` - Case summary
- `2-23-16691-arvestusmetoodika.md` - Accounting methodology issues
- `2-23-16691-õiguslikud-põhimõtted.md` - Legal principles
- `petrov-esindusõigus.md` - Petrov representation authority
- `savitski-teadmine.md` - Savitski knowledge analysis

### kohus/ - Court documents (by case number)
- **2-23-16691/** - Main case: Võistluse tn 6 KÜ vs Tycoon OÜ
- **2-23-3752/** - Hagi tagamise tühistamine
- **2-24-3226/** - Tycoon OÜ kandeavaldus
- **kaebus-advokatuurile/** - Bar complaint against Savitski
- **põhikirjad/** - KÜ bylaws (2019, 2023, 2024 versions)
  - kokkuvõte.md - Kohtuasja kokkuvõte
  - kohtuasja-ülevaade.md - Võistluse tn 6 KÜ vs TYCOON OÜ
  - arvestusmetoodika-probleemid.md - KÜ arvestusmetoodika analüüs
  - õiguslikud-põhimõtted.md - KrtS ja TsÜS põhimõtted

## seadused/ - Estonian Laws

**Converter:** `.github/scripts/xml_to_md.py`
- Auto-runs via GitHub Actions on `.akt` push
- Supports superscript sections (§ 64¹ → #para64b1)

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
