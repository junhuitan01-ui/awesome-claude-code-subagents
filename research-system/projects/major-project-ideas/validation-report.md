# Validation report: major-project-ideas

Date: 14 October 2026. Checked by the orchestrator (not delegated).

## Deliverables

| File | Status | What was checked |
|------|--------|------------------|
| `07-deliverables/report.docx` | PASS | `tools/check_deliverables.py --dump` passed (3,349 words, 8 headings, 2 tables). All eight required section headings present in the spec's order (read with python-docx). Both tables are real Word tables. |
| `07-deliverables/report.pdf` | PASS | Checker passed (9 pages, 3,368 words). All eight sections, both tables and the 33-entry reference list found in the extracted text (pypdf). Page 2 rendered to an image and inspected: Table 1 starts under its caption, text wraps inside the page. |

## Brief requirements

| Success criterion | Result | Evidence |
|---|---|---|
| Answers all four research questions, each with cited sources | Met | RQ1 in §2, RQ2 in §3, RQ3 in §4, RQ4 in §5; review-2 confirmed the mapping. |
| At least eight concrete ideas, each with why it helps and effort | Met | Table 1 has 11 ideas with Idea, Why it helps, Effort, Sources columns. |
| A simple way to prioritise ideas | Met | §4 has a 7-step method built on MoSCoW. Steps 2–4 are labelled as the report's own synthesis, not a tested method. |
| Every fact cited to an opened source; gaps disclosed | Met, with notes | Every citation maps to a source both researchers recorded as opened (33 references). Several were read at abstract level only, which §7 says. Two evidence-gap markers are in §7. The §6 debate scores cite this pipeline's own verdict file, not an outside source. |
| Readable by a beginner | Met | Jargon (MoSCoW, CI, WCAG, OWASP, SCI, W3C, ISO, post-mortem, defect density) is explained on first use. Some sentences exceed the style guide's 25-word aim (format-notes.md). |
| Length 1,500–2,500 words (spec) | Met | Sections 1–7: 2,472 words without citation tags (2,556 if each citation tag is counted as a word). |

## Spot-checks of three key claims

1. "Timeliness was the most common organisational issue (26.15% of codes in that category)" [9] matches `independent-research.md` (I6: "Within organisational matters ... (34 codes, 26.15%)"). The reviewer also checked it against the paper itself.
2. "Students expected their thesis to take 33.9 days; it took 55.5" [30] matches `independent-research.md` (I17).
3. "Must Haves ... no more than about 60% of your effort, and about 20% ... in Could Haves" [15] matches `research-notes.md` (S9) and `independent-research.md` (I1); the reviewer confirmed it on the live page.

## Unresolved review issues

- **R12 (minor, from review 2):** §3 and §7 say "only four ideas have any source for their cost", but only three Table 1 rows (2, 3, 4) are shown without the (J) judgement label. The fourth (ethics, row 6) has a sourced lead time [19] but its effort cell is fully marked (J). Small inconsistency; no blocker or major issue remains open.

## Evidence gaps

- [EVIDENCE GAP: cost and benefit of deployment as a student-project addition]
- [EVIDENCE GAP: effort data for sustainability, security review and documentation in student projects]
- No source in either report shows how much any addition raises a grade.
- No systematic multi-institution data on what final-year students under-deliver; the most relevant 2026 paper ([28]) is embargoed until 12 November 2026.
- No Asian university rubric was found.
- Not verified: the final ACM Code of Ethics text (pages would not load), OWASP Top 10:2025, a possible newer BCS edition, and several papers read at abstract level only.

## Debate result

The primary researcher (John) won, weighted 4.00 against the independent researcher (Jane) at 3.55; no guard applied. All nine carry-over points from Jane (CO1–CO9) appear in the final report. Jane's points not carried over: secrets hygiene for public repositories (vendor source), the "gold plating" term (Wikipedia definition) and the time-boxing study (abstract only).

## Failed or skipped checks

- The first research attempt by John stopped partway when the account hit its usage limit; it was resumed after the limit reset and completed.
- No second improve cycle was needed (review 2 was PASS).
- The builder's first few shell commands combined `cd`/`&&`, against the one-plain-command convention; later commands followed it. No effect on the output.

## Tools and capabilities

- WebSearch and WebFetch worked through Claude Code's tools. Direct downloads with curl were blocked by this workspace's network policy (not needed).
- The custom agents were run as general-purpose subagents given their agent files as instructions, because this session was not started inside `research-system/`.
- python-docx, reportlab, pypdf and pdftoppm were available; nothing was left unbuilt.
