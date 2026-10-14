"""Shared helpers for the build scripts (paths and light markdown parsing)."""
import re
from pathlib import Path

BUILD_DIR = Path(__file__).resolve().parent
OUT_DIR = BUILD_DIR.parent
PROJECT = OUT_DIR.parent
FORMATTED = PROJECT / "06-formatted"

INLINE = re.compile(r"(\*\*.+?\*\*|\*.+?\*|`.+?`)")


def runs(text):
    """Split inline markdown into (text, bold, italic, code) tuples."""
    out = []
    for part in INLINE.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**") and len(part) > 4:
            out.append((part[2:-2], True, False, False))
        elif part.startswith("`") and part.endswith("`"):
            out.append((part[1:-1], False, False, True))
        elif part.startswith("*") and part.endswith("*") and len(part) > 2:
            out.append((part[1:-1], False, True, False))
        else:
            out.append((part, False, False, False))
    return out


def parse_report():
    """Return (title, blocks). Block = (kind, payload).
    kinds: h2, h3, p, bullet, num, table (list of rows)."""
    lines = (FORMATTED / "report.md").read_text(encoding="utf-8").splitlines()
    title = ""
    blocks = []
    i = 0
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            i += 1
            continue
        if ln.startswith("# "):
            title = ln[2:].strip()
        elif ln.startswith("### "):
            blocks.append(("h3", ln[4:].strip()))
        elif ln.startswith("## "):
            blocks.append(("h2", ln[3:].strip()))
        elif ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(set(c) <= set("-: ") for c in cells):
                    rows.append(cells)
                i += 1
            blocks.append(("table", rows))
            continue
        elif ln.startswith("- "):
            blocks.append(("bullet", ln[2:].strip()))
        elif re.match(r"\d+\. ", ln):
            blocks.append(("num", re.sub(r"^\d+\. ", "", ln).strip()))
        else:
            blocks.append(("p", ln.strip()))
        i += 1
    return title, blocks


def parse_slides():
    """Return list of dicts: title, bullets, notes."""
    text = (FORMATTED / "slides.md").read_text(encoding="utf-8")
    slides = []
    cur = None
    for ln in text.splitlines():
        if ln.startswith("## "):
            t = re.sub(r"^Slide \d+:\s*", "", ln[3:].strip())
            cur = {"title": t, "bullets": [], "notes": ""}
            slides.append(cur)
        elif cur is not None:
            if ln.startswith("- "):
                cur["bullets"].append(ln[2:].strip())
            elif ln.startswith("Notes:"):
                cur["notes"] = ln[len("Notes:"):].strip()
    return slides
