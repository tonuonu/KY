# Laws

Index of Estonian laws and EU regulations relevant to apartment association (korteriühistu) legal matters.

## Laws Index

| Lühend | Seadus | Kehtiv | RT | Files |
|--------|--------|--------|-----|-------|
| KrtS | Korteriomandi- ja korteriühistuseadus | 2024-01-15 | [123122022004](https://www.riigiteataja.ee/akt/123122022004) | [MD](./123122022004.md) · [XML](./123122022004.akt) · [PDF](./123122022004.pdf) |
| AOS | Asjaõigusseadus | 2025-01-11 | [111112025002](https://www.riigiteataja.ee/akt/111112025002) | [MD](./111112025002.md) · [XML](./111112025002.akt) · [PDF](./111112025002.pdf) |
| TsMS | Tsiviilkohtumenetluse seadustik | 2025-04-03 | [103042025002](https://www.riigiteataja.ee/akt/103042025002) | [MD](./103042025002.md) · [XML](./103042025002.akt) · [PDF](./103042025002.pdf) |
| TsÜS | Tsiviilseadustiku üldosa seadus | 2025-01-01 | [131122024048](https://www.riigiteataja.ee/akt/131122024048) | [MD](./131122024048.md) · [XML](./131122024048.akt) · [PDF](./131122024048.pdf) |
| AdvS | Advokatuuriseadus | 2025-01-01 | [114032025004](https://www.riigiteataja.ee/akt/114032025004) | [MD](./114032025004.md) · [XML](./114032025004.akt) |
| MTÜS | Mittetulundusühingute seadus | 2023-02-01 | [123122022015](https://www.riigiteataja.ee/akt/123122022015) | [MD](./123122022015.md) · [XML](./123122022015.akt) · [PDF](./123122022015.pdf) |
| AOSRakS | Asjaõigusseaduse rakendamise seadus | 2025-01-01 | [104122024003](https://www.riigiteataja.ee/akt/104122024003) | [MD](./104122024003.md) · [XML](./104122024003.akt) · [PDF](./104122024003.pdf) |

## EU Regulations

| Number | Title | Files |
|--------|-------|-------|
| 2019/945 | Delegeeritud määrus - mehitamata õhusõidukite süsteemid | [HTML](./EU_2019-945.html) |
| 2019/947 | Rakendusmäärus - mehitamata õhusõidukite käitamiseeskirjad | [HTML](./EU_2019-947.html) |

$1

| Format | Purpose | Source |
|--------|---------|--------|
| **XML** (`.akt`) | Source of truth with full structure and metadata | [Riigi Teataja](https://www.riigiteataja.ee) |
| **PDF** (`.pdf`) | Official version for human verification | [Riigi Teataja](https://www.riigiteataja.ee) |
| **Markdown** (`.md`) | LLM-friendly, auto-generated from XML | `xml_to_md.py` |

### Estonian Laws

| Format | Purpose | Source |
|--------|---------|--------|
| **XML** (`.akt`) | Source of truth with full structure | [Riigi Teataja](https://www.riigiteataja.ee) |
| **PDF** (`.pdf`) | Official version for human verification | [Riigi Teataja](https://www.riigiteataja.ee) |
| **Markdown** (`.md`) | LLM-friendly, auto-generated from XML | `xml_to_md.py` |

### EU Regulations

| Format | Purpose | Source |
|--------|---------|--------|
| **HTML** (`EU_*.html`) | Source of truth downloaded from EUR-Lex | [EUR-Lex](https://eur-lex.europa.eu) |
| **Markdown** (`EU_*.md`) | LLM-friendly, auto-generated from HTML | `eurlex_to_md.py` |


$1### Estonian Laws

$2 from [Riigi Teataja](https://www.riigiteataja.ee) (click "Laadi alla" → XML)
2. Save as `laws/{RT_ID}.akt`
3. Download PDF, save as `laws/{RT_ID}.pdf`
4. Commit and push - GitHub Actions will auto-generate Markdown

**Manual conversion:**
```bash
python3 .github/scripts/xml_to_md.py --input-dir laws --output-dir laws
```

### EU Regulations

1. Go to [EUR-Lex](https://eur-lex.europa.eu) and find the regulation
2. Select Estonian language, then HTML format
3. Save as `laws/EU_{YEAR}-{NUMBER}.html` (e.g., `EU_2019-945.html`)
4. Commit and push - GitHub Actions will auto-generate Markdown

**Manual conversion:**
```bash
python3 .github/scripts/eurlex_to_md.py --input-dir laws --output-dir laws
```

## Riigi Teataja ID Format

The numeric ID (e.g., `123122022004`) encodes:
- Publication date
- Article number
- Used for versioning - same law may have multiple IDs over time
