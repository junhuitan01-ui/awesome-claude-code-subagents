# Making your major project stronger: additional ideas and how to choose them

*Draft for review, 14 October 2026*

## 1 Executive summary

The best "extras" for a major project are usually not new features. They are the non-technical qualities that assessors already mark and that students often do poorly: evaluation, testing, documentation, ethics and planning. Three accreditation bodies in three countries, and several universities' marking rubrics, name these qualities [S1][S2][S3][S4][S5][S6][S7][S8]. Studies of student projects find that students struggle most with exactly this kind of work, such as time management, documentation and requirements [I6][I3][S17][S20].

This report suggests 11 additional ideas, most linked to a standard or rubric that values them. The main points are:

- **Pick additions that improve something assessors mark,** and back each one with evidence such as test results or user findings. Extras without evidence earn little credit [S4][S5][S11][S17].
- **Start with the cheap version of each idea.** A basic accessibility check or a five-person user test costs far less than full conformance or a statistical study [I15][I13].
- **Protect the core project first.** Use a simple priority method (MoSCoW, explained in section 4), keep a time buffer, and agree your scope with your supervisor early [S9][S6][S7][S20].

No source measured how much any addition raises a grade. The advice rests on what standards and rubrics reward, not on outcome data.

## 2 What makes a major project strong

**Assessors reward more than a working product.** Five qualities appear again and again (confidence: high):

- **Evaluation and analysis of results.** BCS, the UK professional body for IT, asks for "evaluation (with hindsight) of the project outcome and the process of its production" and "critical self-evaluation" [S2]. Trinity College Dublin gives 15% of the mark to testing, evaluation and conclusions [S4]. Oxford's top band asks for "a significant amount of analysis or assessment of results" [S5].
- **Testing, or verification and validation.** BCS asks the report to explain "how verification and validation were applied" [S2]. ABET, the US engineering accreditor, expects students to "develop and conduct appropriate experimentation, analyze and interpret data" [S1].
- **Documentation and communication.** Engineers Australia expects "high quality engineering documents such as progress and project reports" [S3].
- **Ethics and professional issues.** ABET, BCS and Engineers Australia all expect them [S1][S2][S3].
- **Planning and project management.** Warwick gives 10% of the mark to a separate project-management report [S6]. UCL lists "realistic work commitments" as a learning outcome [S7].

**The core artefact still matters most.** At Trinity, technical content and execution carry 50% of the mark [S4]. Top bands also reward originality [S4][S5].

**Students often fall short on the non-technical work** (confidence: medium). A study of 79 post-mortem reports from software engineering capstone teams at one university found that "technical issues tend to be less challenging than non-technical ones". Timeliness (26.15% of coded issues), documentation (21.77%) and requirements (20.16%) ranked highest [I6]. A 2010 survey of 88 engineering seniors found scheduling conflicts and lack of time management were the top barriers [I3]. Other reports point the same way: students start late [S17], struggle with time management [S20], do not test systematically while believing they do [S18], and present conclusions with "barely any evidence" [S17]. Most of these studies cover one institution, so treat them as signals, not proof.

## 3 Additional ideas

Table 1 lists 11 ideas. "Effort" is marked **(J)** where the rating is the authors' judgement; only four ideas have any source for their cost. Several ideas name a standard to design and test against. ABET asks for "appropriate engineering standards" in the final design experience [S1], so citing WCAG, OWASP or SCI explicitly is a small extra that strengthens ideas 3, 5 and 9.

**Table 1. Additional ideas for a major project**

