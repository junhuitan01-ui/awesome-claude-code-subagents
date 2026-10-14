# Pipeline log — example-acme-pilot

- **Date:** 14 October 2026
- **Project:** example-acme-pilot (fictional test data; files in 00-brief only, no web research)

## Required deliverables
- report.docx — board report (700–1,100 words; sections: Executive summary, Background, Findings, Limitations, Recommendation, References; before/after table)
- report.pdf — PDF copy of the report
- slides.pptx — 5–7 slides; title, key findings, limitations, recommendation, sources; speaker notes
- data.xlsx — sheets "Monthly metrics" and "Survey"

## Success criteria
- Answers all three research questions from provided data, with citations
- Reports data limitations (short period, survey response rates)
- Clear recommendation with conditions
- Every number cited and matches source files

## Steps
- Step 0: orchestrator — brief checked (project-brief, deliverable-spec, style-guide, manager-notes, pilot-metrics.csv, staff-survey-summary.md all present); work folders created. OK.
- Step 1: researcher — 01-research/sources.md, research-notes.md saved. OK. Web search/fetch not used (brief forbids). 3 sources, all in 00-brief. Calculations done by hand by the researcher; to be re-verified by the orchestrator in step 8.
- Step 2: analyst — 02-analysis/analysis.md saved. OK. Analyst re-checked researcher's arithmetic, reported no discrepancies. Recommends: extend pilot with conditions (fix Friday cover). No extra research requested.
- Step 3: writer — 03-drafts/draft.md, slides-outline.md, tables.md saved. OK. Writer's word count (~960) was a manual estimate; to be re-counted.
- Step 4 (round 1): reviewer — 04-reviews/review-1.md saved. Verdict REVISE (0 blocker, 3 major, 8 minor). Findings are actionable (location/problem/evidence/fix). Numbers all verified correct by reviewer; issues are caveats (sick-day working-days), "hire" wording, overstated exec summary.
- Step 5 (cycle 1): improver — 05-revised/revised-1.md, slides-outline-1.md, tables-1.md, changes-1.md saved. Improver reports 11/11 findings fixed; to be confirmed by review-2. Improver hand word count ~835 prose / ~1,045 with everything; to be re-counted.
- Step 4 (round 2): reviewer — 04-reviews/review-2.md saved. Verdict REVISE (0 blocker, 1 major N1, 4 minor N2–N5). R1–R11 all verified resolved. No numeric errors. N1: exec summary/slide 3 imply customer service did not improve, but no pre-pilot team data exists. N4: with References counted, body is ~1,125 words (over 1,100).
- Step 5 (cycle 2, final): improver — 05-revised/revised-2.md, slides-outline-2.md, tables-2.md, changes-2.md saved. Improver reports N1–N5 fixed; to be confirmed by review-3. Improver hand count ~803 prose / ~1,077 incl. References.
- **Resumed after an interruption (14 October 2026).** The earlier run stopped before review-3. This run resumes at Step 4 (round 3) on 05-revised/revised-2.md and appends below.
- Step 4 (round 3): reviewer — 04-reviews/review-3.md saved. Verdict PASS (0 blocker, 0 major, 2 minor). N1–N5 all verified resolved. No numeric errors. Open minor: P1 (condition 3 says "from July 2026", which is already past and conflicts with "no data after June"); P2 (slide 7 note says "unaudited", not supported by sources). Reviewer's whole-document count ~1,070 incl. References (margin ~30); it did not independently recount Limitations/Recommendation.
- Step 6: formatter — 06-formatted/report.md, slides.md, tables/monthly-metrics.csv, tables/survey.csv, format-notes.md saved. OK. Text unchanged from revised-2 (layout only). P1 and P2 left open on purpose and listed in format-notes.md as unresolved.
- Step 7: builder — **BLOCKED, nothing built.** The builder's first Bash call (library check `python3 -c "import docx, pptx, openpyxl, reportlab"`) was denied by the permission system. I tried the same exact command from the orchestrator and it also needed approval, although `.claude/settings.json` lists it as pre-approved. No scripts or deliverables exist; no placeholder files were created. Library availability is unknown.
- Step 8: final validation — **NOT RUN** (no deliverables; checker needs Bash approval). No validation-report.md written.
- Run stopped here pending the user approving Bash commands (python3 checks, build scripts, tools/check_deliverables.py).
- **Resumed after Bash permissions were fixed (14 October 2026).** This run resumes at Step 7 (builder), then Step 8 validation and Step 9 report. Entries below are appended.
- Step 7 (resumed): builder — report.docx, report.pdf, slides.pptx, data.xlsx and build/*.py saved in 07-deliverables/. The builder ran `tools/check_deliverables.py` and all four passed. Text unchanged from 06-formatted, so P1 and P2 are still in the files. Builder's report.md word count was 1,099; the checker counts 1,122 (docx) and 1,093 (PDF). Library check `python3 -c "import docx, pptx, openpyxl, reportlab"` worked on resume.
- Step 8: final validation — I ran the checker with `--dump`; all four files PASS. I recomputed the operations figures from the CSV with a script and they all match; I checked the workbook against the CSV and survey notes. validation-report.md written. Open: P1, P2, word count ambiguous (about 1,078 to 1,122 by method), rendering and survey source recheck not done.
- Step 9: summary reported to the user.
