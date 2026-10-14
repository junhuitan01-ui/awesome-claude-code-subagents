# Review 1 of projects/example-acme-pilot/03-drafts/draft.md (with slides-outline.md and tables.md)
Verdict: REVISE

## Checks run
- **Numbers.** I recomputed every figure from `pilot-metrics.csv` and `staff-survey-summary.md`. All of these match the raw files and are correct:
  - Totals and averages: units 60,870 vs 62,430 (+2.56%), on-time 93.12% vs 94.45% (+1.33 points), complaints 90 vs 76 (-15.6%), sick days 420 vs 262 (-37.6%).
  - Headcount-months: 294 vs 304. Units per head: 207.0 vs 205.4 (-0.8%).
  - Excluding December: units +1.2%, on-time +1.09 points, sick days 67.2 vs 43.67.
  - Survey scores and changes, response rates (82%, 73%), team scores and n values, and the 6-comment and 5-from-customer-service counts.
  - "December worst on all four measures" is correct.
- **tables.md.** All 12 monthly rows and all 5 survey rows match the raw files. Sheet names and column order match the spec.
- **Citations.** [1], [2] and [3] all exist in `sources.md`. References are in order of first citation. No orphan or invented IDs.
- **Report length.** My hand count of the body, from Executive summary to the end of Recommendation and excluding References, is below. It is within 700–1,100 under every counting method, but the prose-only figure is close to the lower bound. No fix needed.

| Counting method | Words |
|---|---|
| Prose only (no title, headings, table, caption, source line or citation markers) | about 719 |
| Plus Table 1 (57 words), caption (7) and source line (39) | about 822 |
| Plus title and headings | about 845 |
| Plus about 43 citation markers | about 890 |

- **Slides.** There are 7 slides, within the 5–7 limit. All have speaker notes. Title, findings, limitations, recommendation and sources slides are present. No slide has more than 5 bullets. The longest bullet is 9 words (slide 4, "Five of six Friday-cover comments came from customer service"). All are at or under 12 words, excluding citation markers. Slide 7 is the sources slide.
- **Style.** British English is used correctly: judgement, favours, towards. Headings are in sentence case. The numbers rule is followed.

## Findings

