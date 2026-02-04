#!/usr/bin/env python3
"""Convert EUR-Lex HTML files to LLM-friendly Markdown.

Supports Estonian language EU regulations downloaded from EUR-Lex.

Usage:
    python eurlex_to_md.py [--input-dir laws] [--output-dir laws]
"""

import argparse
import re
from pathlib import Path
from bs4 import BeautifulSoup
import yaml


def extract_celex_from_filename(filename: str) -> str:
    """Extract CELEX number from filename like EU_2019-945.html."""
    match = re.search(r"EU_(\d{4})-(\d+)", filename)
    if match:
        year, num = match.groups()
        return f"32019R0{num}"  # Simplified - assumes regulation
    return ""


def extract_metadata(soup: BeautifulSoup, filename: str) -> dict:
    """Extract regulation metadata from EUR-Lex HTML."""
    # Title from eli-main-title
    title_div = soup.find("div", class_="eli-main-title")
    title_parts = []
    if title_div:
        for p in title_div.find_all("p", class_="oj-doc-ti"):
            text = p.get_text(strip=True)
            if text:
                title_parts.append(text)
    
    title = " ".join(title_parts) if title_parts else filename
    
    # Extract regulation number and date from title
    reg_match = re.search(r"MÄÄRUS \(EL\) (\d+/\d+)", title)
    reg_number = reg_match.group(1) if reg_match else ""
    
    date_match = re.search(r"(\d+)\. (\w+) (\d{4})", title)
    date_str = f"{date_match.group(1)}. {date_match.group(2)} {date_match.group(3)}" if date_match else ""
    
    # Extract CELEX from canonical link
    canonical = soup.find("link", rel="canonical")
    celex = ""
    if canonical and canonical.get("href"):
        celex_match = re.search(r"CELEX[:\d]*(\d+R\d+)", canonical["href"])
        if celex_match:
            celex = celex_match.group(1)
    
    # Parse filename for year and number
    fn_match = re.search(r"EU_(\d{4})-(\d+)", filename)
    year = fn_match.group(1) if fn_match else ""
    num = fn_match.group(2) if fn_match else ""
    
    return {
        "tüüp": "EU määrus",
        "number": reg_number or f"{year}/{num}",
        "kuupäev": date_str,
        "pealkiri": title,
        "celex": celex or f"32019R0{num}",
        "eurlex_url": f"https://eur-lex.europa.eu/legal-content/ET/TXT/HTML/?uri=CELEX:32019R0{num}",
        "html_source": filename,
    }


def clean_text(text: str) -> str:
    """Clean and normalize text content."""
    # Normalize whitespace
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def process_recitals(soup: BeautifulSoup) -> list[str]:
    """Process recitals (põhjendused) section."""
    lines = []
    
    # Find all recital divs (rct_1, rct_2, etc.)
    for div in soup.find_all("div", class_="eli-subdivision", id=re.compile(r"^rct_\d+")):
        # Get recital number and text
        cells = div.find_all("td")
        if len(cells) >= 2:
            num = clean_text(cells[0].get_text())
            text = clean_text(cells[1].get_text())
            if num and text:
                lines.append(f"{num} {text}\n")
    
    return lines


def process_article(div) -> list[str]:
    """Process a single article."""
    lines = []
    
    # Article number
    art_title = div.find("p", class_="oj-ti-art")
    if art_title:
        lines.append(f"### {clean_text(art_title.get_text())}\n\n")
    
    # Article subtitle
    art_subtitle = div.find("p", class_="oj-sti-art")
    if art_subtitle:
        lines.append(f"**{clean_text(art_subtitle.get_text())}**\n\n")
    
    # Article paragraphs
    for para_div in div.find_all("div", id=re.compile(r"^\d{3}\.\d{3}$")):
        para_text = clean_text(para_div.get_text())
        if para_text:
            lines.append(f"{para_text}\n\n")
    
    # Direct paragraphs with oj-normal class (not in tables)
    for p in div.find_all("p", class_="oj-normal", recursive=False):
        text = clean_text(p.get_text())
        if text and not text.startswith("(") and not re.match(r"^\d+\)", text):
            lines.append(f"{text}\n\n")
    
    # Numbered points in tables
    for table in div.find_all("table", recursive=False):
        rows = table.find_all("tr")
        for row in rows:
            cells = row.find_all("td")
            if len(cells) >= 2:
                marker = clean_text(cells[0].get_text())
                content = clean_text(cells[1].get_text())
                if marker and content:
                    lines.append(f"{marker} {content}\n\n")
    
    return lines


