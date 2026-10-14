# Independent research report (Jane, step 1b)

**Assigned angle:** I used counter-framed searches about scope creep, failure, gold plating and overcommitment. I combined education research on student and team experience with practitioner and employer sources. I analysed everything for cost, trade-off and risk.

## 1. Research question and scope

These are the research questions from `00-brief/project-brief.md`:
1. What do capstone and final-year project guides and assessors value, and which of those qualities do students often under-deliver?
2. What additional ideas or features are commonly recommended to strengthen a major project (user testing, accessibility, automated testing, security, documentation, data and evaluation, ethics, sustainability, deployment)? Give concrete examples.
3. How should a student choose, prioritise and scope additions (must-have vs stretch, time, risk)?
4. What are the risks or downsides of adding extra ideas, and how can they be managed?

The scope is generic advice for any major project, with computing and engineering examples. Sources are English-language and roughly 2015 onward. Content farms, essay mills, unauthored listicles and AI summaries are excluded.

The research supports a 1,500–2,500 word student report. That report needs a table of at least eight ideas (Idea | Why it helps | Effort | Sources) and a prioritisation method.

## 2. Research approach and source-selection rationale

**Angle and how it differs from the default.** The primary researcher's default is official and primary sources first, answering each question directly. My angle differs in three ways:
- **Search strategy:** I used counter-framed queries that start from failure and overload, not from rubrics. Examples:
  - "capstone project scope creep"
  - "why software engineering capstone projects fail"
  - "gold plating software project risk"
  - "student software projects feature creep overambitious"
  - "final year project common mistakes too ambitious"
  - "planning fallacy thesis students"
  - "Standish features rarely or never used"
- **Source mix:**
  - education research on student and team experience [I3][I5][I6][I10]
  - practitioner sources on prioritisation and risk [I1][I4][I14]
  - individual supervisors' advice [I7][I8]
  - an employer or IT-leader perspective [I11]
  - cost and effort evidence for specific additions [I12][I13][I15][I16][I18]
- **Analytical perspective:** for each addition, I asked what it costs, what it buys and what can go wrong.

**Tools.** WebSearch (standard mode) and WebFetch were available and used. curl and Bash network access were blocked. All 18 cited sources were opened. Several conference papers could only be read at abstract or landing-page level, which is flagged in the sources list and below.

**Not covered by design.** I deliberately did not cover accreditation criteria (ABET, Engineers Australia) or formal marking rubrics, because those belong to the primary angle.

## 3. Key findings

### RQ1: What assessors value and what students under-deliver

