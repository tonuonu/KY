#!/usr/bin/env python3
"""Convert Riigi Teataja XML (.akt) files to LLM-friendly Markdown.

Usage:
    python xml_to_md.py [--input-dir seadused] [--output-dir seadused]
"""

import argparse
import re
from pathlib import Path
from lxml import etree
import yaml

# Law abbreviations mapping (RT ID -> abbreviation)
LAW_ABBREVIATIONS = {
    "123122022004": "KrtS",    # Korteriomandi- ja korteriühistuseadus
    "111112025002": "AOS",     # Asjaõigusseadus
    "103042025002": "TsMS",    # Tsiviilkohtumenetluse seadustik
    "131122024048": "TsÜS",    # Tsiviilseadustiku üldosa seadus
    "114032025004": "AdvS",    # Advokatuuriseadus
    "123122022015": "MTÜS",    # Mittetulundusühingute seadus
    "104122024003": "AOSRakS", # Asjaõigusseaduse rakendamise seadus
}

NAMESPACE = {"ns": "tyviseadus_1_10.02.2010"}


def get_text(element, xpath, default=""):
    """Get text content from element using xpath."""
    result = element.xpath(xpath, namespaces=NAMESPACE)
    if result:
        if isinstance(result[0], str):
            return result[0].strip()
        return (result[0].text or "").strip()
    return default


def extract_metadata(root):
    """Extract law metadata from XML."""
    meta = root.find(".//ns:metaandmed", NAMESPACE)
    aktinimi = root.find(".//ns:aktinimi/ns:nimi/ns:pealkiri", NAMESPACE)
    
    global_id = get_text(meta, "ns:globaalID/text()")
    lyhend = get_text(meta, "ns:lyhend/text()")
    
    # Fallback to our mapping if lyhend not in XML
    if not lyhend and global_id in LAW_ABBREVIATIONS:
        lyhend = LAW_ABBREVIATIONS[global_id]
    
    return {
        "riigiteataja_id": global_id,
        "seadus": aktinimi.text if aktinimi is not None else "",
        "lyhend": lyhend,
        "kehtiv_alates": get_text(meta, "ns:kehtivus/ns:kehtivuseAlgus/text()"),
        "riigiteataja_url": f"https://www.riigiteataja.ee/akt/{global_id}",
        "xml_source": f"{global_id}.akt",
    }


def clean_text(text):
    """Clean text content, handling inline tags."""
    if text is None:
        return ""
    # Handle <i> tags by converting to markdown emphasis
    text = re.sub(r"<i>([^<]+)</i>", r"*\1*", text)
    # Remove any other HTML-like tags
    text = re.sub(r"<[^>]+>", "", text)
    return text.strip()


def get_element_text(element):
    """Get combined text content from sisuTekst element."""
    sisu = element.find("ns:sisuTekst", NAMESPACE)
    if sisu is None:
        return ""
    
    parts = []
    for child in sisu:
        if child.tag.endswith("tavatekst"):
            # Get full serialized content to preserve <i> tags
            text = etree.tostring(child, encoding="unicode", method="text")
            # Also check for any i tags in the raw XML
            raw = etree.tostring(child, encoding="unicode")
            if "<i>" in raw:
                # Re-extract with tags
                text = child.text or ""
                for sub in child:
                    if sub.tag.endswith("}i") or sub.tag == "i":
                        text += f"*{sub.text or ''}*"
                    text += sub.tail or ""
            parts.append(clean_text(text))
    
    return " ".join(parts)


# Unicode superscript digits for display
SUPERSCRIPT_DIGITS = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")


def make_rt_link(lyhend, para_nr, superscript=None):
    """Create Riigi Teataja link for a paragraph.
    
    Args:
        lyhend: Law abbreviation (e.g., "KrtS")
        para_nr: Paragraph number (e.g., "64")
        superscript: Optional superscript number (e.g., "1" for § 64¹)
    """
    if superscript:
        # Display with Unicode superscript, link with b{n} format
        display_nr = f"{para_nr}{superscript.translate(SUPERSCRIPT_DIGITS)}"
        link_nr = f"{para_nr}b{superscript}"
    else:
        display_nr = para_nr
        link_nr = para_nr
    return f"[§ {display_nr}](https://www.riigiteataja.ee/akt/{lyhend}#para{link_nr})"


def process_alampunkt(element, indent=""):
    """Process alampunkt (sub-clause) element."""
    alampunkt_nr_elem = element.find("ns:alampunktNr", NAMESPACE)
    nr = alampunkt_nr_elem.text.strip() if alampunkt_nr_elem is not None and alampunkt_nr_elem.text else ""
    superscript = alampunkt_nr_elem.get("ylaIndeks") if alampunkt_nr_elem is not None else None
    text = get_element_text(element)
    display_nr = f"{nr}{superscript.translate(SUPERSCRIPT_DIGITS)}" if superscript else nr
    return f"{indent}{display_nr}) {text}\n"


