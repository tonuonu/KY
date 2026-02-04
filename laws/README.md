# Laws

Index of Estonian laws and EU regulations.

## Estonian Laws

| Lühend | Seadus | Kehtiv | RT | Files |
|--------|--------|--------|-----|-------|
| KrtS | Korteriomandi- ja korteriühistuseadus | 2024-01-15 | [123122022004](https://www.riigiteataja.ee/akt/123122022004) | [MD](./123122022004.md) · [XML](./123122022004.akt) · [PDF](./123122022004.pdf) |
| AOS | Asjaõigusseadus | 2025-01-11 | [111112025002](https://www.riigiteataja.ee/akt/111112025002) | [MD](./111112025002.md) · [XML](./111112025002.akt) · [PDF](./111112025002.pdf) |
| TsMS | Tsiviilkohtumenetluse seadustik | 2025-04-03 | [103042025002](https://www.riigiteataja.ee/akt/103042025002) | [MD](./103042025002.md) · [XML](./103042025002.akt) · [PDF](./103042025002.pdf) |
| TsÜS | Tsiviilseadustiku üldosa seadus | 2025-01-01 | [131122024048](https://www.riigiteataja.ee/akt/131122024048) | [MD](./131122024048.md) · [XML](./131122024048.akt) · [PDF](./131122024048.pdf) |
| AdvS | Advokatuuriseadus | 2025-01-01 | [114032025004](https://www.riigiteataja.ee/akt/114032025004) | [MD](./114032025004.md) · [XML](./114032025004.akt) |
| MTÜS | Mittetulundusühingute seadus | 2023-02-01 | [123122022015](https://www.riigiteataja.ee/akt/123122022015) | [MD](./123122022015.md) · [XML](./123122022015.akt) · [PDF](./123122022015.pdf) |
| AOSRakS | Asjaõigusseaduse rakendamise seadus | 2025-01-01 | [104122024003](https://www.riigiteataja.ee/akt/104122024003) | [MD](./104122024003.md) · [XML](./104122024003.akt) · [PDF](./104122024003.pdf) |
| LennS | Lennundusseadus | 2026-01-01 | [130122025023](https://www.riigiteataja.ee/akt/130122025023) | [MD](./130122025023.md) · [XML](./130122025023.akt) · [PDF](./130122025023.pdf) |
| LMS | Lõhkematerjaliseadus | 2025-01-01 | [112122024009](https://www.riigiteataja.ee/akt/112122024009) | [MD](./112122024009.md) · [XML](./112122024009.akt) · [PDF](./112122024009.pdf) |

## Estonian Regulations (määrused)

These use a different XML schema and don't have auto-generated Markdown yet.

| RT ID | Määrus | PDF |
|-------|--------|-----|
| 112092017004 | Lõhkematerjali kasutamise ja hävitamise nõuded | [PDF](./112092017004.pdf) |
| 111072017013 | Lõhkaja, lõhkemeistri ja pürotehniku tervisenõuded | [PDF](./111072017013.pdf) |
| 122082017001 | Pürotehnilise toote müügikohale, ilutulestiku korraldamisele ja pürotehnilise toote hävitamisele esitatavad nõuded | [PDF](./122082017001.pdf) |
| 119022019013 | Lõhkematerjalile ja pürotehnilisele tootele, nende nõuetele vastavuse tõendamisele ja käibe jälgitavusele ning arvestuse pidamisele esitatavad nõuded | [PDF](./119022019013.pdf) |

## EU Regulations

| Number | Title | Files |
|--------|-------|-------|
| 2019/945 | Delegeeritud määrus - mehitamata õhusõidukite süsteemid (droonid) | [MD](./EU_2019-945.md) · [HTML](./EU_2019-945.html) |
| 2019/947 | Rakendusmäärus - mehitamata õhusõidukite käitamiseeskirjad | [MD](./EU_2019-947.md) · [HTML](./EU_2019-947.html) |

## File Formats

### Estonian Laws (seadused)

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

## Updating

### Estonian Laws

1. Download latest XML from [Riigi Teataja](https://www.riigiteataja.ee) (click "Laadi alla" → XML)
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
