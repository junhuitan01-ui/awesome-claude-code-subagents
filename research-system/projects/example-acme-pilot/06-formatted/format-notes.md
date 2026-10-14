# Format notes: example-acme-pilot

Input: `05-revised/revised-2.md`, `slides-outline-2.md`, `tables-2.md` (review-3 verdict PASS).

## Open issues (deliberately not fixed, as instructed)
- **P1 (minor).** Report, Recommendation condition 3 still reads "from July 2026". It conflicts with "No data exists after June" and with the 14 October 2026 access date. Review fix: "from the start of the extension", or state the start date.
- **P2 (minor).** Slide 7 speaker note still says "internal and unaudited". "Unaudited" is not in any source. Review fix: "internal, and their definitions are not stated", or delete the word.

## Changes made
- Report: wording, numbers, caveats, citations and the reference list are unchanged from revised-2. Only layout was normalised (heading levels, bold caption for Table 1, numbered conditions, bullet lists). Table 1 keeps its numbered caption and source line. All sections are in the required order. The three references are all cited, in order of first citation.
- Slides: renamed headings to `## Slide N: Title` and the speaker-note label to `Notes:`. Added a file title. Slide wording is unchanged. There are 7 slides, none with more than 5 bullets or any bullet over 12 words, and sources are last.
- Tables: the CSV blocks from tables-2.md are saved as two files with the exact spec column names. The captions and notes from tables-2.md are not in the CSVs (they would break the header row). The builder should add them as below.
  - Monthly metrics sheet: "Table 2: Monthly metrics, July 2025 to June 2026". Note: Before = July to December 2025; Pilot = January to June 2026. Units shipped are units per month, complaints are a count per month, and sick days are days per month. The file does not define sick days, and working days per month may differ between periods.
  - Survey sheet: "Table 3: Staff wellbeing survey, December 2025 and June 2026". Note: Before = December 2025 (41 of 50 responded, 82%). After = June 2026 (37 of 51 responded, reported as 73%). Five is the best score. The survey is anonymous, so respondents may differ between rounds.
  - Both sheets need a bold header row, no merged cells and a Source line.
- Style rules applied: British English, sentence-case headings, numbered citations [1]-[3], and the numbers rule (words for one to nine, digits for 10 and above and with units).

## Possible factual or consistency points (not changed)
- Word count: review-3 estimates about 1,070 words including References, against a 1,100 cap. A tool that splits file paths on `/` and `-` could push it near or over the limit. Re-check at validation. Trim the report body if needed.
- Background sentence "single British site" and "All data is fictional test data" have no citation marker. No source file states this.
- Slide 5 bullet 5 ("Sick-day definition unclear; working days may differ") and slide 6 bullets 1 to 4 carry no citation. They are recommendations or restate the cited limits.
- Reference [2]'s author reads "Human resources, HR", while `sources.md` has "HR". This was approved in review-3 (N3), so it is unchanged.
- Spec and style tension: the spec-fixed column names lack units for Units shipped, Customer complaints and Sick days. The style guide asks for units in headers. The spec was followed.

## Style rules not applied
- "Units in column headers" for three monthly-metrics columns (spec names take precedence).
- Header-row bold and no merged cells apply to the xlsx and cannot be set in CSV. This is for the builder.
