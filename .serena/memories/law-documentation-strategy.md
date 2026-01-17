# Law Documentation Strategy

## Decision: File Management

**Keep:**
- `*.akt` (XML) - Source of truth with full structure/metadata
- `*.pdf` - Official version for human verification
- `*.md` (auto-generated) - Optimized for LLMs (Claude/Serena)

**Deleted:**
- `*.txt` - Redundant middle ground

## Laws in Repository

| ID | Lühend | Seadus | Kehtiv |
|----|--------|--------|--------|
| 123122022004 | KrtS | Korteriomandi- ja korteriühistuseadus | 2024-01-15 |
| 111112025002 | AOS | Asjaõigusseadus | 2025-11-21 |
| 103042025002 | TsMS | Tsiviilkohtumenetluse seadustik | 2025-04-13 |
| 131122024048 | TsÜS | Tsiviilseadustiku üldosa seadus | 2025-01-01 |
| 114032025004 | AdvS | Advokatuuriseadus | 2025-01-01 |
| 123122022015 | MTÜS | Mittetulundusühingute seadus | 2023-02-01 |
| 104122024003 | AOSRakS | Asjaõigusseaduse rakendamise seadus | 2025-01-01 |

## Markdown Format Design

### YAML Frontmatter
```yaml
---
riigiteataja_id: "123122022004"
seadus: "Korteriomandi- ja korteriühistuseadus"
lyhend: "KrtS"
kehtiv_alates: "2024-01-15"
riigiteataja_url: "https://www.riigiteataja.ee/akt/123122022004"
xml_source: "123122022004.akt"
pdf_source: "123122022004.pdf"
---
```

### Riigi Teataja Links
Format: `[§ 40](https://www.riigiteataja.ee/akt/KrtS#para40)`

Creates clickable links directly to paragraphs.

### Structure Preservation
- Peatükk (chapter)
- Paragrahv (§)
- Lõige (subsection)
- Punkt (point)

## Implementation Status

**Completed:**
- ✅ #8: XML to Markdown converter script (PR #11)
  - `.github/scripts/xml_to_md.py` - converts .akt XML to .md
  - Handles all structure types (osa/peatükk/jagu/paragrahv/lõige/alampunkt)
  - Fixed to handle laws without chapters (e.g., AOSRakS)

**Closed (Deprecated):**
- ❌ #1: PDF to Markdown converter - superseded by XML approach

**Completed:**
- ✅ #9: GitHub Actions workflow (PR #13)
- ✅ #10: seadused/README.md index (PR #12)
- ✅ #14: Superscript (ylaIndeks/ülaindeks) support

## Usage

```bash
# Convert all .akt files to .md
python3 .github/scripts/xml_to_md.py --input-dir laws --output-dir laws
```

Requires: `lxml`, `pyyaml`

## Note
Directory renamed from `seadused/` to `laws/` for English consistency.