# KY - Korteriühistu Legal Repository

Searchable archive of Estonian apartment association (korteriühistu) legal documents. Law treated like software - versioned, searchable, cross-referenced.

## Structure

```
├── seadused/           # Estonian laws (XML→Markdown, auto-converted)
├── analüüs/            # Legal analysis threads
├── kohus/              # Court judgments and proceedings
├── põhikirjad/         # KÜ bylaws (2019, 2023, 2024)
└── .github/
    ├── scripts/        # xml_to_md.py converter
    └── workflows/      # Auto-conversion on push
```

## Laws (seadused/)

7 Estonian laws with LLM-friendly Markdown, auto-generated from Riigi Teataja XML.

| Lühend | Seadus |
|--------|--------|
| KrtS | Korteriomandi- ja korteriühistuseadus |
| AOS | Asjaõigusseadus |
| TsMS | Tsiviilkohtumenetluse seadustik |
| TsÜS | Tsiviilseadustiku üldosa seadus |
| AdvS | Advokatuuriseadus |
| MTÜS | Mittetulundusühingute seadus |
| AOSRakS | Asjaõigusseaduse rakendamise seadus |

See [seadused/README.md](seadused/README.md) for details.

## Põhikirjad (Bylaws)

| Kehtiv | Lõpp |
|--------|------|
| 13.12.2019 | 09.10.2023 |
| 09.10.2023 | 30.07.2024 |
| 30.07.2024 | - (kehtiv) |

## For AI Assistants

See [CLAUDE.md](CLAUDE.md) for detailed instructions.

