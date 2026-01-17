# Document Conventions

## Directory Structure
- `laws/` - Estonian laws (XML, MD, PDF)
- `court/` - Court cases organized by case number
- `analysis/` - Legal analysis in Markdown
- `bylaws/` - KÜ bylaws

## File Naming
**English filenames only** - no Estonian characters (ü, ö, ä, õ, š, ž)

### Court Cases
`court/{case-number}/{court-level}.{ext}`
- Example: `court/2-23-16691/maakohus.txt`
- Court levels: maakohus, ringkonnakohus, riigikohus

### Analysis
`analysis/{case-number}-{topic}.md`
- Example: `analysis/2-23-16691-overview.md`
- General analysis: `analysis/{topic}.md`

### Laws
`laws/{RT_ID}.{ext}`
- Example: `laws/123122022004.md`

## Content Guidelines
- Documents in Estonian (content, not filenames)
- Preserve section numbering (§, punkt, lõige)
- Cross-reference laws using RT (Riigi Teataja) codes
- Follow Estonian legal citation format

## Analysis Tasks
- Find legal basis citations (seaduse viited)
- Extract court reasoning (kohtu põhjendused)
- Compare bylaw versions
- Cross-reference between laws