def process_loige(element, indent=""):
    """Process lõige (subsection) element."""
    lines = []
    loige_nr_elem = element.find("ns:loigeNr", NAMESPACE)
    nr = loige_nr_elem.text.strip() if loige_nr_elem is not None and loige_nr_elem.text else ""
    superscript = loige_nr_elem.get("ylaIndeks") if loige_nr_elem is not None else None
    text = get_element_text(element)
    
    if nr:
        display_nr = f"{nr}{superscript.translate(SUPERSCRIPT_DIGITS)}" if superscript else nr
        lines.append(f"{indent}({display_nr}) {text}\n")
    else:
        lines.append(f"{indent}{text}\n")
    
    # Process sub-clauses
    for alampunkt in element.findall("ns:alampunkt", NAMESPACE):
        lines.append(process_alampunkt(alampunkt, indent + "  "))
    
    return "".join(lines)


def process_paragrahv(element, lyhend):
    """Process paragrahv (section) element."""
    lines = []
    para_nr_elem = element.find("ns:paragrahvNr", NAMESPACE)
    nr = para_nr_elem.text.strip() if para_nr_elem is not None and para_nr_elem.text else ""
    superscript = para_nr_elem.get("ylaIndeks") if para_nr_elem is not None else None
    pealkiri = get_text(element, "ns:paragrahvPealkiri/text()")
    
    # Section header with RT link
    rt_link = make_rt_link(lyhend, nr, superscript)
    if pealkiri:
        lines.append(f"### {rt_link} {pealkiri}\n\n")
    else:
        lines.append(f"### {rt_link}\n\n")
    
    # Process subsections
    for loige in element.findall("ns:loige", NAMESPACE):
        lines.append(process_loige(loige))
    
    lines.append("\n")
    return "".join(lines)


def process_jagu(element, lyhend):
    """Process jagu (subdivision) element."""
    lines = []
    nr = get_text(element, "ns:jaguNr/text()")
    pealkiri = get_text(element, "ns:jaguPealkiri/text()")
    
    lines.append(f"#### {nr}. jagu. {pealkiri}\n\n")
    
    for paragrahv in element.findall("ns:paragrahv", NAMESPACE):
        lines.append(process_paragrahv(paragrahv, lyhend))
    
    return "".join(lines)


def process_peatykk(element, lyhend):
    """Process peatükk (chapter) element."""
    lines = []
    nr = get_text(element, "ns:peatykkNr/text()")
    pealkiri = get_text(element, "ns:peatykkPealkiri/text()")
    
    lines.append(f"## {nr}. peatükk. {pealkiri}\n\n")
    
    # Process subdivisions if present
    jagud = element.findall("ns:jagu", NAMESPACE)
    if jagud:
        for jagu in jagud:
            lines.append(process_jagu(jagu, lyhend))
    
    # Process paragraphs directly under chapter
    for paragrahv in element.findall("ns:paragrahv", NAMESPACE):
        lines.append(process_paragrahv(paragrahv, lyhend))
    
    return "".join(lines)


def process_osa(element, lyhend):
    """Process osa (part) element."""
    lines = []
    nr = get_text(element, "ns:osaNr/text()")
    pealkiri = get_text(element, "ns:osaPealkiri/text()")
    
    lines.append(f"# {nr}. osa. {pealkiri}\n\n")
    
    for peatykk in element.findall("ns:peatykk", NAMESPACE):
        lines.append(process_peatykk(peatykk, lyhend))
    
    return "".join(lines)


def convert_xml_to_markdown(xml_path):
    """Convert a single XML file to Markdown."""
    tree = etree.parse(xml_path)
    root = tree.getroot()
    
    metadata = extract_metadata(root)
    lyhend = metadata["lyhend"]
    
    # Build YAML frontmatter
    frontmatter = yaml.dump(metadata, allow_unicode=True, sort_keys=False, default_flow_style=False)
    
    lines = [
        "---\n",
        frontmatter,
        "---\n\n",
        f"# {metadata['seadus']}\n\n",
    ]
    
    sisu = root.find(".//ns:sisu", NAMESPACE)
    if sisu is None:
        return None
    
    # Check for parts (osa) - larger codified laws
    osad = sisu.findall("ns:osa", NAMESPACE)
    if osad:
        for osa in osad:
            lines.append(process_osa(osa, lyhend))
    else:
        # Check for chapters
        peatykid = sisu.findall("ns:peatykk", NAMESPACE)
        if peatykid:
            for peatykk in peatykid:
                lines.append(process_peatykk(peatykk, lyhend))
        else:
            # Direct paragraphs under sisu (e.g., AOSRakS)
            for paragrahv in sisu.findall("ns:paragrahv", NAMESPACE):
                lines.append(process_paragrahv(paragrahv, lyhend))
    
    return "".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Convert RT XML to Markdown")
    parser.add_argument("--input-dir", default="seadused", help="Input directory with .akt files")
    parser.add_argument("--output-dir", default="seadused", help="Output directory for .md files")
    args = parser.parse_args()
    
    input_dir = Path(args.input_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    akt_files = list(input_dir.glob("*.akt"))
    print(f"Found {len(akt_files)} .akt files")
    
    for akt_file in akt_files:
        print(f"Converting {akt_file.name}...")
        try:
            markdown = convert_xml_to_markdown(akt_file)
            if markdown:
                output_file = output_dir / akt_file.with_suffix(".md").name
                output_file.write_text(markdown, encoding="utf-8")
                print(f"  -> {output_file}")
            else:
                print(f"  Warning: No content found in {akt_file.name}")
        except Exception as e:
            print(f"  Error: {e}")
    
    print("Done!")


if __name__ == "__main__":
    main()
