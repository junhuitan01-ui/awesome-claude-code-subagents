# Review 2 of projects/example-acme-pilot/05-revised/revised-1.md (with slides-outline-1.md and tables-1.md)
Verdict: REVISE

## Checks run

I did not rely on changes-1.md. I rechecked against the raw files in `00-brief/`, `01-research/` and `02-analysis/`.

- **Numbers.** I rechecked every figure in the report, Table 1, Table 2, Table 3 and the slide notes against `pilot-metrics.csv` and `staff-survey-summary.md`. All match.
  - Totals and changes: units 60,870 and 62,430 (+2.6%); on-time 93.12% and 94.45% (+1.33 points); complaints 90 and 76 (-15.6%); sick days 420 and 262 (-37.6%).
  - Per head: units 207.0 and 205.4 (-0.8%); average headcount 49.0 and 50.67, shown as "about 49 to about 51".
  - Excluding December: units +1.2%, on-time +1.09 points, sick days 67.2 to 43.7.
  - Other figures: the pilot complaints average of 12.67 and the earlier sick-day average of 70; June complaints 18 and May 9.
  - Survey: five measures and changes; team scores 3.1, 4.1 and 4.0; eight respondents; response rates 82% and 73%; 9 and 14 non-respondents; 6 comments, 5 from customer service.
  - Log facts: the log's wording for April, June, January and February matches.
  - Changed or new numbers: "43.7" is correct rounding of 43.67. "About 49 to about 51" is correct. The new Table 1 rows (workload 3.1 to 3.0, -0.1; recommend 3.4 to 4.0, +0.6) match the survey.
- **tables-1.md.** All 12 monthly rows were checked against the CSV and all match. The 5 survey rows match. Sheet names and column names match the spec exactly. Numbered captions (Table 2, Table 3) and source lines are present. The units gap in the headers is explained in the note, because the spec fixes the column names (a documented conflict with the style guide, acceptable).
- **Citations.** [1], [2] and [3] all exist in sources.md. References are in order of first citation. No invented or orphan IDs.
- **Structure.** The section order is Executive summary, Background, Findings, Limitations, Recommendation, References. The before/after table is present. Headings are in sentence case. British English is used throughout (judgement, favours, towards, programme not used).
- **Slides.** There are 7 slides (spec 5–7), and each has speaker notes. The title, findings, limitations, recommendation and sources slides are present. No slide has more than 5 bullets (slides 3 and 5 have exactly 5). Titles are takeaways.

### Report word count (hand count, my own; not taken from changes-1.md)

Scope: Executive summary to the end of Recommendation. References are excluded, as in round 1.

| Method | Words | Within 700–1,100? |
|---|---|---|
| Prose only (no title, headings, table, caption, source line or citation markers) | about 836 (exec 130, background 60, findings 190, limitations 254, recommendation 202) | Yes |
| Prose + Table 1 (73) + caption (7) + source line (55) | about 971 | Yes |
| Above + title and headings (22) | about 993 | Yes |
| Above + citation markers (about 49) | about 1,042 | Yes |

The changes-1.md hand counts (835, 975, 1,000, 1,045) agree with mine within a few words. The variance is about ±10.

See N4 for the one counting method that could exceed 1,100.

### Slide bullet word counts (excluding citation markers)

Every bullet is 12 words or fewer.

| Slide | Words per bullet |
|---|---|
| 1 | 6, 5, 6, 6 |
| 2 | 6, 5, 6, 8 |
| 3 | 6, 6, 6, 9, 7 |
| 4 | 8, 6, 7, 9 |
| 5 | 7, 6, 8, 8, 7 |
| 6 | 5, 5, 7, 8, 8 |
| 7 | 6, 6 (plus two source lines of about 6 each) |

The longest bullet is 9 words.

## Findings