- **Evaluation and write-up carry the marks (one supervisor's view).** A Cambridge supervisor tells students "Your marks come from your dissertation, not your project" and "The evaluation is very important". He asks for an explanation of tests, experimental design, benchmarks, error margins and statistics. [I7] (reported claim; single source)
- **Marks track stated aims (same supervisor).** He advises proposing "a relatively modest project" and then doing more than claimed, because Part II marks depend on meeting stated aims. [I7] (reported claim; single source)
- **Sussex expects early ethics thinking.** Students should have "considered ethical issues relating to their project" by the Interim Report. [I9] (verified fact for Sussex; single source)
- **Sussex marks presentation separately.** The presentation mark "should primarily reflect the quality of the presentation rather than the quality of the project". This suggests communication is assessed as a skill in its own right. [I9] (verified fact for Sussex; interpretation for the generalisation; single source)
- **Non-technical issues dominate in SE capstones.** A study of 79 post-mortem reports from SE capstone teams at one German university concludes that "technical issues tend to be less challenging than non-technical ones". [I6] (verified fact about that study; single source)
  - Within organisational matters, "time aspects and timeliness" was the most coded issue (34 codes, 26.15%).
  - Within professional and technical issues, documentation (27 codes, 21.77%) and software requirements (25 codes, 20.16%) were the most frequent.
- **Time management in mechanical engineering teams.** A Villanova survey of 88 mechanical engineering seniors found these leading factors [I3] (verified fact about that study; single source; dated 2010):
  - scheduling conflicts (52.6%) and lack of time management (46.6%) were the top barriers to team functioning;
  - teamwork (70.5%) was the leading enabler.
- **Students under-deliver on process more than technical ambition.** Taken together, the evidence suggests students under-deliver on time management, requirements, documentation and teamwork rather than on technical ambition. [I3][I6] (interpretation; confirmed: 2+ independent sources on time management specifically)
- **IT leaders see similar gaps in newcomers.** IT leaders interviewed in Brazil said newcomers "tend to underestimate the difficulty of the tasks". They listed "sense of time", "patience" (rushing delivery at the expense of quality) and communication among graduates' gaps. [I11] (reported claim; single source) These employer gaps match the student-side weaknesses above. [I6][I11] (interpretation)

### RQ2: Common additions and what each one costs

- **Automated testing (TDD) costs time in professional teams.** Industrial teams at Microsoft and IBM using TDD produced code "60 to 90 percent better in terms of defect density". They also took "15 to 35 percent longer". [I12] (reported claim from the research organisation; single source; 2009; professional teams, not students)
  - The same summary reports that "higher code coverage was not the best measure of post-release failures". It suggests testing complex code matters more than chasing coverage. [I12] (reported claim; single source)
  - Automated testing therefore has a real, measurable time cost, and its benefit depends on testing the complex parts. [I12] (interpretation)
- **User testing: five users is enough only for qualitative studies.** NN/g says five users suffice for a qualitative usability test. This relies on the Nielsen–Landauer model, which assumes a 31% chance that a user hits a given issue; under that assumption, five users find about 85% of issues. [I13] (verified fact about the guideline; single source)
  - Quantitative claims need "usually more than 30" participants, and "40 or more" for narrow intervals.
  - The 31% figure comes from early-1990s projects. At a 10% chance, 18 users are needed.
  - Interpretation: a five-person think-aloud test is a low-cost addition, while claiming statistically meaningful usability metrics is high-cost, and students may confuse the two. [I13] (interpretation)
- **User testing triggers ethics review, which takes time.** Testing with people usually triggers ethics review when a project collects data from human participants. At one Cambridge department, cases referred to the School committee "can take up to three weeks (longer if revisions are required)". [I16] (verified fact for that department; single source; non-computing department) That review times are similar elsewhere is a hypothesis, not verified.
- **Accessibility: a basic pass is cheap, full conformance is not.** The 2026 WebAIM Million found that 95.9% of the top one million home pages had detected WCAG 2 failures, averaging 56.1 errors per page. [I15] (verified fact; single source)
  - "96% of all errors detected fall into these six categories": low-contrast text (83.9% of pages), missing alt text (53.1%), missing form labels (51%), empty links (46.3%), empty buttons (30.6%) and missing document language (13.5%).
  - WebAIM states that automated tools cannot detect all failures.
  - Interpretation: a basic pass on these six issues is low effort and covers the most frequent automatically detectable problems, while claiming full conformance needs manual testing and is higher effort. [I15] (interpretation)
- **Security: keep secrets out of public repositories.** GitGuardian reports 28,649,024 new secrets detected in public GitHub commits in 2025. It also reports 81% year-on-year growth in leaked AI-service secrets. [I18] (reported claim from a vendor; single source)
  - A public portfolio repository is itself a risk if API keys are committed, so keeping secrets out of the repository is a cheap, high-value addition. [I18] (interpretation)
- **Extra features versus depth.** One supervisor warns against bolting on features such as an app, because a website rarely demonstrates much computer science. He advises going "deeper rather than wider", for example by implementing a known algorithm or replicating a paper. [I8] (reported claim; single source; opinion)
  - For assessment, depth and evaluation may be worth more than breadth of features. [I7][I8] (interpretation)

### RQ3: Choosing, prioritising and scoping additions

- **MoSCoW sets priority levels and effort limits.** The Agile Business Consortium (DSDM) defines the levels as follows. [I1] (verified fact; single source, the standard's owner)
  - **Must Have:** "the minimum usable subset". The test is "what happens if this requirement is not met?"
  - **Should Have:** "important but not vital".
  - **Could Have:** the first to drop, and the main contingency pool.
  - **Won't Have this time:** recorded so the items are not quietly reintroduced.
  - Must Haves should be "typically no more than 60%" of effort, and Could Haves about 20%. Going above 60% is risky unless estimates are accurate, the approach is well understood and external risk is low.
- **DSDM fixes time and flexes scope.** It does this through timeboxes, with priorities set per timebox. [I1] (verified fact; single source)
- **A supervisor's version of the same idea.** Chisnall advises halving the planned work and listing the rest as possible extensions in the proposal. [I7] (reported claim; single source) This maps onto MoSCoW: the proposal's aims are the Must Haves and the listed extensions are the Coulds. [I1][I7] (interpretation)
- **Timeboxed milestones help self-organised student projects.** A time-boxed MSc design module with five milestones received "very positive" feedback. [I10] (reported claim; single source; abstract only; no quantitative outcome)
  - The author attributes this to milestone structure, strict enforcement and rotating project management.
  - The author also notes that self-organised projects "tend to start out with low speed and push the workload forward".
- **Students underestimate how long work takes.** A Donders Institute blog reports a 1994 study by Buehler, Griffin and Ross. Honours students estimated their thesis would take 33.9 days, but it took 55.5 days, longer than their own pessimistic estimate of 48.6 days. [I17] (reported claim; single source; secondary report of a 1994 study)
  - The blog's debiasing advice: base estimates on a similar past task, and ask someone else for an estimate. [I17] (reported claim; single source)
  - Together with the IT leaders' observation [I11], this supports building a time buffer before adding any extras. [I11][I17] (interpretation; confirmed: 2+ independent sources on underestimation)

### RQ4: Risks of adding extras, and how to manage them

- **Scope creep.** Scope creep is "adding of additional features or functions … that is not authorized". It risks "causing delays, additional costs, and hurt customer or team relationships", and is more likely when scope is poorly defined. [I2] (reported claim; single source; undated open educational resource)
- **Gold plating.** Gold plating is "working on a project or task past the point of diminishing returns". It "introduces a new source of risks to the original planning" and can add testing, documentation and timeline pressure. [I4] (reported claim; low-reliability tertiary source; definition only)
  - Every addition carries second-order costs (tests, documentation and evaluation of the addition itself) that students may not budget for. [I4][I6] (interpretation)
- **Scope change is common but did not lower outcomes in one study.** In one Northeastern capstone offering, about 46% of projects changed topic or scope substantially after significant work. There was "no statistical difference" in prototype or success scores. [I5] (verified fact about that study; single source)
  - High-scoring changed teams were proud of their flexibility and their project and time management.
  - Low-scoring teams were surprised by how difficult, vague and time-consuming the work was.
  - How a team manages change matters more than whether change happens. [I5] (interpretation)
- **The "64% of features unused" statistic is unreliable.** The often-repeated claim comes from "a study of four internal applications", according to Standish via Mountain Goat Software. It should not be generalised. [I14] (reported claim; single source)
- **Share unfinished work early.** One supervisor advises not hiding unfinished work, because incomplete work shared early costs no marks. [I7] (reported claim; single source)
  - An extra that is unfinished, untested or unevaluated may add risk without adding marks. [I7][I12] (interpretation) That it actually lowers marks is a hypothesis, not tested in any source opened.

## 4. New evidence or perspectives

This angle surfaced several points that John's report does not contain.

- **Cost evidence for specific additions.** These figures can anchor the Effort column, which John's report calls an evidence gap:
  - testing took industrial teams 15–35% longer [I12];
  - five users suffice for qualitative usability tests, but 30–40+ are needed for quantitative ones [I13];
  - six accessibility error types cover 96% of automatically detected errors [I15];
  - ethics review can take up to three weeks or more [I16].
- **Converging evidence that students and newcomers underestimate time.** This comes from post-mortems, surveys, employer interviews and planning research [I3][I6][I11][I17]. John's time-management evidence is labelled "confirmed, weakly".
- **A systematic analysis of capstone challenges.** It ranks timeliness, documentation and requirements highly, and finds non-technical issues harder than technical ones [I6].
- **The conflict over ambition** [I7][I8][I9]. One source argues for depth over breadth, which John's report does not discuss.
- **A newer NN/g treatment of the five-user rule.** It limits the rule to qualitative studies [I13]. John relied on the 2000 article [S12] and listed a newer NN/g article as not opened.
- **A caution on the widely repeated "64% of features unused" statistic** [I14].
- **Secrets hygiene as a cheap security idea for public portfolio repositories** [I18].
- **Gold plating and second-order costs** as a named risk [I4].

## 5. Conflicting evidence and counterarguments

- **How ambitious to be: the sources genuinely disagree.** This disagreement is in the sources, not manufactured.
  - Chisnall advises a modest proposal with extensions held in reserve [I7].
  - Reddington says about 80% of students are "insufficiently ambitious" and that "there are more marks in making a heroic effort for a difficult project" [I8].
  - Sussex tells supervisors to "Encourage students to be as ambitious as possible" while planning for setbacks [I9].
  - A possible reconciliation (interpretation): Reddington favours going deeper rather than wider and warns against bolt-on features [I8], while Chisnall's caution concerns stated commitments, not effort [I7]. Ambition in the core problem and caution about extra features may both hold. [I7][I8][I9]
- **Scope change is not always harmful.** Changed or delayed capstones did no worse on outcomes [I5]. This counters the "scope creep is bad" framing. However, it concerns client-driven change, which differs from student-driven gold plating.
- **Automated testing is not a free win.** It is commonly recommended, but [I12] reports a 15–35% time cost in professional settings, so it is a trade-off.
- **The five-user rule has limits.** It is often repeated as universal, but NN/g itself limits it to qualitative studies. NN/g also notes its assumptions date from the early 1990s [I13].

## 6. Source-quality concerns and potential bias

- **Single-institution studies.** [I3], [I5], [I6], [I9], [I10] and [I16] each describe one institution, so generalisation is uncertain.
- **Outside the brief's date window.** [I3] (2010), [I12] (2009) and the 1994 study behind [I17] predate the brief's rough 2015+ window. They are kept as the best cost and estimation evidence found from this angle, and are flagged.
- **Abstract-only reads.** [I5] and [I10] were not read in full, and sample sizes for [I5] are not stated on the page read.
- **Professional, not student, teams.** [I12]'s TDD figures come from industrial teams, so the effect sizes may not transfer to students.
- **Vendor source.** [I18] is from a company that sells secret-detection tools. Its figures cover a large scale but are not independently reviewed.
- **Opinion sources.** [I7] and [I8] are individual supervisors' views. [I8]'s "80%" is his own estimate, not data, and his institution is not stated.
- **Wikipedia for definition only.** [I4] is used only for a definition. McConnell's *Rapid Development* was not opened.
- **Thin employer evidence.** [I11] is a convenience sample of 25 IT leaders in Brazil with no per-skill counts. Better employer or portfolio evidence was not found; search results were mostly bootcamp and vendor marketing pages, which were avoided.

## 7. Points of agreement with the primary findings

Our separate angles agree on the following:

- **MoSCoW guidance.** Must Haves should be no more than about 60% of effort, with about 20% in Could Haves as contingency. Both reports used the same Agile Business Consortium page [S9]=[I1]. Both note it is industry guidance not tested on students.
- **Accessibility prevalence and its limits.** Both reports cite the same WebAIM figures (95.9%, 56.1 errors per page, contrast, alt text and form labels) and the caveat that automated checks do not prove conformance [S11]=[I15].
- **Scope change and outcomes.** Both reports read Jaeger-Helton and Smyser the same way: about 46% of projects changed, with no statistical difference in outcomes, so managing change matters more than whether change happens [S15]=[I5].
- **Time management is a weakness.** Both reports find students struggle with it [S17][S20][S22] and [I3][I6][I17]. Both treat it as a central risk of adding extras.
- **Unevidenced extras do not earn credit.** John: "An extra such as 'accessibility' or 'security' claimed without evidence will not meet evaluation criteria". This matches my reading that unfinished or unevaluated extras add risk without marks [I7][I12].
- **Ethics review is a burden of adding user studies.** Both reports note this ([S21]; [I16]). My source adds a concrete timeline.
- **Evaluation and the write-up matter.** John's rubric and accreditation evidence [S2][S4][S5][S6] confirms, from a much stronger source base, the supervisor view I found [I7].
- **No source quantifies grade benefit.** Neither report found a source showing how much any specific addition improves grades.

## 8. Unresolved questions, limitations and confidence assessment

**Overlap with the primary method.** The two methods overlapped only partly. Three sources were shared ([S9]=[I1], [S11]=[I15], [S15]=[I5]). Agreement on those three points is therefore not fully independent. The remaining 15 of my 18 sources do not appear in John's list.

**Not verified** (seen in search results but not opened or not usable):
- Steve McConnell, *Rapid Development* (1996) and "Classic Mistakes Enumerated".
- Ovesen, Eriksen & Tollestrup (2011), "Speeding up Development Activities in Student Projects with Time Boxing and Scrum", E&PDE 2011. The landing page was opened, but the paper is pre-2015 and the full text is members-only, so it is not used as evidence.
- Sahl & Samarah (2025), "Building MVPs: An Experience Report of a Software Engineering Capstone Course", ICSE Designing 2025 workshop. The landing page was opened but contained no MVP findings, so it is not used.
- Adkins & Tu (2019), "Applying an Agile Approach in an Information Systems Capstone Course", ISEDJ 17(3). The landing page was opened but the findings were not on it, so it is not used.
- Radermacher & Walia, on industry expectations versus graduate abilities (NDSU and ICSE 2014 links). Not opened.
- Buehler, Griffin & Ross (1994), the original planning-fallacy paper. Not opened; known only through [I17].

**Gaps:**
- No direct evidence was found on how much any specific addition raises a capstone mark.
- [EVIDENCE GAP: sustainability addition — none found from this angle]. John's report covers this through [S1][S3][S14].
- [EVIDENCE GAP: deployment cost/benefit for students], beyond secrets hygiene.
- Employer and portfolio evidence is thin [I11].
- This angle did not cover accreditation or rubric sources. On RQ1, John's report is the stronger evidence base.

**Confidence:**
- Moderate-to-high, from several independent sources: students and newcomers underestimate time [I3][I6][I11][I17]; MoSCoW-style must/could separation with contingency is established practice [I1][I7].
- Moderate, from single strong sources: accessibility quick wins [I15]; user-testing sample sizes [I13].
- Low-to-moderate: TDD cost figures applied to students [I12]; ambition guidance, where the sources conflict [I7][I8][I9].

## 9. Recommended issues for the Analyse Agent to investigate

1. **Effort column.** Combine John's standards-linked ideas list [S10][S13][S14][S2][S3] with my cost evidence [I12][I13][I15][I16]. This lets some Effort ratings be sourced rather than all flagged as gaps. Where no cost evidence exists (sustainability, deployment, risk register), keep the rating labelled as judgement.
2. **Prioritisation method.** The shared MoSCoW guidance ([S9]=[I1]: Musts no more than 60%, about 20% Coulds) is a strong candidate basis. It maps onto proposal aims plus listed extensions [I7] and early written scope agreements [S6][S7][S20]. Add a time buffer justified by underestimation evidence [I3][I6][I11][I17].
3. **Ambition conflict.** Resolve [I7][I8][I9] against John's rubric evidence. [S5] rewards originality and [S4] rewards "an element of originality". Check whether "ambitious core, cautious extras" fits both.
4. **User testing guidance.** Prefer [I13] (2021) over [S12] (2000), or use both with the qualitative/quantitative caveat.
5. **Testing as a trade-off.** Present automated testing with both its learning benefits [S18][S19] and its time cost [I12]. Note that [I12] comes from professional teams.
6. **Ethics lead time.** Use [I16] as one example of review taking up to three weeks or more, alongside [S21].
7. **Date and sample caveats.** Apply caveats to [I3], [I12] and [I17], and prefer 2015+ sources where they cover the same point.
8. **The 64% statistic.** If any draft uses the "64% of features unused" figure, remove it or add a caveat [I14].
9. **[S9] date.** The page is dated 28 May 2026 and was last modified 9 September 2026 [I1]. Correct the reference date in the final report.
