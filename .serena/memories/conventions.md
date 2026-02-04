# Document Conventions

## Directory Structure
- `laws/` - Estonian laws + EU regulations (XML, MD, PDF, HTML)
- `court/` - Court cases organized by case number
- `analysis/` - Legal analysis in Markdown
- `bylaws/` - KÜ bylaws

## File Naming
**English filenames only** - no Estonian characters (ü, ö, ä, õ, š, ž)

### Estonian Laws
`laws/{RT_ID}.{ext}`
- Example: `laws/123122022004.md`
- Formats: `.akt` (XML), `.md` (Markdown), `.pdf` (PDF)

### EU Regulations
`laws/EU_{YEAR}-{NUMBER}.{ext}`
- Example: `laws/EU_2019-945.html`
- Formats: `.html` (source), `.md` (Markdown)

### Court Cases
`court/{case-number}/{court-level}.{ext}`
- Example: `court/2-23-16691/maakohus.txt`
- Court levels: maakohus, ringkonnakohus, riigikohus

### Analysis
`analysis/{case-number}-{topic}.md`
- Example: `analysis/2-23-16691-overview.md`
- General analysis: `analysis/{topic}.md`

## Content Guidelines
- Documents in Estonian (content, not filenames)
- Preserve section numbering (§, punkt, lõige)
- Cross-reference laws using RT (Riigi Teataja) codes or CELEX for EU
- Follow Estonian legal citation format

## CI/CD Workflows
- `convert-laws.yml` - triggers on `laws/*.akt` push → generates `.md`
- `convert-eu-laws.yml` - triggers on `laws/EU_*.html` push → generates `.md`

## Analysis Tasks
- Find legal basis citations (seaduse viited)
- Extract court reasoning (kohtu põhjendused)
- Compare bylaw versions
- Cross-reference between laws