| ID | Severity | Location | Problem | Evidence | Required fix |
|----|----------|----------|---------|----------|--------------|
| N1 | major | Report, Executive summary para 2 ("Customer service is the exception. Its staff report lower satisfaction"); slides-outline-1 slide 3 title ("Wellbeing improved, except in customer service") | The headline says customer service did not share the wellbeing improvement. The data only show that customer service scored lower than the other teams in June 2026. No pre-pilot team score exists, so the data cannot show whether customer service improved, stayed flat or fell. The slide 3 speaker note and the body of the report already say this ("We cannot tell whether customer service was already lower"), so the headline contradicts the report's own caveat. The Executive summary is the part the board will read. | staff-survey-summary.md: team scores are "June 2026" only, and the December figure is overall. research-notes.md gap: "It cannot be shown whether customer service was already lower before the pilot, or whether it fell." analysis.md open question: "Was customer service satisfaction already lower before the pilot?" | Reword the Executive summary to the supported claim. For example: "Customer service is the weak point: in June its staff scored satisfaction 3.1, against 4.0 and 4.1 for other teams, and Friday cover is thin [2][3]." Retitle slide 3, for example "Wellbeing improved overall; customer service scored lowest". Keep the "cannot tell if already lower" caveat. |
| N2 | minor | Report, Recommendation condition 1 ("Options include a second person on Fridays or a defined escalation route [3]"); Findings, Problems para ("Most related to slow Friday responses… Thursday." has no marker); Executive summary ("A four-day week has fewer working days… [1]") | Three citation-placement problems. (a) The two fix options are the analyst's suggestions, but the marker [3] makes them read as the manager's. The log only says "recommend fixing Friday cover before any permanent change". (b) The "Most related to…" sentence has no marker of its own. The [3] comes only on the next sentence. (c) "Fewer working days" is cited to [1], but [1] says nothing about working days. It is the report's own inference. | manager-notes.md April and Overall entries contain no options. pilot-metrics.csv has no working-days information. style-guide.md: "No citation, no claim." | (a) Move [3] to cover only "Fix Friday cover" and mark the options as "our suggestions", or drop the marker from the options. (b) Add [3] after "Thursday". (c) Cite [1] only for "the file does not define sick days". Present "fewer working days" as the reasoning for the caveat, not as a sourced fact. |
| N3 | minor | References [2] "(HR)"; Executive summary sentence 2 of para 2 and Limitations "Missing data" sentence 1 | (a) "HR" is used without being defined, although R4 applied the "define every acronym" rule to "UK". (b) Two sentences run to about 27 words each, against the style-guide aim of fewer than 25. The "Missing data" list sentence is hard to read for a non-specialist board. | style-guide.md: "Define every acronym on first use". "Short sentences (aim for under 25 words)". The sentences are "Sick days fell 37.6%… lower [1]" (27 words) and "The files give no queue times… assessed" (27 words). | Write "Human resources (HR)" or "Human resources" in [2]. Split the two sentences. For example, end the exec sentence at "slightly higher" and start a new one for output per person. |
| N4 | minor | Report length, whole-document method | Under the four methods asked for, the count is within 700–1,100 (maximum about 1,042). The result is not robust to a broader method. If the docx or PDF word count includes the References section and its heading (about 83 words), the total is about 1,125. That exceeds the spec's 1,100 limit. The spec lists References as one of the report's sections, so a validator could reasonably count it. | My counts above. References [1]–[3] are about 82 words, plus the heading. spec: "Length: 700–1,100 words". | Trim about 30–50 words from the body to give margin. Good candidates are the repeated "see Limitations" and the Findings "Wellbeing" restatement. Alternatively the orchestrator can record the counting convention (References excluded) in the validation report. |
| N5 | minor | slides-outline-1 slide 5 bullet 5 ("Sick-day definition unclear; working days fell") and slide 5 speaker note ("survives the baseline check, though not the working-days question") | (a) The bullet states "working days fell" as fact. The report says only that the file does not say, and that the counts "may not be strictly comparable". The bullet is stronger than the report. (b) The note sentence is unclear. It says the absence result "survives… though not the working-days question", and a board reader will not know what that means. | revised-1.md Limitations "Sick-day comparability". research-notes.md: "whether the four-day week changed the number of working days available" is listed as undefined. | Change the bullet to "Sick-day definition unclear; working days may differ" (7 words). Change the note to "The baseline check does not remove the working-days question." |

## Resolved from previous review

| ID | Status | Verification |
|----|--------|--------------|
| R1 | Resolved | The Executive summary now carries the caveat. A "Sick-day comparability" limitation was added. "Clearest change" became "largest change, but the measure may not be comparable". The slide 2 title now says "output was maintained". The slide 2 and slide 5 notes and a slide 5 bullet carry the working-days caveat. N5 is a small wording issue on the new slide 5 bullet. |
| R2 | Resolved | The Limitations bullet now reads "Headcount rose from 50 to 51 in March (role not stated) [1]". [3] is cited only for meetings and planning, and "No extra Friday-cover hire was made [3]" is stated. This matches the CSV and the log. |
| R3 | Resolved | The Executive summary uses the wording suggested in R3. "Cut" and "at or above" are gone. The Findings text uses average headcount (about 49 to about 51), which matches 49.0 and 50.67. |
| R4 | Resolved | "UK" was changed to "British site". N3 notes a similar undefined acronym ("HR") in References. |
| R5 | Resolved | The Table 1 source line states that totals, averages and percentages are calculated from [1] and that the on-time average is unweighted. The slide 2 note repeats it. |
| R6 | Resolved | Table 1 now has all 5 survey rows, with correct values. |
| R7 | Resolved | The June sentence now follows the log ("Most related to slow Friday responses… The operations manager judged it mostly a one-off but linked it to thin Friday cover [3]"). The slide 4 note agrees. The first sentence still lacks its own marker (see N2b). |
| R8 | Resolved | Citations were added to the headcount, 1.2%, 1.09 points, 67.2 to 43.7, eight respondents, 18 complaints and 70 figures in the notes. The slide 6 bullet reads "pilot average (12.67/month) [1]". |
| R9 | Resolved | Table 2 and Table 3 have numbered captions and source lines. The unit definitions are in the sheet note. The spec fixes the column names, so this is acceptable. |
| R10 | Resolved | "43.7" is used consistently in the report and slide 5 note. The decision-test bullets use one punctuation style (none). |
| R11 | Resolved | "Missing data" now mentions pay and hours worked and that output per hour cannot be assessed. "Survey limits" now mentions that the nine and 14 non-respondents may differ. |

The changes-1.md claims of "11 fixed" are borne out. Its word counts are accurate within the stated tolerance.

## Notes
- N1, N2, N3 and N5 can be fixed from existing material. N4 needs a small trim, or a recorded convention for what the word count covers. None needs new research.
- No new factual or numerical errors were found in the revision. All remaining issues are wording or claim-strength issues.
- N1 is the only major finding. It stems from the analysis ("not for customer service") and was not caught in round 1. If it is not fixed in the final round, it should be listed as unresolved.
- Word counts are hand counts, with a variance of about ±10.

**Verdict: REVISE. Findings: 0 blocker, 1 major, 4 minor.**