| Idea | Why it helps | Effort (low / medium / high) | Sources |
|---|---|---|---|
| 1. Stronger evaluation against your objectives, plus critical reflection on your process | Required by BCS; 15% of the mark at Trinity; reflective writing assessed at Warwick. Arguably core work: do this well first | Medium (J) | [S2][S4][S5][S6][I7] |
| 2. Small rounds of user testing (about five users per round, thinking aloud) | Gives evidence for evaluation and validation. Five users find most problems in a *qualitative* test | Low–medium; medium if ethics approval is needed | [S1][S2][S12][I13][I16] |
| 3. Accessibility pass aiming at WCAG 2.2 level AA: fix contrast, image descriptions (alt text), form labels, empty links and buttons, page language; report automated and manual checks | WCAG is the international web standard; failures are very common on real sites | Low (basic pass); high (claiming full conformance) | [S10][S11][I15] |
| 4. Automated unit tests that run in continuous integration (CI) on every code push | BCS asks for verification and use of tools; students tend to under-test | Medium | [S2][S18][S19][I12] |
| 5. Security review against the OWASP Top 10, recording each risk and how you handle it | A widely used industry list of web security risks | Medium (J) | [S13] |
| 6. Ethics, privacy and professional-issues section | Expected by three accreditation bodies | Low (written section); medium if a user study needs approval (J) | [S1][S2][S3][I9][I16] |
| 7. Risk register: list risks, rate them, plan responses, review regularly | Engineers Australia expects risks to be identified and managed; late failures are hard to recover | Low (J) | [S3][S22] |
| 8. Project-management record and documentation (plan, progress log, README or user guide) | Assessed directly at Warwick (10%); documentation is a top student weakness | Low–medium (J) | [S3][S6][I6] |
| 9. Sustainability analysis: a written discussion, or a Software Carbon Intensity (SCI) estimate | ABET and Engineers Australia name environmental factors; SCI is an ISO standard method | Low (discussion); medium–high (measured SCI) (J) | [S1][S3][S14] |
| 10. Deployment to real users or a live environment | Indirect support only: BCS values meeting "a real need in a wider context" | Medium–high (J) | [S2][S8] |
| 11. Budget or cost estimate (engineering projects) | Graduates felt least prepared for budgeting (mean 5.0 on a 7-point scale) | Low–medium (J) | [S16] |

*Source: this report's analysis of the cited sources. (J) = authors' judgement; no source gives a cost. Ratings without (J) draw partly on a cost source, but the low / medium / high labels are still our reading.*

Some terms in the table, and what the evidence says about cost:

- **User testing.** Five users are enough only for qualitative testing, where you watch people and note problems. Claims with numbers usually need more than 30 users [I13]. The older five-user rule comes from a 2000 article and early-1990s assumptions [S12][I13]. Testing with people may also need ethics approval. At one university department, referred cases "can take up to three weeks (longer if revisions are required)" [I16].
- **WCAG** (Web Content Accessibility Guidelines) 2.2 is the W3C web accessibility standard. It has three conformance levels: A, AA and AAA [S10]. In 2026, 95.9% of the top one million home pages had detected failures [S11]. Six error types made up 96% of detected errors, so fixing them is a cheap first pass [I15]. But "absence of detected errors does not indicate that a page is accessible or conformant" [S11].
- **CI** (continuous integration) means tests run automatically each time you save code to a shared repository. In one small study, most students found writing their own tests helpful [S19]. Testing has a cost, though. Professional teams using test-driven development took 15–35% longer, but had 60–90% lower defect density [I12]. That data is from 2009 and from professionals, so treat it as a rough pointer only. Focus tests on complex code rather than chasing coverage figures [I12].
- **OWASP** (Open Worldwide Application Security Project) publishes the Top 10, "a standard awareness document" for web security [S13]. We used the 2021 edition; a 2025 draft was not checked.
- **SCI** is calculated as (E × I + M) per R: energy used, times the carbon intensity of that energy, plus emissions from making the hardware, per unit such as one user or one request [S14].
- **Ethics timing.** Sussex expects students to have "considered ethical issues relating to their project" by the interim report [I9]. Educators list ethics approval as a common project-module challenge [S21].

## 4 How to choose and scope your additions

**MoSCoW** is a priority method from the Agile Business Consortium. It sorts work into **M**ust have, **S**hould have, **C**ould have and **W**on't have this time [S9][I1]. Must Haves should take no more than about 60% of your effort, and about 20% should sit in Could Haves as a buffer you can drop [S9]. This guidance comes from industry and has not been tested on student projects.

**How ambitious should you be?** Supervisors disagree (confidence: low-medium):

- One advises proposing "a relatively modest project" and listing extensions separately [I7].
- Another says most students are "insufficiently ambitious" and should go "deeper rather than wider" instead of bolting on features [I8].
- A third university tells supervisors to encourage students "to be as ambitious as possible" while planning for setbacks [I9].

Rubrics reward both originality [S4][S5] and "realistic work commitments" [S7]. A reasonable reading is this: be ambitious and deep in the core problem, promise only a modest set of Must Haves, and treat extras as Could Haves. This reconciliation is our interpretation.

**A step-by-step prioritisation method.** Steps 3 and 4 are the analyst's synthesis, not a tested method.

