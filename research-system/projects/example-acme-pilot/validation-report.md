# Validation report — example-acme-pilot

Date: 14 October 2026. Run by the orchestrator after the Step 7 build.
All data is fictional test data (three files in `00-brief/`; no web research).

## Deliverables

| File | Status | What was checked |
|---|---|---|
| `07-deliverables/report.docx` | PASS (with a word-count caveat) | Checker: opens, 9 headings, 1 table. I read the dumped text and ran my own script on the file. The six required sections are present in order. Table 1 has 10 data rows (5 operations and 5 survey). Numbered [1]–[3] citations and a reference list are present. Word count: see Caveats. I did not see the end of the References in the checker dump (it was cut off); the docx text matches `06-formatted/report.md`, whose three references I read in full. |
| `07-deliverables/report.pdf` | PASS (with the same caveat) | Checker: 3 pages, 1,093 words. Dumped text matches the docx up to where the dump was cut off. I did not look at the PDF's layout. |
| `07-deliverables/slides.pptx` | PASS | Checker: 7 slides (spec: 5–7), 7 with speaker notes. Dumped text shows the title, key findings (slides 2–3), limitations (slide 5), recommendation (slide 6) and sources (slide 7). I did not view the rendered slides. The builder reports font sizes of 30pt for titles and 22pt for body text; I did not check them. |
| `07-deliverables/data.xlsx` | PASS | Checker: sheets "Monthly metrics" (16 rows) and "Survey" (9 rows). Column names match the spec exactly. I compared the 12 monthly rows and the 5 survey rows against `pilot-metrics.csv` and `research-notes.md`; all match. |
| `07-deliverables/build/*.py` | Present | `common.py`, `build_docx.py`, `build_pdf.py`, `build_pptx.py`, `build_xlsx.py` (reported by the builder; not individually reviewed). |

## Brief requirements

| Success criterion | Result | Evidence |
|---|---|---|
| Answers all three research questions from the provided data, with citations | Met | Findings covers output, service and absence (Q1), wellbeing and team differences (Q2), and problems and causes (Q3). Every claim carries [1]–[3]. |
| Reports data limitations (short period, survey response rates) | Met | The Limitations section covers both. It also covers no control group, sick-day comparability, seasons, December baseline, and missing data. |
| Clear recommendation with conditions | Met | Extend for at least six months, with four conditions and a four-point decision test. It is labelled as a judgement with medium confidence. |
| Every number cited and matches source files | Met, subject to the notes below | I recomputed Table 1's operations figures from `pilot-metrics.csv` with a script. All match: units 60,870 → 62,430 (+2.56%); complaints 90 → 76 (−15.56%); sick days 420 → 262 (−37.62%); on-time 93.12 → 94.45 (+1.33); units per head 207.0 → 205.4 (−0.81%); average headcount 49.0 → 50.67; pilot complaints average 12.67; earlier sick-day average 70.0. The limitations figures also match (excluding December: units +1.24%, on-time +1.09, sick days 67.2 → 43.7). The survey figures in Table 1 and `data.xlsx` match the research notes. I did **not** re-check them against `staff-survey-summary.md` itself, so they rest on the researcher, analyst and three reviewers. |
| Spec: report 700–1,100 words | Partly met / depends on the counting method | See Caveats. |
| Spec: sections in order, before/after table | Met | Headings checked in the docx. |
| Spec: slides 5–7, with the required slides and speaker notes | Met | 7 slides, 7 with notes. |
| Spec: xlsx sheets and columns | Met | Names match exactly. |

### Spot-checks (three claims against `01-research/research-notes.md` and the source CSV)
1. Sick days 420 → 262 (−37.6%): matches the notes and my recomputation.
2. Units per head 207.0 → 205.4 (−0.8%), with average headcount about 49 → about 51: matches.
3. Weak-baseline claim (excluding December, units +1.2%, on-time +1.09, sick days 67.2 → 43.7): matches.

## Caveats on the word count
The spec sets 700–1,100 words and does not say whether References and the table count. Counts for the report:
- My whitespace count of the docx paragraphs, including title and References but not the table: 994 words. Before References: 916 words. Table text: 84 words. Together that is about 1,078 words.
- Checker: docx 1,122 words, PDF 1,093 words. The docx figure is over 1,100. The checker probably counts the table, title and path-like tokens differently.
- Builder's count of `report.md`: 1,099 words, which is 1 under the cap.
- The body without References and the table is well inside the range on every count. The whole-document total sits at or just over the cap depending on the tool. **The board owner should decide which count applies.**

## Unresolved review issues (from review-3, verdict PASS)
- **P1 (minor):** Recommendation condition 3 says "Collect monthly operations data from July 2026". July 2026 is already past and the data ends in June, which conflicts with it. Left open on purpose. It appears in `report.docx`, `report.pdf` and slides. Fix: change it to "from the start of the extension".
- **P2 (minor):** The slide 7 speaker note says the files are "internal and unaudited". The sources do not support "unaudited". Per `format-notes.md` and the builder, this is still in `slides.pptx`. I did not read the notes text myself because the checker dump does not show it.

## Evidence gaps (carried from `01-research/research-notes.md`)
- No control group. The hire, the shorter meetings and the Monday–Thursday re-planning cannot be separated from the four-day week.
- No seasonality baseline (no January–June 2025 data).
- December 2025 is the weakest month on all four operations measures, which flatters the comparison.
- June 2026 complaints spike (18): the cause is one manager's judgement. There is no complaint-level data and no data after June.
- No pre-pilot team-level survey. Customer service's June score (3.1, n=8) cannot be compared with an earlier score.
- Anonymous survey. Response rates are 82% (December) and 73% (June).
- No queue-time or Friday-specific data.
- No team-level operations data.
- No cost, pay, turnover or hours-worked data.
- On-time % and sick days are not defined. On-time % is an unweighted monthly average.

## Failed or skipped checks
- I did not look at the rendered PDF or slides (layout, overflow, readability). The checker confirms only that files exist, open and have content.
- The checker dump was cut off partway through the docx and PDF text. I did not see the end of the References in either file.
- I did not recheck the survey numbers against `staff-survey-summary.md` (see above).
- Slide speaker-note text and slide font sizes were not read by me.
- File sizes were not checked.

## Tools and capabilities unavailable
- Web search and fetch: not used, because the brief forbids external sources.
- Python libraries `python-docx`, `python-pptx`, `openpyxl` and `reportlab` imported and worked after the permission fix.
- Visual rendering (PDF or slides to images) was not attempted.
- Step 7 was blocked on the first run because Bash permissions were not loaded. It succeeded on the resume.
