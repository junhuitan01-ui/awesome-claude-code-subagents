# Analysis — major-project-ideas

**Date:** 14 October 2026
**Built on:** the primary report (John, [S#]), with carry-over points CO1–CO9 from the independent report (Jane, [I#]). See `debate-verdict.md`.

## Summary of conclusions
1. **Assessors consistently reward five qualities beyond the working artefact:** evaluation and analysis of results; testing, or verification and validation; documentation and communication; ethics and professional issues; and planning or project management. Three accreditation bodies in three countries and several universities' rubrics or module pages name them, some with explicit mark weights. **Confidence: high** [S1][S2][S3][S4][S5][S6][S7][S8]; supervisor-level support [I7][I9].
2. **Students fall short mainly on non-technical work:** time management, documentation, requirements, systematic testing and evidence-backed conclusions. Most sources are single-institution, small or practitioner reports. **Confidence: medium** [I6][I3][S17][S20][S22][S18][S19][S16].
3. **The strongest additions are the ones that improve an assessed quality and can be evidenced against a named standard.** These are evaluation and reflection, user testing, accessibility to WCAG 2.2 AA, automated testing, an OWASP-based security review, an ethics section, a risk register, and sustainability using SCI. Only claims backed by evidence earn credit. No source measures how much any addition raises a grade, so this rests on what standards and rubrics value, not on outcome data. **Confidence: medium** [S1][S2][S4][S5][S10][S11][S13][S14][S17]; gap shared by both reports.
4. **Effort can be partly evidenced for four ideas; everything else is judgement.** The four are: qualitative user testing (five users per round) vs quantitative testing (>30 users) [I13]; a basic accessibility pass vs full conformance [S11][I15]; the time cost of automated testing (+15–35%, professional teams, 2009) [I12]; and ethics-review lead time (up to three weeks or more, one department) [I16]. **Confidence: high that this is the limit of the evidence; low-medium for the cost figures themselves** (each is single-source, and some are dated or from non-student settings).
5. **A practical way to prioritise:** MoSCoW, with Must Haves ≤60% of effort and about 20% kept as Could-Have contingency. Combine it with a modest stated scope plus listed extensions, a scope agreed in writing early with the supervisor, and regular checkpoints. **Confidence: medium.** The method comes from one industry source, not tested on students [S9]=[I1]; the scoping practices are documented at several universities [S6][S7][S8][S20]; the "modest proposal" advice comes from a supervisor [I7].
6. **The main risks of adding extras** are time overrun and late failure, extras done only for show or without evidence, ethics-review lead time, and extras crowding out the core artefact that carries most marks. These are managed by contingency, early milestones, and evaluating every addition. **Confidence: medium** [S22][S17][S20][S11][S4][I16][I17][I11].
7. **Changing scope is not harmful in itself, and ambition belongs in the core problem, not in bolt-ons.** One capstone study found no outcome penalty for teams that changed scope. Rubrics reward both originality and realistic commitments. **Confidence: low-medium** (one abstract-only study; the ambition advice is a reconciliation of conflicting opinions) [S15]=[I5][S4][S5][S7][I7][I8][I9].

## Debate result
John's primary report wins with 4.00 against 3.55. His report answers all four research questions from the source types the brief prefers: accreditation bodies, university rubrics and standards. Jane's report is strongest on cost, trade-offs and risk, but it deliberately leaves out assessors' own documents, has gaps on sustainability and deployment, and relies more on weak or pre-2015 sources. No guard applied. Carry-over points used in this analysis:
- CO1: the [S9] date correction [I1];
- CO2: ethics-review lead time [I16][I9];
- CO3: the qualitative-only limit on the five-user rule [I13];
- CO4: the time cost of testing [I12];
- CO5: systematic under-delivery evidence [I6][I3];
- CO6: the conflict over how ambitious to be [I7][I8][I9];
- CO7: the six-category accessibility pass [I15];
- CO8: underestimation of time [I17][I11];
- CO9: the guard against the "64%" statistic [I14].

## Evidence assessment

**Strong** (several independent, authoritative sources)
- What assessors value [S1][S2][S3]. These are three separate accreditors, and university rubrics and module specifications back them [S4][S5][S6][S7][S8]. Each university document covers one institution, but they agree.
- Evaluation and critical reflection are assessed [S2][S4][S5][S6][I7].
- Ethics and professional issues are expected [S1][S2][S3][I9].
- Planning and process are assessed, not optional: a separate 10% project-management report at Warwick [S6], plus [S2][S7].
- WCAG 2.2 is the current W3C Recommendation, and accessibility failures are common on real sites [S10][S11]=[I15].

**Medium**
- Students' non-technical weaknesses. [I6] is systematic but covers one institution. [I3] is from 2010, and [S17][S20][S22] are weak individually, but they agree with [I6] and [I3] on time management.
- Students do not test systematically [S18] (introductory students, abstract only), and the share writing tests is low before an intervention [S19] (small sample).
- The usability-testing sample-size guidance [S12][I13]. The organisation is reputable, and the 2021 article [I13] supersedes the 2000 framing for quantitative claims.
- MoSCoW limits [S9]=[I1]. The guidance comes from the body that owns the method, but it is industry guidance never tested on students.
- Early written scope and checkpoints [S6][S7][S8][S20][I10].

**Weak or contested**
- **Students underestimate time.** Only [I17] (a 1994 study reported second-hand) and [I11] (25 IT leaders, about newcomers to industry) measure underestimation directly. [I3] and [I6] show time-management problems, not underestimation (verdict C-J9).
- **Effort figures.** [I12] is from 2009 and covers professional TDD teams. [I16] is one non-computing department. Neither should be presented as a typical figure for students.
- **Deployment as an addition.** Only indirect support exists [S2][S8], and Jane records an evidence gap.
- **Security.** [S13] is authoritative but is the 2021 edition (a 2025 Release Candidate exists and was not opened). [I18] is a vendor report.
- **Sustainability method.** SCI rests on one source [S14] (the ISO text itself was not opened). That sustainability matters is backed by [S1] and [S3].
- **Scope change.** [S15]=[I5] was read at abstract level only. John's note "(p = .05)" alongside "no statistical difference" is unclear, so the writer should report "no statistical difference" without the p-value.
- **Ambition.** The sources conflict [I7][I8][I9], and [I8] is a personal blog.

**Do not use:** the "64% of features rarely or never used" statistic [I14]; the ACM Code of Ethics draft text (John's "Not verified" list); the OWASP 2025 category names (not opened).

## Patterns and comparisons

**Pattern 1: assessors and students diverge on the same qualities.** What assessors reward (evaluation, documentation, planning, communication [S1][S2][S4][S6]) closely matches where students struggle (timeliness, documentation, requirements [I6]; time management [I3][S17][S20]; evidence for conclusions [S17]; systematic testing [S18]). Employers report similar gaps in newcomers [I11] (interpretation). The highest-value "additions" are therefore often *better execution of assessed non-technical qualities*, not new features.

**Pattern 2: credit needs evidence.** Rubrics ask for analysis of results [S4][S5]. Automated accessibility checks do not prove conformance [S11]. Students believe they test systematically when they do not [S18]. Process artefacts can be "made up" to tick a box [S17]. Each addition should therefore come with its own evidence, such as test results, an audit record or user findings. Second-order costs follow from this: each addition needs its own testing, documentation and evaluation (interpretation from [I6], with [I4] for the "gold plating" term only).

**Pattern 3: effort depends on how far each idea is taken.** Accessibility (basic pass vs full conformance [I15][S11]) and user testing (qualitative five-user rounds vs quantitative 30+ [I13]) each have a cheap version and an expensive version. For several other ideas a split version is suggested here as judgement.

**Pattern 4: time is the binding constraint.** Time-management problems are the most consistent finding across both reports [S17][S20][S22][I3][I6]. Late failures are hard to recover [S22], and estimates tend to run short [I17][I11] (low-medium). This supports MoSCoW's contingency and early checkpoints [S9][S6][S7][S8].

### Table A: candidate ideas for the writer's table (Idea | Why it helps | Effort | Sources)
"Effort basis" says whether a rating has a source anchor or is **judgement**. The writer must label every judgement rating as such in the report (for example, a footnote: "Effort ratings are the authors' judgement except where a source is cited").

| # | Idea (concrete version) | Why it helps (evidence) | Strength of value evidence | Suggested effort | Effort basis | Key caveat |
|---|---|---|---|---|---|---|
| 1 | Stronger evaluation against objectives plus critical reflection on process | Required by BCS ("evaluation (with hindsight)", "critical self-evaluation"); 15% at TCD; "significant ... analysis or assessment of results" at Oxford; reflective writing at Warwick; one supervisor calls it "very important" [S2][S4][S5][S6][I7] | Strong | Medium | Judgement | Arguably core rather than an add-on; present it as "do this well first" |
| 2 | Small rounds of qualitative user testing (about five users per round, think-aloud) | Experimentation and data (ABET outcome 6) and validation (BCS) [S1][S2]; five users find most problems *in qualitative tests* [S12][I13] | Medium | Low–medium (test itself); medium overall if ethics review is needed | Partly sourced: participant numbers [I13]; review lead time [I16] | Do not claim statistical usability metrics from five users; quantitative claims need >30 [I13]. Plan ethics approval early [I16][I9][S21] |
| 3 | Accessibility pass to a WCAG 2.2 AA target: fix contrast, alt text, form labels, empty links and buttons, document language; report automated plus manual checks | WCAG 2.2 is the W3C standard [S10]; failures are very common [S11]; six error types make up 96% of detected errors [I15] | Medium–strong | Low (basic pass); high (claiming full conformance) | Partly sourced: scope from [I15][S11]; the low/high split is interpretation | "Absence of detected errors does not indicate that a page is accessible or conformant" [S11] |
| 4 | Automated unit tests running in continuous integration (CI) on each push | BCS asks for verification and validation and use of tools [S2]; students under-test [S18][S19]; most students in one CI study found it helpful [S19] | Medium | Medium | Partly sourced: TDD took 15–35% longer in industrial teams [I12] | [I12] is from 2009 and covers professionals; focus tests on complex code rather than chasing coverage [I12] |
| 5 | Security review against the OWASP Top 10 (record each category and its mitigation); keep secrets out of public repositories | OWASP is "a standard awareness document" [S13]; leaked secrets in public repositories are common [I18] | Medium (single standard) | Medium (review); low (secrets hygiene) | Judgement | 2021 edition; a 2025 Release Candidate was not checked [S13]. [I18] is a vendor report |
| 6 | Ethics, privacy and professional-issues section | Expected by ABET outcome 4, BCS §2.6.1 and Engineers Australia 3.1 [S1][S2][S3]; Sussex expects it by the Interim Report [I9] | Strong | Low (written section); medium if a user study needs approval | Judgement; lead time sourced [I16] | Ethics approval is a common project-module challenge [S21] |
| 7 | Risk register (identify, rate, mitigate, review) | Engineers Australia 2.1 expects risks to be identified and managed [S3]; late failures are hard to recover [S22] | Medium (single standard) | Low | Judgement | — |
| 8 | Project-management record and documentation (plan, log, README or user guide) | Warwick assesses a 10% project-management report [S6]; Engineers Australia expects "high quality engineering documents" [S3]; documentation is a top challenge [I6] | Strong (value); medium (under-delivery) | Low–medium | Judgement | Do the real thing; made-up process artefacts are a known failure [S17] |
| 9 | Sustainability analysis: qualitative discussion, or Software Carbon Intensity (SCI) = (E × I + M) per R | ABET outcome 2 ("environmental ... factors") and Engineers Australia 1.6c and 2.4f [S1][S3]; SCI is ISO/IEC 21031:2024 [S14] | Medium (value); method single-source | Low (discussion); medium–high (measured SCI) | Judgement | No cost evidence in either report; the ISO text was not opened |
| 10 | Design against a named standard (cite WCAG, OWASP or SCI explicitly) | ABET requires "appropriate engineering standards" [S1] | Medium (single source) | Low on top of ideas 3, 5 and 9 | Judgement | Cross-cutting; it may be better folded into ideas 3, 5 and 9 than given its own row |
| 11 | Deployment to real users or a live environment | "Real need in a wider context" and the CITP outcome "deploy, verify and maintain" [S2][S8] | Weak (indirect) | Medium–high | Judgement | [EVIDENCE GAP: deployment cost/benefit for students] |
| 12 | Budget or cost estimate (engineering projects) | Graduates felt least prepared for budgeting (mean 5.0/7) [S16] | Weak (single, preliminary, small sample) | Low–medium | Judgement | — |

Ideas 1–9 meet the brief's minimum of eight with at least medium-strength value evidence. Ideas 10–12 are optional.

### Table B: the ambition conflict, reconciled
| Source | Advice | How it fits |
|---|---|---|
| [I7] supervisor | Propose a "relatively modest project" and list extensions | Applies to *stated commitments*, i.e. the Must Haves |
| [I8] supervisor blog | Most students are "insufficiently ambitious"; go "deeper rather than wider", avoid bolt-on apps | Applies to depth in the *core problem* |
| [I9] Sussex | "As ambitious as possible" while planning for setbacks | Ambition with contingency |
| [S4][S5] rubrics | Top bands reward originality | Supports an ambitious core |
| [S7] UCL | Rewards "realistic work commitments" | Supports modest stated commitments |

Reconciliation (interpretation, low-medium confidence): be ambitious and deep in the core problem, commit only to a modest set of Must Haves, and treat extras as Could Haves that can be dropped.

## Recommendations
The brief asks for ideas, a prioritisation method and risk management, so these are in scope.

**Prioritisation method (for the report's step-by-step section).** It is built from [S9]=[I1], [I7], [S6][S7][S20], [S8][I10], [S2][S4][S5], [I13][I15] and [S22][I17]. Steps 3 and 4 are the analyst's synthesis and should be labelled that way.
1. **Secure the core first.** Write down the project's aims and treat them as the Must Haves, which should take ≤60% of the estimated effort. Keep stated aims modest [S9][I7].
2. **List candidate additions** (Table A) and mark which assessed quality each one improves (evaluation, testing, ethics, documentation, standards) [S2][S4][S5]. Linking additions to rubric criteria is an inference, not a tested method.
3. **Rate each addition** for value (rubric link and strength of evidence) and effort (Table A, with judgement labelled). Prefer the cheap version first: a basic accessibility pass before full conformance, qualitative before quantitative user testing [I15][I13].
4. **Sort the additions.** High value and low effort become Should Haves. Others become Could Haves (about 20% of effort, the first to drop). Record the rest as Won't Have this time [S9].
5. **Hold a time buffer and start time-sensitive items early.** Plan for estimates being optimistic [I17][I11], and start ethics approval early [I16][S21].
6. **Agree the scope in writing with the supervisor** and check progress at fixed milestones (project plan, interim report, mid-project demonstration). Drop Could Haves first if behind [S6][S7][S8][S20][I10].
7. **Evidence every addition you keep**, through test results, audit records or user findings. Anything unevidenced should be cut or reported honestly as incomplete [S4][S5][S11][S17][I7].

**Risks and mitigations (for the risks section)**

| Risk | Mitigation |
|---|---|
| Time overrun [S22][S17][S20][I3][I6] | Contingency and early milestones [S9][S6][S7][S8] |
| Late failure is hard to recover [S22] | Interim reports and demonstrations [S7][S8]; share unfinished work early [I7] |
| Tick-box or unevidenced extras [S17][S18][S11] | Evaluate each addition, or drop it |
| Extras crowd out the core, which carries the largest mark weight (50% at TCD) [S4][S2] | Inference from one rubric; MoSCoW ordering, depth over breadth [I8] |
| Ethics lead time [I16][S21] | Apply early |
| Scope change | Not harmful in itself if managed [S15]=[I5] (low-medium confidence) |

## Assumptions and limitations
- **No outcome data.** No source in either report shows that any addition raises a grade. "Why it helps" rests on what standards and rubrics value.
- **Effort ratings.** Mostly judgement. Only four ideas have cost anchors, and each anchor is single-source with caveats: [I12] is from 2009 and covers professional teams; [I16] is one non-computing department.
- **Geographic spread.** Rubrics come from the UK, Ireland and US accreditation. There is no Asian university rubric; Australia is covered only through Engineers Australia [S3].
- **Shared sources.** Three key agreements rest on the same sources ([S9]=[I1], [S11]=[I15], [S15]=[I5]), so they are not independently confirmed.
- **Abstract-only reads.** [S15]/[I5], [S18], [S21] (embargoed until 12 November 2026) and [I10].
- **Dated sources.** Sources outside the brief's window are [S12] (2000), [I3] (2010), [I12] (2009) and [I17] (a 1994 study). Prefer newer sources where they overlap ([I13] over [S12]; [I6] over [I3]).
- **Unresolved disagreements.**
  1. [S9]'s date: resolved provisionally in favour of [I1] (2026). The analyst could not re-open the page.
  2. How strongly time underestimation is supported: rated low-medium here, not Jane's moderate-to-high.
  3. Whether "marks come from the dissertation" [I7]: not generalised.
  4. How ambitious to be: reconciled only by interpretation (Table B).
- **MoSCoW limits.** The 60%/20% figures are industry guidance, untested on students [S9]=[I1].

## Open questions
These come from the research gaps. None is blocking: the writer can proceed with them disclosed.
- **[S9]'s publication date.** A quick re-check would confirm the provisional ruling. Optional.
- **OWASP Top 10:2025.** Is it final, and what are its category names? This would let the report cite the current edition. Optional.
- **Effort or cost evidence** for sustainability (SCI), deployment, security review and documentation in student projects. None was found. [EVIDENCE GAP]
- **Systematic, multi-institution data on what final-year students under-deliver.** [S21] may help once its full text is released (after 12 November 2026).
- **Typical ethics-review lead times in computing and engineering departments.** Only one non-computing example exists [I16].
- **Not opened:** NN/g "How Many Test Users in a Usability Study?", ACM/IEEE CS2023 capstone guidance, the final ACM Code of Ethics text, and the Sussex undergraduate marking criteria. All are listed as not verified.
