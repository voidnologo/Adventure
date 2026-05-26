#!/usr/bin/env python3
"""Build a print-ready PDF of the Aetherfall rulebook from the Eleventy _site output."""

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE_DIR = ROOT / "_site" / "rules"
DATA_DIR = ROOT / "web" / "_data"
CSS_DIR = ROOT / "web" / "rules" / "css"
OUTPUT_DIR = ROOT / "print"


def load_pages():
    with open(DATA_DIR / "pages.json") as f:
        return json.load(f)


def extract_content(html_path):
    """Extract the chapter body from a built HTML page."""
    text = html_path.read_text()

    # Find the page-hero div (chapter header)
    hero_match = re.search(r'<div class="page-hero">', text)
    if not hero_match:
        print(f"  WARNING: No page-hero found in {html_path.name}", file=sys.stderr)
        return ""

    # Find the bottom nav (chapter navigation links) — marks end of content
    nav_match = re.search(r'\n\s*<nav class="page-nav">', text[hero_match.start():])
    if nav_match:
        content = text[hero_match.start():hero_match.start() + nav_match.start()]
    else:
        # Fallback: find the footer
        footer_match = re.search(r'<footer class="site-footer">', text[hero_match.start():])
        if footer_match:
            content = text[hero_match.start():hero_match.start() + footer_match.start()]
        else:
            content = text[hero_match.start():]

    # Strip the compact nav if it got included
    content = re.sub(r'<nav class="page-nav-compact">.*?</nav>\s*', '', content, flags=re.DOTALL)

    return content


def prefix_ids(content, page_id):
    """Prefix all id attributes with the page ID to avoid duplicates across chapters."""
    def replace_id(match):
        attr = match.group(1)
        id_val = match.group(2)
        return f'{attr}"{page_id}--{id_val}"'

    content = re.sub(r'(id=)"([^"]+)"', replace_id, content)
    # Also fix internal href="#..." links to match
    content = re.sub(r'(href=)"#([^"]+)"', lambda m: f'{m.group(1)}"#{page_id}--{m.group(2)}"', content)
    return content


def build_toc(pages):
    """Build a table of contents with target-counter references."""
    entries = []
    for page in pages:
        num = page["num"]
        if not re.match(r'^\d+$', num) and num != "QS":
            continue
        display_num = num if num != "QS" else "QS"
        entries.append(
            f'    <li class="toc-entry">'
            f'<span class="toc-num">{display_num}</span>'
            f'<a href="#chapter-{page["id"]}">{page["title"]}</a>'
            f'</li>'
        )
    return "\n".join(entries)


def build_combined_html(pages):
    """Assemble all chapters into a single print-ready HTML document."""
    css_path = CSS_DIR / "print.css"

    parts = []
    parts.append(f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Aetherfall RPG — Rulebook</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,700;0,900;1,400;1,700&family=Source+Serif+4:ital,wght@0,400;0,600;0,700;1,400&family=JetBrains+Mono:wght@400;700&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,700;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css_path}">
</head>
<body>
""")

    # Title page
    parts.append("""
<section class="title-page">
  <div class="title-page-content">
    <h1 class="book-title">Aetherfall</h1>
    <p class="book-subtitle">Magic &amp; Machines in the 1920s</p>
    <p class="book-type">Tabletop Roleplaying Game</p>
    <p class="book-edition">Playtest Draft</p>
  </div>
</section>
""")

    # Table of contents
    toc_entries = build_toc(pages)
    parts.append(f"""
<section class="toc-chapter">
  <h1 class="chapter-title toc-title">Table of Contents</h1>
  <ol class="toc">
{toc_entries}
  </ol>
</section>
""")

    # Chapters
    for page in pages:
        page_file = page["file"]
        html_path = SITE_DIR / page_file
        if not html_path.exists():
            print(f"  WARNING: {html_path} not found, skipping", file=sys.stderr)
            continue

        print(f"  Processing: {page['num']} — {page['title']}")
        content = extract_content(html_path)
        if not content:
            continue

        content = prefix_ids(content, page["id"])
        parts.append(f'<section class="chapter" id="chapter-{page["id"]}">')
        parts.append(content)
        parts.append("</section>\n")

    parts.append("</body>\n</html>")
    return "\n".join(parts)


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    print("Loading page manifest...")
    pages = load_pages()

    print("Assembling combined HTML...")
    html = build_combined_html(pages)

    combined_path = OUTPUT_DIR / "aetherfall-rulebook.html"
    combined_path.write_text(html)
    print(f"  Written: {combined_path}")

    pdf_path = OUTPUT_DIR / "aetherfall-rulebook.pdf"
    print(f"Generating PDF with WeasyPrint...")
    result = subprocess.run(
        ["weasyprint", str(combined_path), str(pdf_path)],
        capture_output=True,
        text=True,
    )

    if result.returncode != 0:
        print("WeasyPrint errors:", file=sys.stderr)
        print(result.stderr, file=sys.stderr)
        sys.exit(1)

    if result.stderr:
        # WeasyPrint prints warnings to stderr even on success
        warnings = [l for l in result.stderr.splitlines() if "WARNING" in l]
        if warnings:
            print(f"  ({len(warnings)} warnings — mostly font/CSS)")

    print(f"  Done: {pdf_path}")
    print(f"  Size: {pdf_path.stat().st_size / 1024 / 1024:.1f} MB")


if __name__ == "__main__":
    main()