def process_chapter(div) -> list[str]:
    """Process a chapter."""
    lines = []
    
    # Chapter title
    chapter_title = div.find("p", class_="oj-ti-section-1")
    if chapter_title:
        lines.append(f"## {clean_text(chapter_title.get_text())}\n\n")
    
    # Chapter subtitle
    chapter_subtitle = div.find("p", class_="oj-ti-section-2")
    if chapter_subtitle:
        lines.append(f"**{clean_text(chapter_subtitle.get_text())}**\n\n")
    
    # Process articles within chapter
    for art_div in div.find_all("div", class_="eli-subdivision", id=re.compile(r"^art_\d+")):
        lines.extend(process_article(art_div))
    
    return lines


def process_annex(div) -> list[str]:
    """Process an annex (lisa)."""
    lines = []
    
    # Annex title
    annex_title = div.find("p", class_="oj-ti-grseq-1")
    if annex_title:
        lines.append(f"# {clean_text(annex_title.get_text())}\n\n")
    
    # Annex subtitle
    annex_subtitle = div.find("p", class_="oj-sti-grseq-1")
    if annex_subtitle:
        lines.append(f"**{clean_text(annex_subtitle.get_text())}**\n\n")
    
    # Process content - can have various structures
    for p in div.find_all("p", class_=re.compile(r"oj-")):
        text = clean_text(p.get_text())
        if text:
            # Determine heading level based on class
            cls = p.get("class", [])
            if "oj-ti-grseq-1" in cls:
                lines.append(f"# {text}\n\n")
            elif "oj-ti-grseq-2" in cls:
                lines.append(f"## {text}\n\n")
            elif "oj-ti-grseq-3" in cls:
                lines.append(f"### {text}\n\n")
            elif "oj-sti-grseq-1" in cls or "oj-sti-grseq-2" in cls:
                lines.append(f"**{text}**\n\n")
            else:
                lines.append(f"{text}\n\n")
    
    return lines


def convert_html_to_markdown(html_path: Path) -> str | None:
    """Convert a single EUR-Lex HTML file to Markdown."""
    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    
    metadata = extract_metadata(soup, html_path.name)
    
    # Build YAML frontmatter
    frontmatter = yaml.dump(metadata, allow_unicode=True, sort_keys=False, default_flow_style=False)
    
    lines = [
        "---\n",
        frontmatter,
        "---\n\n",
        f"# {metadata['pealkiri']}\n\n",
    ]
    
    # Process preamble (preambul)
    pbl = soup.find("div", class_="eli-subdivision", id="pbl_1")
    if pbl:
        lines.append("## Preambul\n\n")
        
        # Institution
        for p in pbl.find_all("p", class_="oj-normal", recursive=False):
            text = clean_text(p.get_text())
            if text and text not in ["ning arvestades järgmist:", "ON VASTU VÕTNUD KÄESOLEVA MÄÄRUSE:"]:
                lines.append(f"{text}\n\n")
        
        # Recitals
        recitals = process_recitals(pbl)
        if recitals:
            lines.append("### Põhjendused\n\n")
            lines.extend(recitals)
            lines.append("\n")
    
    # Process chapters (I PEATÜKK, II PEATÜKK, etc.)
    for chapter in soup.find_all("div", id=re.compile(r"^cpt_")):
        lines.extend(process_chapter(chapter))
    
    # Process standalone articles (not in chapters)
    enc = soup.find("div", class_="eli-subdivision", id="enc_1")
    if enc:
        for art_div in enc.find_all("div", class_="eli-subdivision", id=re.compile(r"^art_\d+"), recursive=False):
            lines.extend(process_article(art_div))
    
    # Process annexes (lisad)
    for annex in soup.find_all("div", class_="eli-subdivision", id=re.compile(r"^anx_")):
        lines.extend(process_annex(annex))
    
    return "".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Convert EUR-Lex HTML to Markdown")
    parser.add_argument("--input-dir", default="laws", help="Input directory with EU_*.html files")
    parser.add_argument("--output-dir", default="laws", help="Output directory for .md files")
    args = parser.parse_args()
    
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    html_files = list(input_dir.glob("EU_*.html"))
    print(f"Found {len(html_files)} EU HTML files")
    
    for html_file in html_files:
        print(f"Converting {html_file.name}...")
        try:
            markdown = convert_html_to_markdown(html_file)
            if markdown:
                output_file = output_dir / html_file.with_suffix(".md").name
                output_file.write_text(markdown, encoding="utf-8")
                print(f"  -> {output_file}")
            else:
                print(f"  Warning: No content found in {html_file.name}")
        except Exception as e:
            print(f"  Error: {e}")
    
    print("Done!")


if __name__ == "__main__":
    main()
