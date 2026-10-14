from xml.sax.saxutils import escape
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, ListFlowable, ListItem)
from common import OUT_DIR, parse_report, runs


def markup(text):
    out = ""
    for t, b, i, c in runs(text):
        s = escape(t)
        if c:
            s = f'<font face="Courier" size="8.5">{s}</font>'
        if b:
            s = f"<b>{s}</b>"
        if i:
            s = f"<i>{s}</i>"
        out += s
    return out


def main():
    title, blocks = parse_report()
    ss = getSampleStyleSheet()
    body = ParagraphStyle("body", parent=ss["BodyText"], fontSize=10, leading=13.5, spaceAfter=6)
    cell = ParagraphStyle("cell", parent=body, fontSize=8.5, leading=10.5, spaceAfter=0)
    cellb = ParagraphStyle("cellb", parent=cell, fontName="Helvetica-Bold")
    h1 = ParagraphStyle("h1", parent=ss["Heading1"], fontSize=15, spaceBefore=12, spaceAfter=6)
    h2 = ParagraphStyle("h2", parent=ss["Heading2"], fontSize=12, spaceBefore=8, spaceAfter=4)
    ttl = ParagraphStyle("ttl", parent=ss["Title"], fontSize=20, leading=24)

    story = [Paragraph(escape(title), ttl)]
    i = 0
    while i < len(blocks):
        kind, p = blocks[i]
        if kind in ("bullet", "num"):
            items = []
            while i < len(blocks) and blocks[i][0] == kind:
                items.append(ListItem(Paragraph(markup(blocks[i][1]), body)))
                i += 1
            if kind == "bullet":
                story.append(ListFlowable(items, bulletType="bullet", start="•", leftIndent=16))
            else:
                story.append(ListFlowable(items, bulletType="1", leftIndent=18))
            continue
        if kind == "h2":
            story.append(Paragraph(escape(p), h1))
        elif kind == "h3":
            story.append(Paragraph(escape(p), h2))
        elif kind == "p":
            story.append(Paragraph(markup(p), body))
        elif kind == "table":
            data = [[Paragraph(markup(c), cellb if r == 0 else cell) for c in row]
                    for r, row in enumerate(p)]
            w = 17 * cm
            widths = [6.2 * cm, 2.4 * cm, 2.4 * cm, 3.0 * cm, 3.0 * cm]
            t = Table(data, colWidths=widths, repeatRows=1)
            t.setStyle(TableStyle([
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E8E8E8")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ]))
            story.append(t)
            story.append(Spacer(1, 6))
        i += 1

    out = OUT_DIR / "report.pdf"
    SimpleDocTemplate(str(out), pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm,
                      topMargin=2 * cm, bottomMargin=2 * cm, title=title).build(story)
    print("saved", out)


main()
