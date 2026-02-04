# KY - Korteriühistu Legal Repository

## Purpose
Searchable archive of Estonian apartment association (korteriühistu) legal documents. Law treated like software - versioned, searchable, cross-referenced.

## Structure

### laws/ - Estonian Laws and EU Regulations

**Converters:**
- `.github/scripts/xml_to_md.py` - Riigi Teataja XML → Markdown
- `.github/scripts/eurlex_to_md.py` - EUR-Lex HTML → Markdown

**CI Workflows:**
- `convert-laws.yml` - triggers on `laws/*.akt` push
- `convert-eu-laws.yml` - triggers on `laws/EU_*.html` push

#### Estonian Laws (seadused)

| ID | Abbr | Law |
|----|------|-----|
| 103042025002 | TsMS | Tsiviilkohtumenetluse seadustik |
| 104122024003 | AOSRakS | Asjaõigusseaduse rakendamise seadus |
| 111112025002 | AOS | Asjaõigusseadus |
| 112122024009 | LMS | Lõhkematerjaliseadus |
| 114032025004 | AdvS | Advokatuuriseadus |
| 123122022004 | KrtS | Korteriomandi- ja korteriühistuseadus |
| 123122022015 | MTÜS | Mittetulundusühingute seadus |
| 130122025023 | LennS | Lennundusseadus |
| 131122024048 | TsÜS | Tsiviilseadustiku üldosa seadus |

#### Estonian Regulations (määrused) - no MD converter yet

| ID | Regulation |
|----|------------|
| 112092017004 | Lõhkematerjali kasutamise ja hävitamise nõuded |
| 111072017013 | Lõhkaja, lõhkemeistri ja pürotehniku tervisenõuded |
| 119022019013 | Lõhkematerjalile ja pürotehnilisele tootele... |
| 122082017001 | Pürotehnilise toote müügikohale... |

#### EU Regulations

| Number | Title |
|--------|-------|
| 2019/945 | Delegeeritud määrus - droonide nõuded |
| 2019/947 | Rakendusmäärus - droonide käitamiseeskirjad |

File formats: `.akt` (XML source), `.pdf` (official), `.md` (LLM-friendly), `EU_*.html` (EUR-Lex HTML), `EU_*.md` (EU Markdown)

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
- Estonian Laws: XML (.akt) → Markdown (.md) via xml_to_md.py
- EU Regulations: HTML (EU_*.html) → Markdown (EU_*.md) via eurlex_to_md.py
- Court docs: PDF, DOCX, TXT
- Analysis: Markdown
- Signed docs: .asice
