# Format notes: major-project-ideas

**Input:** 05-revised/revised-1.md (review 2 verdict: PASS)
**Output:** 06-formatted/report.md
**Deliverables in spec:** report.docx and report.pdf. No slides or spreadsheets are required, so there is no slides.md and no tables/*.csv.
**Date:** 14 October 2026

## Rules applied

### Structure (deliverable spec)
- The required sections appear in the order the spec gives:
  1. Executive summary
  2. What makes a major project strong
  3. Additional ideas
  4. How to choose and scope your additions
  5. Risks and how to manage them
  6. How this report was made
  7. Limitations
  8. References
- Headings are numbered (the report is over 1,500 words) and in sentence case. The title is unchanged.
- The line "*Revised draft (revision 1), 14 October 2026*" is replaced with the plain date line "14 October 2026".
- Table 1 keeps the required columns: Idea | Why it helps | Effort (low / medium / high) | Sources. It has a numbered caption and a source line.
- Table 2 has a numbered caption and a source line.
- The 7-step prioritisation method is kept.

### Length
- Sections 1–7 are 2,472 words, counted with wc on the text from the §1 heading to just before §8, with citation tags removed. This is within the 1,500–2,500 limit.
- If table pipes, list markers and other markup are also excluded, the count is 2,287 words.
- If citation tags are counted as words, the count is 2,556. That is because grouped citations are now separated by ", ". Review 2 counted 2,488 with tags, but there the tags were written together with no spaces (for example [S1][S2]).

### Citations
- All [S#] and [I#] IDs are converted to numbered citations [1]–[33], in order of first citation. A script checked that the numbers appear in strictly increasing order of first use.
- Grouped citations are sorted in ascending order and separated by ", ". Runs of three or more consecutive numbers are written as ranges, for example [1]–[8].
- Sources that share a URL get one number:
  - [S9] and [I1] are the same page. Both are cited, and both became [15]. The entry uses the corrected date (28 May 2026, from I1).
  - [S11] and [I15] share a URL, and so do [S15] and [I5]. Only [S11] (now [13]) and [S15] (now [31]) are cited, so [I15] and [I5] are not listed.
- The reference list includes only cited sources: all 22 S-sources and 11 I-sources (I1 merged with S9). These sources were not cited and are left out: I2, I4, I5, I10, I15 and I18.
- Every entry follows the format `[n] Author/Organisation. (Year). Title. Publisher. URL (accessed 14 October 2026).`
  - Undated sources use "(n.d.)" in place of the draft's "undated".
  - [27] keeps "(c. 2018)" and [28] keeps "(2026, in press)", as recorded in sources.md.
  - Where the source lists record a DOI or page range, it is kept.
  - [8] keeps the note that its institution and year are inferred from the URL.
- One wording change came with renumbering in §7, "Partial reading". "[S21]'s full text" became "The full text of [28]". The three abstract-only sources are now listed in ascending order: [16], [28], [31].

### Acronyms (style guide; review 2, R13)
- R13 is applied:
  - "World Wide Web Consortium (W3C)" is spelled out at first use (§3, WCAG bullet).
  - "International Organization for Standardization (ISO)" is spelled out at first use (Table 1, row 9). The cell now reads "SCI is a method standardised by the International Organization for Standardization (ISO)".
- Two more acronyms were defined at first use: "information technology (IT)" in §2, and "University College London (UCL)" in §2.
- WCAG, OWASP, SCI, CI and MoSCoW were already defined in the draft.

### Unchanged
- Both [EVIDENCE GAP: ...] markers stay visible in §7.
- No facts, figures, quotes or confidence labels were added, removed or changed.
- British spelling, the number style and the date style were already compliant. No changes were needed.

## Open issues for the orchestrator

- **R12 (review 2, minor, content issue; not changed by Format).** §3 and §7 say "only four ideas have any source for their cost". But only three rows in Table 1 (rows 2, 3 and 4) have effort ratings without the (J) label. Row 6 (ethics) is the fourth cost-evidenced idea: its lead time comes from [19] (I16). Yet its whole effort cell is marked (J), and [19] is not tied to the "medium" part.
  - Review 2 suggests changing the row 6 effort cell to: "Low (written section) (J); medium if a user study needs approval, since review can take up to three weeks [19]".
  - The alternative is to change "four" to "three" in §3 and §7.
  - This is a content decision, so it is left for the orchestrator or improver.
- **Unchecked edition.** The reference for [2] (BCS, 2020) notes in sources.md that a newer edition may exist. This was not checked. It is already covered in spirit by §7, which lists the OWASP edition as not checked.

## Style rules not fully applied

1. **"Define every acronym on first use": partly applied.**
   - UK and US are left as they are: they are standard country abbreviations.
   - BCS, ABET and OWASP Top 10 are proper names. BCS and ABET are described in the text rather than expanded.
   - README is a file name.
   - In the reference list, venue and organisation names stay as published: ASEE, ASEE CIEC, IEEE/ACM ICSE-SEET, FIE, ICSEA, IARIA, CSEDU, NSF, ACM and EPCOS. Expanding them would change the published titles.
2. **"Prefer short sentences (aim for under 25 words)": not enforced.** A few sentences are longer, for example:
   - the post-mortem findings sentence in §2;
   - the ABET standards sentence in the §3 intro.

   Splitting them risks changing meaning or quotations in an approved draft.
3. **"Every fact, figure and quote needs a citation": one exception.** The debate result in §6 (scores 4.00 to 3.55, per-criterion scores) has no numbered citation. It comes from this pipeline's own 02-analysis/debate-verdict.md, not from an external source, so it cannot go in the reference list. Review 2 confirmed it matches debate-verdict.md.
