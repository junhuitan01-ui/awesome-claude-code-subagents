# Review 3 of projects/example-acme-pilot/05-revised/revised-2.md
Verdict: PASS

Companions reviewed: `05-revised/slides-outline-2.md` and `05-revised/tables-2.md`. I verified against the raw files in `00-brief/` and `01-research/sources.md`, not against `changes-2.md`. I did not re-open `research-notes.md` or `analysis.md`. Every claim was checked against the raw brief files, which are the ground truth. The numbers do not depend on the notes.

## Checks run

### Numbers (recomputed from `pilot-metrics.csv` and `staff-survey-summary.md`)
All figures match.
- **Units:** before 60,870, pilot 62,430 (+2.56%, shown as +2.6%).
- **Headcount:** sums are 294 and 304, so averages are 49.0 and 50.67 ("about 49 to about 51").
- **Units per head:** 207.04 and 205.36 (-0.8%).
- **On-time delivery:** 558.7/6 = 93.12% and 566.7/6 = 94.45% (+1.33 points).
- **Complaints:** 90 and 76 (-15.6%). The pilot average is 12.67 a month. June is 18 and May is 9.
- **Sick days:** 420 and 262 (-37.6%). The earlier average is 70 a month.
- **Excluding December:**
  - Units: 51,390/5 = 10,278 against 10,405, a rise of 1.2%.
  - On-time delivery: 93.36% against 94.45%, a gain of 1.09 points.
  - Sick days: 67.2 against 43.67 (43.7).
  - December 2025 is the worst month on all four measures across the 12 months. This holds: lowest units, lowest on-time delivery, highest complaints and highest sick days.
- **Survey:**
  - The five measures and their changes match. Workload is 3.1 to 3.0 (-0.1) and recommend is 3.4 to 4.0 (+0.6).
  - Team scores are 3.1, 4.1 and 4.0, with n=8 for customer service.
  - Response rates are 82% (41 of 50) and 73% (37 of 51), with 9 and 14 non-respondents.
  - Comments: 6, of which 5 are from customer service.
- **Log facts:** April (one person on Fridays, queue times rose, no extra hire), June (Thursday recall, one-off but thin cover), January (two-week adjustment, small dip) and the "Overall" recommendation all match `manager-notes.md`.
- **Headcount in March:** 50 to 51 matches the CSV.
- **tables-2.md:** all 12 monthly rows match the CSV and all 5 survey rows match. Sheet names and column names match the spec exactly. Numbered captions and source lines are present. The missing units in the spec-fixed headers are explained in the note, which is acceptable.

### Citations
[1], [2] and [3] all exist in `sources.md`. References are in order of first citation. There are no orphan or invented IDs. The [2] author is now "Human resources, HR", which matches the sources file. The accessed date and file paths match `sources.md`. The claim-level markers are placed correctly:
- [1] follows only "the file does not define sick days".
- [3] follows "Thursday".
- [3] is on the "Fix Friday cover" recommendation only.
- The fix options are labelled "Our suggestions".

### Structure and style
- **Report sections:** the order is Executive summary, Background, Findings, Limitations, Recommendation, References. The before/after table is present (Table 1) with a numbered caption and a source line.
- **Style:** headings are in sentence case and spelling is British (judgement, favours, towards). Numbers follow the words-under-10 rule. HR is defined on first use in [2]. I checked the longest sentences. None is over about 24 words (the Limitations survey-limits sentence is the longest).
- **Slides:** there are 7 slides (spec 5–7). Every slide has speaker notes. The title, key findings, limitations, recommendation and sources slides are all present, with sources last. The maximum is 5 bullets, on slides 3, 5 and 6.
- **Bullet words:** every bullet is 12 words or fewer, excluding markers. The longest is slide 3 bullet 4 at 11 words. Others are 8 or fewer. Titles are takeaways.
- **Spreadsheet:** the Source column is present, and so are the sheet and column names the spec requires.

### Word count (my own hand count, ±10)
Method: I counted whitespace-separated tokens by hand per section.

