# KY - Legal Repository

Searchable archive of Estonian laws, EU regulations, and legal documents. Law treated like software - versioned, searchable, cross-referenced.

## Structure

```
├── laws/               # Estonian laws + EU regulations
│   ├── *.akt           # Riigi Teataja XML
│   ├── *.md            # Auto-generated Markdown
│   ├── EU_*.html       # EUR-Lex HTML
│   └── EU_*.md         # Auto-generated EU Markdown
├── court/              # Court cases by case number
│   ├── 2-23-16691/     # Main case: Võistluse tn 6 KÜ vs Tycoon OÜ
│   ├── 2-23-3752/      # Hagi tagamise tühistamine
│   ├── 2-24-3226/      # Tycoon OÜ kandeavaldus
│   └── bar-complaint/  # Complaint to bar association
├── analysis/           # Legal analysis threads
├── bylaws/             # KÜ bylaws (2019, 2023, 2024)
└── .github/
    ├── scripts/        # xml_to_md.py, eurlex_to_md.py converters
    └── workflows/      # Auto-conversion on push
```

## Laws

### Estonian Laws (9)

| Abbr | Law |
|------|-----|
| KrtS | Korteriomandi- ja korteriühistuseadus |
| AOS | Asjaõigusseadus |
| TsMS | Tsiviilkohtumenetluse seadustik |
| TsÜS | Tsiviilseadustiku üldosa seadus |
| AdvS | Advokatuuriseadus |
| MTÜS | Mittetulundusühingute seadus |
| AOSRakS | Asjaõigusseaduse rakendamise seadus |
| LennS | Lennundusseadus |
| LMS | Lõhkematerjaliseadus |

### EU Regulations (2)

| Number | Title |
|--------|-------|
| 2019/945 | Delegeeritud määrus - droonide nõuded |
| 2019/947 | Rakendusmäärus - droonide käitamiseeskirjad |

See [laws/README.md](laws/README.md) for full details.

## Bylaws

| Valid from | Valid to |
|------------|----------|
| 2019-12-13 | 2023-10-09 |
| 2023-10-09 | 2024-07-30 |
| 2024-07-30 | current |

## For AI Assistants

See [CLAUDE.md](CLAUDE.md) for detailed instructions.
