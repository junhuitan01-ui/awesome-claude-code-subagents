# Review 2 of 05-revised/revised-1.md
Verdict: PASS

| ID | Severity | Location | Problem | Evidence | Required fix |
|----|----------|----------|---------|----------|--------------|
| R12 | minor | §3 intro (line 33), Table 1 row 6 (line 44), table note (line 51), §7 bullet 2 (line 127) | The report says "only four ideas have any source for their cost" (§3 and §7). But only three rows have effort ratings without the (J) label: rows 2, 3 and 4. Row 6 (ethics) is the fourth idea with a cost source: ethics review takes up to three weeks [I16]. Yet its whole effort cell is marked (J), and [I16] is not tied to the "medium" part. A reader who counts the unlabelled rows finds three, not four. The table note also says ratings without (J) "draw partly on a cost source". | analysis.md Table A row 6, Effort basis column: "Judgement; lead time sourced [I16]"; analysis.md conclusion 4 (the four cost-evidenced ideas include ethics-review lead time [I16]) | In row 6, change the effort cell to "Low (written section) (J); medium if a user study needs approval, since review can take up to three weeks [I16]". Or keep the cell as it is and change "four" to "three" in §3 and §7. The first option matches the analysis. |
| R13 | minor | §3, WCAG bullet (line 56) "the W3C web accessibility standard"; Table 1 row 9 (line 48) "SCI is an ISO standard method" | W3C and ISO are used without being written out. The style guide says to define every acronym the first time it is used, and the brief asks for a report a beginner can read. | style-guide.md, Language: "Define every acronym on first use"; project-brief.md success criteria: "no unexplained jargon" | Write "World Wide Web Consortium (W3C)" at its first use in the WCAG bullet. Write "an international (ISO) standard method" in row 9, or spell out International Organization for Standardization (ISO). |

## Resolved from previous review
- **R1 (major): fixed.** §2 now gives each percentage as a share of its own category ("26.15% of codes in that category"; "the most common professional and technical issues"). The quote is kept.
- **R2: fixed.** The sentence now reads "introductory students do not test systematically while believing they do [S18]".
- **R3: fixed.** WCAG, OWASP and SCI are written out at first use in the §3 intro.
- **R4: fixed.** Post-mortem, test-driven development and defect density are now explained. "Analyst's synthesis" is now "our own synthesis of the sources".
- **R5: fixed.** [I7] is now "A Cambridge supervisor", which matches I7 (Chisnall, Department of Computer Science and Technology, University of Cambridge). [I8] is now "writing on his personal blog", and [I9] is the University of Sussex.
- **R6: fixed.** Step 5 now carries the "(low-medium confidence: reported second-hand)" label.
- **R7: fixed.** The method intro now reads "Steps 2–4 are our own synthesis of the sources, not a tested method."
- **R8: fixed.** The exec summary now says "is likely to cost far less".
- **R9: fixed in the text.** The shared documents are cited once each as [S9], [S11] and [S15]. [I1] remains only where the date correction is the point (carry-over point 1, and the [S9] reference note). Note for the Format step: [S9] and [I1] are the same web page, so they should get one reference number.
- **R10: fixed.** Carry-over point 8 now reads "Students and new graduates … (low-medium confidence) [I17][I11]".
- **R11: fixed.** Row 11 now ends "(small, preliminary survey)".

## Notes
- **Length.** Sections 1–7 are 2,488 words with citation tags and 2,461 without (counted with wc on the text from the §1 heading to just before §8). That is within 1,500–2,500, but close to the limit. The fixes for R12 and R13 add about 10 words, which still fits. The improver should recount after editing.
- **Spec checks passed:**
  - **Sections and order:** all required sections are present, in the order the spec gives.
  - **Table 1:** has the columns Idea | Why it helps | Effort (low / medium / high) | Sources, 11 ideas (at least eight needed), a numbered caption and a source line.
  - **Prioritisation method:** a 7-step method is included.
  - **Table 2:** has a caption and a source line.
  - **Research questions:** all four are answered (§2 RQ1, §3 RQ2, §4 RQ3, §5 RQ4).
  - **Debate result:** the result is presented as the verdict decided (4.00 to 3.55). The per-criterion scores match debate-verdict.md, and CO1–CO9 are all present.
  - **"Do not use" items:** still absent ("64%" figure, ACM draft text, OWASP 2025 category names). The p-value for [S15] is still left out.
- **Claims checked again in this pass against the research notes, all consistent:**
  - Trinity weights: 50% technical, 15% testing and evaluation [S4].
  - Oxford's "significant amount of analysis or assessment of results" [S5].
  - Warwick: a 10% project-management report and reflective writing [S6].
  - 79 post-mortem reports at one university [I6].
  - 88 engineering seniors (mechanical engineering) [I3].
  - 73% of students said writing their own tests helped ("most students") [S19].
  - Budgeting had the lowest preparedness rating, mean 5.0 on a 7-point scale [S16].
  - Ethics review can take up to three weeks [I16].
  - Students estimated 33.9 days for their thesis; it took 55.5 days [I17].
  - About 46% of projects changed scope [S15].
  - Supervisors' quotes on ambition [I7][I8][I9].
  - Review 1 had already spot-checked the WebAIM, MoSCoW and [I6] figures on the web; this review did not re-fetch them.
- **Citation IDs:** every ID used in sections 1–7 appears in the reference list and exists in sources.md or independent-sources.md. There are no orphan IDs.
- **Nothing here needs new research.** The open gaps are already disclosed in §7.
