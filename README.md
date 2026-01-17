# KY - Korteriühistu Legal Repository

Searchable archive of Estonian apartment association (korteriühistu) legal documents. Law treated like software - versioned, searchable, cross-referenced.

## Structure

```
├── laws/               # Estonian laws (XML→Markdown, auto-converted)
├── court/              # Court cases by case number
│   ├── 2-23-16691/     # Main case: Võistluse tn 6 KÜ vs Tycoon OÜ
│   ├── 2-23-3752/      # Hagi tagamise tühistamine
│   ├── 2-24-3226/      # Tycoon OÜ kandeavaldus
│   └── bar-complaint/  # Complaint to bar association
├── analysis/           # Legal analysis threads
├── bylaws/             # KÜ bylaws (2019, 2023, 2024)
└── .github/
    ├── scripts/        # xml_to_md.py converter
    └── workflows/      # Auto-conversion on push
```

## Laws

7 Estonian laws with LLM-friendly Markdown, auto-generated from Riigi Teataja XML.

| Abbr | Law |
|------|-----|
| KrtS | Korteriomandi- ja korteriühistuseadus |
| AOS | Asjaõigusseadus |
| TsMS | Tsiviilkohtumenetluse seadustik |
| TsÜS | Tsiviilseadustiku üldosa seadus |
| AdvS | Advokatuuriseadus |
| MTÜS | Mittetulundusühingute seadus |
| AOSRakS | Asjaõigusseaduse rakendamise seadus |

See [laws/README.md](laws/README.md) for details.

## Bylaws

| Valid from | Valid to |
|------------|----------|
| 2019-12-13 | 2023-10-09 |
| 2023-10-09 | 2024-07-30 |
| 2024-07-30 | current |

## For AI Assistants

See [CLAUDE.md](CLAUDE.md) for detailed instructions.