| ID | Severity | Location | Problem | Evidence | Required fix |
|----|----------|----------|---------|----------|--------------|
| R1 | major | Draft, Executive summary para 2; Findings (Output) | The sick-day result, which is the headline, omits a caveat the research flagged. A four-day week reduces working days. If "sick days" count working days, the -37.6% (and -39.7% per head) could partly be mechanical. The report only lists "definitions of … sick days" as missing data. It never says working days per week changed. Slide 2 and the slide 5 note also present absence as the strongest result with no such caveat. | research-notes.md "Gaps" (definitions bullet): "the sick-day totals may not be strictly comparable if working days per month differ". analysis.md evidence table, row "Sick days -37.6%": "working days per month may differ". Neither made it into the draft's Limitations or slides. | Add a Limitations point (and a short qualifier in the slide 5 note): sick-day counts may not be comparable because the pilot reduced working days and the file does not define the measure [1]. Qualify "clearest change" and "strongest result" accordingly. No new research needed. |
| R2 | major | Draft, Limitations bullet 1 vs Findings (Problems); also analysis.md line 31 | The report is inconsistent about a hire. Problems says "no extra hire was made" [3]. Limitations says "A March hire … changed during the pilot" [1][3]. [3] says nothing about a March hire. [1] shows only that headcount rose from 50 to 51 in March. Headcount also rose twice before the pilot (48 to 49 to 50). Calling it a "hire" is an inference, and it reads as contradicting the Friday-cover finding. | pilot-metrics.csv: headcount 48, 48, 49, 49, 50, 50, then 50, 50, 51, 51, 51, 51. manager-notes.md April: "No extra hire was made" (about Friday cover). research-notes.md line 123: "The files do not say which role that hire filled." | Reword to "headcount rose from 50 to 51 in March (role not stated) [1]" and cite only [1] for it. Add that no extra Friday-cover hire was made [3], so the two statements do not clash. |
| R3 | major | Draft, Executive summary para 2; Findings (Output) para; Table 1 | The executive summary overstates the evidence in two ways. (a) It says the pilot "cut sick days" and "kept output … at or above earlier levels". "Cut" is causal wording, but the Limitations say effects cannot be separated from other changes or from seasonality. "At or above" is also wrong for output per head, which fell 0.8% and is about 205.4 vs 210.6 excluding December. (b) The Findings text says "headcount also rose from 48 to 51". That compares one month in July 2025 with one in 2026. The right comparison is average headcount, 49.0 vs 50.67. | analysis.md Summary point 2: "output was maintained, not improved", confidence low for "output rose". analysis.md December baseline paragraph (205.4 vs 210.6). research-notes.md "Per-head adjustment" (average headcount 49.0 and 50.67). | Rewrite to: "Sick days fell 37.6% during the pilot, and total output and on-time delivery were maintained or slightly higher, although output per person was flat to slightly lower [1]." Use average headcount (about 49 to about 51) in the Findings sentence. |
| R4 | minor | Draft, Background | "UK" is not defined on first use, but the style guide says to define every acronym. | style-guide.md, Language: "Define every acronym on first use". | Write "United Kingdom (UK)" or just "British site". |
| R5 | minor | Draft, Table 1 and source line; slide 2 | All totals, averages, percentages and per-head figures are the analysts' calculations, not figures in the source files. The report does not say so. The unweighted on-time average is disclosed only in the slide 2 speaker note, not in the report. | pilot-metrics.csv contains monthly values only. research-notes.md line 41: "simple, unweighted average … I did not weight by volume". | Add to the Table 1 source line: "Totals, averages and percentages are calculated from [1]; on-time delivery is an unweighted average of monthly figures." |
| R6 | minor | Draft, Table 1 | The table shows only 3 of the 5 survey measures. It omits "workload manageable" (-0.1) and "would recommend" (+0.6). The omitted measure includes the one that did not improve, which looks selective. The text covers workload, but the table does not. | staff-survey-summary.md has 5 measures. tables.md Survey sheet lists all 5. | Add the two rows to Table 1, or add a note to the source line that the other two measures are in the text and in data.xlsx. |
| R7 | minor | Draft, Findings (Problems), sentence on June | This paraphrase shifts the log's emphasis. The log says most complaints related to slow Friday responses during the recall notice. The manager "judged this mostly a one-off but linked it to thin Friday cover". The draft says the manager "linked this mostly to a recall notice … plus thin Friday cover". | manager-notes.md, June entry. | Reword: "Most related to slow Friday responses during a recall notice issued on a Thursday. The operations manager judged it mostly a one-off but linked it to thin Friday cover [3]." |
| R8 | minor | slides-outline.md, speaker notes for slides 2, 3, 5 and 6 | Several figures in the notes have no citation. Examples: "headcount rose from 48 to 51", "1.2%", "1.09 points", "67.2 to 43.67", "eight respondents" and "No month at 18". The style guide says no citation means no claim. Slide 6's bullet "12.67 a month" is also not labelled as the pilot average. | style-guide.md, Citations. | Add [1] or [2] to the figures in the notes. Change the slide 6 bullet to "Test: complaints at or below pilot average (12.67/month) [1]". |
| R9 | minor | tables.md | The tables have source lines but no numbered captions, which the style guide requires. Some column headers lack units, for example "Sick days" and "Customer complaints". | style-guide.md, Structure ("numbered caption and a source line"); Spreadsheets ("Units in column headers"). The spec fixes the column names, so keep them. | Add numbered captions (for example "Table 2: Monthly metrics, July 2025 to June 2026"). Put units in the sheet note, or add them in brackets only if the spec allows. |
| R10 | minor | Draft, Limitations bullet 3; Decision test list | Decimals are inconsistent: "67.2 to 43.67". The final decision-test bullet ends with a full stop but the other three do not. | style-guide.md (consistency). | Use "67.2 to 43.7" or "67.20 to 43.67". Apply one punctuation style to the list. |
| R11 | minor | Draft, Limitations | The report does not disclose that pay and hours worked under the pilot are not described, so output per hour cannot be assessed. It also does not disclose that non-respondents (9 of 50 and 14 of 51) may differ from respondents. | research-notes.md "Gaps" (cost, revenue, turnover and hours-worked bullet; non-response bullet). | Add one clause to "Missing data" and "Survey limits". No new research needed. |

## Resolved from previous review
Not applicable (round 1).

## Notes
- All findings can be fixed from existing material. None needs new research.
- The remaining uncertainty is about the evidence, not the draft. It is already disclosed, apart from the working-days caveat in R1.
- Word counts are hand counts. Expect a variance of about ±10 against a tool.

**Verdict: REVISE. Findings: 0 blocker, 3 major, 8 minor.**