| Method | Words | Within 700–1,100? |
|---|---|---|
| Prose only (no title, headings, table, caption, source line or markers). Exec about 136, Background about 56, Findings about 194, Limitations and Recommendation about 410 together | about 800 | Yes |
| + Table 1 (about 73) + caption (7) + source line (about 45) | about 925 | Yes |
| + title and headings (about 23) | about 948 | Yes |
| + citation markers outside the table (about 41) | about 990 | Yes |
| + References section and heading (about 80; [1] 29, [2] 25, [3] 23, heading 1, with file paths counted as one token each) | about 1,070 | Yes |

I counted Executive summary, Background and Findings section by section, and they agree with changes-2.md (138, 55, 196). I did not recount Limitations and Recommendation line by line; I took the sections to be consistent with changes-2.md (230 and 184) after the trims it describes. This is a check, not an independent recount of those two sections.

The whole-document count including References is about 1,070. That is inside the limit with a margin of about 30 words. A tool that splits file paths on `/` and `-` could add roughly 20–40 words and reach the limit. Note this for validation; it is not a defect in the draft.

## Findings

| ID | Severity | Location | Problem | Evidence | Required fix |
|----|----------|----------|---------|----------|--------------|
| P1 | minor | Report, Recommendation condition 3 ("Collect monthly operations data from July 2026") | The date is inconsistent with the rest of the report. The pilot data ends in June 2026, and the report states "No data exists after June". The references are accessed 14 October 2026. "From July 2026" would already be in the past. The start of the extension is not stated. A board cannot tell whether July to October data should exist, or whether the extension starts at some later date. | `pilot-metrics.csv` (last row 2026-06; exported 3 July 2026). revised-2 Limitations "No data exists after June [1]". References accessed 14 October 2026. | Change to "from the start of the extension", or state the start date if the board has set one. This needs no new research. |
| P2 | minor | slides-outline-2 slide 7 speaker note ("All three sources are internal and unaudited") | "Unaudited" is not stated in any source file or in `sources.md`. It is an inference. The reliability ratings in the same note do match `sources.md` (medium, medium, low to medium). | `sources.md` reliability lines for [1]–[3]. No audit status appears in the CSV, survey summary or log. | Replace "unaudited" with "internal, and their definitions are not stated" (supported by `sources.md` [1]), or delete the word. |

## Resolved from previous review

| ID | Status | Verification |
|----|--------|--------------|
| N1 (major) | Resolved | The Executive summary now says customer service "scored lowest on job satisfaction in June (3.1, against 4.0 and 4.1 elsewhere)" and "Whether its score improved is unknown." The Wellbeing section says "No earlier team scores exist, so we cannot tell if customer service was already lower or has improved [2]." Slide 3 is retitled "Wellbeing improved overall; customer service scored lowest". The slide 3 note says "or whether it improved". The slide 4 note says the link to Friday cover cannot be shown. The decision-test bullet says "job satisfaction", which is what the survey team scores measure. No claim of non-improvement remains. |
| N2 (minor) | Resolved | (a) Fix options are labelled "Our suggestions", and [3] covers only the "Fix Friday cover" recommendation. (b) [3] now follows "Thursday". (c) [1] covers only "does not define sick days". The "fewer working days" reasoning is unmarked in the Executive summary, Limitations, and the slide 2 and 5 notes. |
| N3 (minor) | Resolved | [2] reads "Human resources, HR". The long sentences were split. I found none over about 24 words. |
| N4 (minor) | Resolved | The whole-document count including References is now about 1,070. In review 2 it was about 1,125. The remaining margin is thin (see Notes). |
| N5 (minor) | Resolved | Slide 5 bullet 5 now reads "Sick-day definition unclear; working days may differ". The note reads "The baseline check does not remove the working-days question. The output result is weaker." |

The changes-2.md claim of "all five fixed" holds. Its hand counts are consistent with mine within the stated tolerance for the sections I recounted. The "no new facts" statement holds.

## Notes
- Both findings are wording or consistency issues. Neither needs new research.
- The limits stated in the report are not hidden. These are the sick-day comparability, the weak December baseline, the missing control group, the survey being a summary only, and the single-manager source for the June cause.
- The word count is within the limit under every method tried, including References. The margin is about 30 words against the 1,100 cap. If the validation tool counts file paths in a way that splits them, re-check it. The report body is the better place to trim if needed.
- Key claims such as the Friday-cover cause rest on [3], a low-to-medium reliability source. The report discloses this and also cites [2] for the corroborating comments.

**Verdict: PASS. Findings: 0 blocker, 0 major, 2 minor.**
