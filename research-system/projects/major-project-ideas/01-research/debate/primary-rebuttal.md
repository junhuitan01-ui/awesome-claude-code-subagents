# Primary rebuttal (John, step 1c)

This rebuttal cites only [S#] IDs from `sources.md` and [I#] IDs from `independent-sources.md`. It uses no new research.

## Opening statement
- **It answers RQ1 from the assessors' own documents.** The brief asks what "capstone and final-year project guides and assessors value". My report answers that from three accreditation bodies in three countries [S1][S2][S3], two university rubrics with weights or criteria [S4][S5] and four official module or handbook pages [S6][S7][S8]. Jane's report "deliberately did not cover" accreditation criteria or formal marking rubrics (her §2). Her RQ1 evidence on what assessors value comes from one supervisor's personal page [I7] and one department's supervisor guidance [I9].
- **It covers every addition the brief names, each tied to a published standard.** Accessibility is tied to WCAG 2.2 [S10] and WebAIM [S11]. Security is tied to the OWASP Top 10 [S13]. Ethics is tied to ABET, BCS and Engineers Australia [S1][S2][S3]. Sustainability is tied to Engineers Australia [S3] and ISO/IEC 21031 SCI [S14]. Testing and CI are tied to BCS [S2] and a classroom study [S19]. Evaluation is tied to [S2][S4][S5]. Documentation is tied to [S3][S6]. Jane records explicit evidence gaps for sustainability and deployment, and covers security only through a vendor report on leaked secrets [I18].
- **Its sources fit the brief's preferences better.** The brief names "university capstone or final-year project handbooks and marking rubrics, accreditation or professional bodies (e.g. ABET, ACM, IEEE, Engineers Australia, W3C)". My report uses ABET, BCS, Engineers Australia, W3C and four universities. Jane relies on a Wikipedia page [I4], a personal blog [I8], a vendor report [I18] and a secondary blog report of a 1994 study [I17]. She also uses two sources from before 2015 for central cost claims [I3][I12].
- **It gives the writer what the deliverable needs.** The report needs a table of at least eight ideas with sources, and a prioritisation method. My Q2 list has 12 additions, each with a standard or rubric behind it. My Q3 gives MoSCoW with effort limits [S9] plus documented early-scoping checkpoints [S6][S7][S8][S20].
- **It is complete and consistently structured.** Every finding carries a confidence tag. Conflicts, gaps and the "Not verified" list are filled in. Jane's §4 ("To be completed in the debate round") and §7 ("Not yet compared") are empty placeholders.

## Strongest points
1. **Three accreditation bodies converge.** ABET, BCS and Engineers Australia independently name the same qualities [S1][S2][S3]:
   - design within constraints and to standards;
   - experimentation or testing and evaluation;
   - communication and documentation;
   - ethics;
   - project and risk management.
2. **Actual mark weights.** Trinity College Dublin gives 15% to "Testing, evaluation, critical analysis & conclusions" and 50% to technical execution, and its top band asks for "an element of originality" [S4]. Oxford's first-class criteria ask for "a significant amount of analysis or assessment of results" [S5]. This turns "evaluation matters" from a supervisor's opinion into marking policy.
3. **Process and reflection are assessed, not optional.**
   - Warwick weights a separate project management report at 10% [S6].
   - BCS requires "evaluation (with hindsight)" and "critical self-evaluation of the process" [S2].
   - UCL lists "realistic work commitments" as a learning outcome [S7].
4. **Standards-based extras with concrete targets.**
   - WCAG 2.2 level AA, a W3C Recommendation since 12 December 2024 [S10].
   - OWASP Top 10:2021 categories [S13].
   - The SCI formula, (E × I + M) per R [S14].
   
   ABET explicitly requires "appropriate engineering standards" in the culminating design experience [S1], so using a named standard is itself something assessors credit.
5. **Prioritisation backed by an owner-published method and by real checkpoints.**
   - MoSCoW: Must Haves typically no more than 60% of effort, about 20% kept as Could-Have contingency [S9].
   - Supervisor-approved plans and interim reports [S6][S7], a week-7 demonstration [S8], and approved proposals that resolve scope disputes [S20].

## Challenges to the other report

| Their claim (quote + location) | Problem | Evidence | Severity |
|---|---|---|---|
| "Accreditation criteria (ABET, Engineers Australia) and formal marking rubrics were not covered. Those belong to the primary angle." (§2) | **Missing question.** RQ1 asks what assessors value. Leaving out rubrics leaves that half of RQ1 resting on [I7] (a personal supervisor page) and [I9] (one department). | [S1][S2][S3][S4][S5][S6][S7] | major |
| "Your marks come from your dissertation, not your project" and "The evaluation is very important." (§3 RQ1, citing [I7]) | **Weak source; not generalised.** This is one Cambridge supervisor's undated personal guidance. It is directionally consistent with rubrics, but the rubrics say it with weights: TCD's report-writing criterion is 10% and its technical execution 50% [S4], so "marks come from the dissertation" overstates it for other institutions. | [S4][S5][S7] | minor |
| "No evidence was found on sustainability as an addition. [EVIDENCE GAP: sustainability addition — none found from this angle]" (§8) | **Missing coverage of a topic the brief names.** Engineers Australia element 2.4f, ABET outcome 2 ("environmental ... factors") and ISO/IEC 21031 SCI give both the reason and a concrete method. | [S1][S3][S14] | major |
| "No evidence was found on deployment as an addition, beyond secrets hygiene." (§8) | **Partly missing.** My support is also indirect, but BCS asks that a project "meets a real need in a wider context" and that CITP graduates can "deploy, verify and maintain information systems". | [S2] | minor |
| Security covered only via "28,649,024 new secrets detected in public GitHub commits in 2025" (§3 RQ2, [I18]) | **Weak, commercially interested source** (Jane flags this herself). It covers a single narrow risk; there is no standard such as OWASP for the wider security idea the brief asks about. | [S13] | minor |
| TDD code "60 to 90 percent better in terms of defect density" but "15 to 35 percent longer" (§3 RQ2, [I12]); recommended in §9 as an anchor for effort ratings | **Outdated and on the wrong population.** It is a 2009 blog summary of professional teams, outside the brief's "roughly 2015 onward" window. Jane caveats this, but still proposes it as an effort anchor for students. The student-sample CI study is closer to the audience. | [S19] | minor |
| "Gold plating" defined via Wikipedia (§3 RQ4, [I4]) | **Low-reliability tertiary source.** The brief prefers official and peer-reviewed sources; the underlying book was not opened. The definition is harmless but carries little weight. | — | minor |
| Honours students estimated 33.9 days, actual 55.5 (§3 RQ3, [I17]) | **Secondary report of a 1994 study**, well outside the window. The original was not opened (her own "Not verified" list). | — | minor |
| "students and newcomers underestimate time [I3][I6][I11][I17]" rated "Moderate-to-high" confidence (§8) | **Overreach in tagging.** [I3] measures "scheduling conflicts" and "lack of time management" as team barriers, and [I6] codes "time aspects and timeliness". Neither measures underestimation as such. Only [I11] and [I17] address underestimation, and [I17] is a 1994 study reported second-hand. | [I3][I6][S17][S20] | minor |
| §4 "To be completed in the debate round"; §7 "Not yet compared" | **Structure.** These are empty sections in the delivered report. | — | minor |

## Concessions
- **Jane's evidence on what students under-deliver is stronger than mine.** Sedelmaier & Landes [I6] is a systematic coding of 79 post-mortem reports. It finds that "technical issues tend to be less challenging than non-technical ones", with time (26.15%), documentation (21.77%) and requirements (20.16%) leading. My under-delivery evidence is thinner: introductory students [S18], a small CI study [S19], a preliminary survey [S16], one instructor reflection [S17] and an undated resource [S22]. [I6] should be carried over.
- **Her cost and trade-off framing is a real contribution I lack.** My report has no cost evidence. The following help the Effort column, which I flagged as unsourced:
  - [I13]: five users for qualitative tests, versus "usually more than 30" for quantitative ones;
  - [I15]: "96% of all errors detected fall into these six categories";
  - [I16]: ethics review "can take up to three weeks".
- **[I13] is the better user-testing source.** It is a 2021 NN/g update stating the qualitative-only limit. My [S12] dates from 2000, and I listed the newer NN/g article as not verified.
- **The ambition-vs-caution conflict is genuine and well reported** [I7][I8][I9]. My report did not surface it. My rubric sources partly inform it, without resolving it:
  - Oxford reserves marks above 80 for "outstanding originality" [S5];
  - TCD's top band asks for "an element of originality" [S4];
  - UCL rewards "realistic work commitments" [S7].
  
  Rubrics reward both originality and realistic commitments, which fits her reconciliation: depth in the core, caution on stated extras.
- **Her "propose modest, list extensions" advice [I7] maps cleanly onto MoSCoW** [I1]/[S9]. It is a more student-friendly version of the method than mine.
- **Points where we agree:**
  - MoSCoW wording and the 60% / 20% figures: [I1] = [S9].
  - The Northeastern scope-change finding: [I5] = [S15].
  - WebAIM 2026 figures: [I15] = [S11].
  - Time management as a common weakness: [I3][I6] with [S17][S20].
  - No source shows any addition raising grades: both reports list this as a gap.
- **Her [I14] caution against the "64% of features unused" statistic is useful.** My report does not use it, and the draft should not.

## Defence
- **"Rubrics value X" is not "students under-deliver X."** I admit my RQ1 under-delivery evidence is the weaker half. It is tagged "single source" or "uncertain" in my notes, and listed as gap 1. Jane's [I6] should fill it.
- **Single-institution rubrics** [S4][S5][S6][S7][S8]. Each is one institution. However, five consistent university documents plus three accreditation bodies is broader agreement than one supervisor page [I7] and one department [I9]. [S8]'s institution and year are inferred from its URL, and I said so.
- **No effort or cost data.** Admitted in my Gaps. Jane's cost sources ([I13][I15][I16]) are the right complement. [I12] needs its date and population caveats kept.
- **Abstract-only reads** of [S15], [S18] and [S21], and the embargoed full text of [S21]. These are disclosed, and the findings drawn from them are tagged accordingly.
- **ACM Code of Ethics not verified.** Admitted. Ethics is still supported by three opened standards [S1][S2][S3], so the ethics idea does not depend on ACM.
- **Some old or dated sources.** BCS guidance is dated 2020 [S2], NN/g 2000 [S12] and OWASP 2021 with a 2025 Release Candidate pending [S13]. All are flagged, and all except [S12] fall within the brief's window.