1. **Secure the core first.** Write down your project aims. These are your Must Haves; keep them to about 60% of your estimated effort and keep them modest [S9][I7].
2. **List possible additions** from Table 1. Note which marked quality each one improves: evaluation, testing, ethics, documentation or use of standards [S2][S4][S5].
3. **Rate each addition** for value (does it link to the marking criteria?) and effort. Choose the cheap version first: a basic accessibility pass before full conformance, qualitative testing before statistics [I15][I13].
4. **Sort them.** High value and low effort become Should Haves. The rest become Could Haves, the first to drop. Record what you are leaving out as Won't Have [S9].
5. **Keep a time buffer and start slow items early.** Estimates tend to run short. In one 1994 study, students expected their thesis to take 33.9 days; it took 55.5 [I17]. Apply for ethics approval early [I16][S21].
6. **Agree your scope in writing with your supervisor** and check progress at fixed points, such as a project plan, an interim report and a mid-project demonstration [S6][S7][S8][S20]. If you fall behind, drop Could Haves first.
7. **Back up every addition you keep** with evidence: test results, an audit record or user findings. Cut anything you cannot evidence, or report it honestly as incomplete [S4][S5][S11][S17][I7].

## 5 Risks and how to manage them

Adding extras has real risks (confidence: medium).

**Table 2. Risks of adding extras**

| Risk | How to manage it |
|---|---|
| **Running out of time.** Project work "can consume far more time than its assessment-worth" [S22]; time management is the most consistent student weakness [S17][S20][I3][I6] | Keep a Could-Have buffer and set early milestones [S9][S6][S7][S8] |
| **Late failure.** Failures "discovered near the end of a large project are far more difficult to retrieve" [S22] | Use interim reports and demonstrations [S7][S8]; share unfinished work early [I7] |
| **Extras done for show.** Students have admitted "making up content" for required process documents [S17]; automated checks alone do not prove accessibility [S11] | Evaluate each addition, or drop it |
| **Extras crowding out the core,** which carries the largest share of marks (50% at Trinity) [S4] | Use MoSCoW order; go deep, not wide [I8]. This is an inference from one rubric |
| **Ethics approval delays** [I16][S21] | Apply early |
| **Changing scope midway** | Not harmful in itself. In one capstone course, about 46% of projects changed substantially, with no statistical difference in outcomes [S15]. How you manage change matters more (confidence: low-medium) |

*Source: this report's analysis of the cited sources.*

## 6 How this report was made

This report came from a structured debate. Two researchers worked separately on the same brief:

- The **primary researcher** ("John") focused on accreditation standards, university marking rubrics and published standards.
- The **independent researcher** ("Jane") deliberately took a different angle: education studies, supervisors' advice, and evidence on cost and effort.

Each then wrote one rebuttal of the other's report. An analyst judged both on five criteria, weighting evidence highest.

**Result: the primary report won, 4.00 to 3.55.** It scored 4 out of 5 on every criterion. The independent report scored 4 on argument, content and formatting, and 3 on points covered and references. The winner answered all four research questions from the sources the brief preferred. The independent report left out assessors' own documents, had gaps on sustainability and deployment, and relied more on weak or older sources.

This report presents the winning research. It also carries over nine points from the independent report:

1. The correct date of the MoSCoW guidance (2026, not undated) [I1].
2. Ethics review can take up to three weeks or more, and Sussex expects ethics to be considered early [I16][I9].
3. Five test users are enough only for qualitative tests [I13].
4. Automated testing has a real time cost [I12].
5. Systematic evidence that students fall short mainly on non-technical work [I6][I3].
6. Supervisors disagree on how ambitious to be [I7][I8][I9].
7. Six error types cover most detected accessibility errors, so a basic pass is cheap [I15].
8. Students tend to underestimate time (low-medium confidence) [I17][I11].
9. A warning not to use a widely repeated claim that most software features go unused, because it comes from only four internal applications [I14].

## 7 Limitations

- **No outcome data.** No source shows how much any addition raises a grade.
- **Effort ratings are mostly judgement.** Only four ideas have a cost source, and each is a single source. The testing figures are from 2009 professional teams [I12]; the ethics timing is from one non-computing department [I16].
- **Limited geography.** Rubrics come from the UK and Ireland, plus US and Australian accreditation [S1][S3]. No Asian university rubric was found.
- **Shared sources.** Three agreements between the researchers rest on the same source: MoSCoW [S9][I1], accessibility [S11][I15] and scope change [S15][I5]. They are not independently confirmed.
- **Partial reading.** Only abstracts were read for [S15], [S18], [S21] and [I5]. [S21]'s full text is embargoed until 12 November 2026.
- **Older sources.** [S12] (2000), [I3] (2010), [I12] (2009) and the 1994 study behind [I17] fall outside the brief's 2015 window.
- **Other gaps.** The OWASP 2025 edition was not checked [S13]. [EVIDENCE GAP: cost and benefit of deployment as a student-project addition] [EVIDENCE GAP: effort data for sustainability, security review and documentation in student projects]

## 8 References

[S1] ABET. (2025). Criteria for Accrediting Engineering Programs, 2025–2026.
[S2] BCS, The Chartered Institute for IT. (2020). Guidelines on course accreditation.
[S3] Engineers Australia. (2019). Stage 1 Competency Standard for Professional Engineer.
[S4] Trinity College Dublin, Department of Computer Science. (undated). Final Year Project Evaluation Form and Marking Sheet (sample).
[S5] University of Oxford, Department of Computer Science. (2022). Examination Conventions, Parts A and B, 2022–23.
[S6] University of Warwick. (2026). CS310-30 Computer Science Project.
[S7] University College London. (2026). COMP0029 Individual Project for Year 3 BSc.
[S8] Aberystwyth University, Department of Computer Science. (2022). Major and Minor Project modules: Introduction.
[S9] Agile Business Consortium. (2026). What is MoSCoW Prioritization? (date per [I1]).
[S10] W3C. (2024). Web Content Accessibility Guidelines (WCAG) 2.2.
[S11] WebAIM. (2026). The WebAIM Million: 2026 report.
[S12] Nielsen, J. (2000). Why You Only Need to Test with 5 Users. Nielsen Norman Group.
[S13] OWASP. (2021). OWASP Top 10:2021.
[S14] Green Software Foundation. (2024). Software Carbon Intensity (SCI) Specification, ISO/IEC 21031:2024.
[S15] Jaeger-Helton, K. and Smyser, B. M. (2017). Switching Midstream, Floundering Early, and Tolerance for Ambiguity. ASEE Annual Conference.
[S16] Howe, S. et al. (c. 2018). Preliminary Results from a Study Investigating the Transition from Capstone Design to Industry.
[S17] Howe, E. (2018). Pitfalls to Avoid in Industry Capstone Project. ASEE CIEC.
[S18] Bijlsma, A. et al. (2021). How do Students Test Software Units? IEEE/ACM ICSE-SEET.
[S19] Matthies, C., Treffer, A. and Uflacker, M. (2017). Prof. CI. IEEE Frontiers in Education.
[S20] Hassani, H. et al. (2018). Supervision of Undergraduate Final Year Projects in Computing: A Case Study. Education Sciences 8(4):210.
[S21] Riddle, S., Forshaw, M., Zarb, M. et al. (2026, in press). The Computing Dissertation: Lessons from a UK Practitioner Network. ACM.
[S22] University of Kent. (undated). Supervision: Introduction (EPCOS teaching resource).
[I1] Agile Business Consortium. (2026). What is MoSCoW Prioritization?
[I3] Alaways, L. (2010). Factors that Inhibit or Enable Success of Capstone Design Teams. Mid-Atlantic ASEE Conference.
[I5] Jaeger-Helton, K. and Smyser, B. M. (2017). Same study as [S15].
[I6] Sedelmaier, Y. and Landes, D. (2020). Analyzing Challenges in Software Engineering Capstone Projects. ICSEA 2020.
[I7] Chisnall, D. (undated). Advice for project students. University of Cambridge.
[I8] Reddington, J. (2025). Things I say to project students. Personal blog.
[I9] University of Sussex, School of Engineering and Informatics. (2022). Final Year Projects: Information for supervisors.
[I11] Bona, F. et al. (2023). Understanding the Gaps in Software Engineering Education from the Perspective of IT Leaders. CSEDU 2023.
[I12] Chang, J. (2009). Exploding Software-Engineering Myths. Microsoft Research.
[I13] Budiu, R. (2021). Why 5 Participants Are Okay in a Qualitative Study, but Not in a Quantitative One. Nielsen Norman Group.
[I14] Mountain Goat Software. (2016). Are 64% of Features Really Rarely or Never Used?
[I15] WebAIM. (2026). The WebAIM Million: 2026 report (same as [S11]).
[I16] University of Cambridge, Department of History and Philosophy of Science. (undated). Human participants (research ethics).
[I17] Vijayakumar, S. (2017). Things always take longer than expected. Always. Donders Wonders blog.
