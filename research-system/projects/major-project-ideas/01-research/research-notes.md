# Research notes — major-project-ideas (primary researcher, "John")

Angle: official and primary sources first (accreditation bodies, university handbooks and rubrics, standards bodies), then peer-reviewed work.

## Research questions
1. What do capstone and final-year project guides and assessors value, and which of those qualities do students often under-deliver?
2. What additional ideas or features are commonly recommended to strengthen a major project (user testing, accessibility, automated testing, security, documentation, data/evaluation, ethics, sustainability, deployment)? Concrete examples.
3. How should a student choose, prioritise and scope additions (must-have vs stretch, time and risk)?
4. What are the risks or downsides of adding extra ideas, and how can they be managed?

## Findings

### Q1: What assessors value, and what students under-deliver

**What accreditation bodies require**
- ABET requires engineering programmes to include "a culminating major engineering design experience that 1) incorporates appropriate engineering standards and multiple constraints" (Criterion 5). It defines engineering design as devising a system, component or process "to meet desired needs and specifications within constraints". [S1] (single source for the ABET wording)
- ABET's seven student outcomes (Criterion 3) include:
  - designing with "consideration of public health, safety, and welfare, as well as global, cultural, social, environmental, and economic factors" (outcome 2);
  - communicating "with a range of audiences" (outcome 3);
  - ethical and professional responsibility (outcome 4);
  - teamwork and planning (outcome 5);
  - developing and conducting "appropriate experimentation, analyze and interpret data" (outcome 6);
  - acquiring new knowledge (outcome 7). [S1] (single source)
- BCS requires the individual project report to contain:
  - "elucidation of the problem and the objectives";
  - "an in-depth investigation of the context and literature";
  - where appropriate, the life-cycle stages, use of tools, and "how verification and validation were applied";
  - "a critical appraisal of the project, indicating the rationale for any design/implementation decisions";
  - "evaluation (with hindsight) of the project outcome and the process of its production". [S2 §2.5] (single source)
- BCS also expects undergraduate projects to show that the project "meets a real need in a wider context" and to include "critical self-evaluation of the process" (§2.5.1). Legal, social, ethical and professional issues "should be referred to in the project" (§2.6.1). [S2] An Aberystwyth handbook page restates the same BCS expectations ("real need in a wider context", critical self-evaluation) and asks for "a quality solution together with an evaluation of that solution". [S8] (confirmed: a professional body plus a university that applies it [S2][S8])
- BCS says projects based only on literature review or surveys are not acceptable; projects must involve practical computing work (§2.5.3). [S2] (single source)
- Engineers Australia's Stage 1 competencies include:
  - "Application of systematic approaches to the conduct and management of engineering projects" (2.4);
  - identifying and managing "technical, health, environmental, safety and other contextual risks" (2.1);
  - "Commitment to sustainable engineering practices" (2.4f) and sustainability principles (1.6c);
  - "Ethical conduct and professional accountability" (3.1);
  - preparing "high quality engineering documents such as progress and project reports" (3.2b). [S3] (single source)
- Taken together, three accreditation bodies in three countries name similar qualities: design within constraints, testing or experimentation and evaluation, communication and documentation, ethics, and project or risk management. [S1][S2][S3] (confirmed: 3 independent bodies)

**What university rubrics reward**
- Trinity College Dublin's default final-year project weights are:
  - problem statement, motivation and analysis: 10%;
  - background research and literature review: 15%;
  - technical content and project execution: 50%;
  - testing, evaluation, critical analysis and conclusions: 15%;
  - report presentation and writing: 10%.
  
  Its top band asks for "an element of originality" and "evidence of sound critical evaluation". [S4] (single source; one institution)
- Oxford's first-class criteria for the Part B Computer Science project say the project should satisfy nearly all of the following: it "addresses a well-rounded collection of relevant concerns"; "uses appropriate technology; shows some aspects of originality"; "involves a significant amount of analysis or assessment of results"; and "is written up in a clear report". Only about the top 5% normally score above 80, for "outstanding originality". [S5] (single source)
- Assessment usually covers more than the product. At Warwick, CS310 gives 15% to a progress report, 75% to the final report plus viva, and 10% to a separate 1,000-word project management report. Its outcomes include planning "resources, timetabling, and professional issues" and "reflective writing". [S6] UCL COMP0029 names planning, "realistic work commitments", report writing and "good problem solving and evaluation skills" as outcomes, and says a higher mark depends on report quality as well as the project work. [S7] (confirmed: planning, reporting and evaluation are assessed alongside the artefact at several universities [S4][S6][S7][S8])

**What students under-deliver** (evidence is thin; see Gaps)
- **Testing.** In a study of students who had no formal testing education, "students do not test systematically, while most of them think they do test systematically", and they could mostly "only think of test cases based on programming code". [S18] (single source; introductory students, not capstone students)
- **Writing tests.** In a CI-based exercise, the average number of manually written tests per student in the following project rose from 1.6 to 4.3, and the share of students writing at least one test rose from 24% to 61%. [S19] This implies a low baseline of test-writing before the intervention. (single source; small sample)
- **Communication, documentation and budgeting.** Recent capstone graduates said students often treat communication and documentation as secondary to technical work. Project budgeting had the lowest preparedness rating (mean 5.0 on a 7-point scale, N=21 of 54; mean minimum 4.2). [S16] (single source; preliminary, small sample)
- **Evidence for conclusions.** One instructor reports capstone teams presenting root causes with "barely any evidence (data or process analysis) to validate the root cause". [S17] Rubrics give 15% or more to testing and evaluation and ask for "significant ... analysis or assessment of results" [S4][S5], which shows assessors value this. Whether students commonly fall short on it is supported by only one practitioner report [S17]. (uncertain/conflicting: no systematic data)
- **Time management.** Students "perceive the 15-week time frame for a project as something to start worrying about half-way through the semester" [S17]. A computing FYP case study notes students "might also have difficulties in their time management" [S20]. An educator resource notes that potential failures "discovered near the end of a large project are far more difficult to retrieve" [S22]. (confirmed: 2+ sources, though each is weak [S17][S20][S22])
- **Process artefacts done for show.** Students admitted "making up content" for required process artefacts such as ground rules, to satisfy the assignment. [S17] (single source)

### Q2: Commonly recommended additions, with concrete examples
Each idea below is tied to a standard or rubric that values it. No single source lists these as "add-ons".

- **User or usability testing with small rounds.** Nielsen recommends "testing no more than 5 users and running as many small tests as you can afford". His model estimates that about 85% of problems are found by five users, that all problems would need at least 15, and that three studies of five users beat one study of 15. Caveats: distinct user groups need 3–4 users each, and the article is from 2000. [S12] (single source) This links to ABET outcome 6 (experimentation and data) [S1] and BCS validation and evaluation [S2].
- **Accessibility to WCAG 2.2 level AA.** WCAG 2.2 has been a W3C Recommendation since 12 December 2024. It has four principles (perceivable, operable, understandable, robust) and three conformance levels (A, AA, AAA). [S10] The problem is common in real sites: 95.9% of the top one million home pages had detected WCAG 2 failures, averaging 56.1 errors per page. The most common failures were low-contrast text (83.9%), missing alt text (53.1%) and missing form labels (51%). [S11] Concrete example: fix contrast, alt text and form labels, then report an automated and manual check. Caveat from WebAIM: "Absence of detected errors does not indicate that a page is accessible or conformant." [S11] (confirmed for the standard and for prevalence: [S10][S11])
- **Automated testing and continuous integration (CI).** BCS asks the report to describe verification and validation and the use of tools [S2]. In the Prof. CI study, 73% of respondents agreed that writing their own tests helped them learn, 88% would consider CI for their own projects, and test-writing rose in the next project [S19]. Concrete example: unit tests run automatically on each push, for example through GitHub workflows [S19]. (single source for the effect; [S2] for the requirement)
- **Security review against the OWASP Top 10.** OWASP calls the Top 10 "a standard awareness document for developers and web application security". The 2021 categories include A01 Broken Access Control, A03 Injection and A06 Vulnerable and Outdated Components. [S13] Concrete example: check the app against each category and record the mitigations. Note: a 2025 Release Candidate exists and was not reviewed. [S13] (single source)
- **Ethics, privacy and professional issues section.** Required or valued by BCS (§2.6.1, issues "should be referred to in the project") [S2], ABET outcome 4 [S1] and Engineers Australia 3.1 [S3]. Educators also list ethics approval as a common project-module challenge [S21]. (confirmed: 3+ sources)
- **Sustainability analysis.** Required or valued by Engineers Australia (1.6c, 2.4f) [S3] and ABET outcome 2 ("environmental ... factors") [S1]. A concrete software method is the Green Software Foundation's SCI, ISO/IEC 21031:2024: SCI = (E × I + M) per R, where E is energy, I is carbon intensity, M is embodied hardware emissions and R is a functional unit such as per user or per API call. [S14] (confirmed that it is valued [S1][S3]; method from one source [S14])
- **Use of named standards.** ABET requires "appropriate engineering standards" in the culminating design experience. [S1] Citing WCAG [S10], OWASP [S13] or SCI [S14] gives a project an explicit standard to design and test against. (single source for the requirement)
- **Evaluation against objectives, plus critical reflection.** BCS requires "evaluation (with hindsight)" of the outcome and the process, and "critical self-evaluation" [S2]. TCD weights testing and evaluation at 15% [S4]. Oxford asks for "significant ... analysis or assessment of results" [S5]. Warwick requires reflective writing [S6]. (confirmed: 4+ sources)
- **Documentation and a project-management record.** Warwick assesses a separate 10% project management report [S6]. Engineers Australia expects "high quality engineering documents" [S3]. BCS expects a description of life-cycle stages and tools [S2]. (confirmed)
- **Risk register or risk analysis.** Engineers Australia 2.1 expects students to identify, quantify, mitigate and manage technical and other risks [S3]. (single source among the opened standards)
- **Deployment or real-user context.** BCS asks that the project "meets a real need in a wider context" [S2][S8], and the CITP outcome includes the ability to "deploy, verify and maintain information systems" [S2]. No source specifically about deployment as a capstone add-on was opened. (single source; indirect)
- **Budget or cost estimate (engineering projects).** Graduates felt least prepared for project budgeting, and the authors suggest more exposure to it in capstone [S16]. Design for manufacturing was also requested [S16]. (single source)

### Q3: Choosing, prioritising and scoping additions
- **MoSCoW.** The Agile Business Consortium defines:
  - Must Have: the "Minimum Usable SubseT (MUST) of requirements which the project guarantees to deliver";
  - Should Have: "Important but not vital";
  - Could Have: "Wanted or desirable but less important", forming "the main pool of contingency";
  - Won't Have this time: agreed exclusions, recorded so they are not quietly reintroduced. [S9] (single source)
- **Effort limits.** Must Haves should typically be no more than 60% of effort, with about 20% of effort held in Could Haves as contingency. Higher Must-Have levels add risk unless estimates are accurate and the environment is low-risk. [S9] (single source; industry guidance, not tested on students)
- **Agree scope in writing early.** UCL requires a supervisor-approved Project Plan (mid-November) and Interim Report (late January) [S7]. Warwick requires a Project Specification in term 1 and a progress report in term 2 [S6]. One university introduced approved proposals partly to resolve scope disputes [S20]. A written problem statement "holds the company accountable for the scope" in sponsored projects [S17]. (confirmed: 4 sources)
- **Use regular supervision and checkpoints.** "weekly meetings play a crucial role in the success of the students" [S20]. Aberystwyth expects weekly supervisor meetings and a mid-project demonstration in week 7 [S8]. Early deadlines such as Gantt charts were used to counter late starts [S17]. (confirmed)
- **Choose additions that map to the marking criteria.** Rubrics and standards reward evaluation, testing, ethics and professional issues, and documentation [S2][S4][S5][S6]. No source tested "map additions to rubric weights" as a prioritisation method directly. (uncertain: this is an inference)
- **Keep scope appropriate to the assessment.** Projects can be pitched too simple or too complex, and it is "difficult to judge an appropriate and comparable level of complexity" [S22]. UCL lists "make realistic work commitments" as a learning outcome [S7]. (confirmed, weakly)

### Q4: Risks and downsides of adding extras, and how to manage them
- **Time overrun.** Project work "can consume far more time than its assessment-worth", and supervisors should be ready to reduce workload [S22]. Students start late [S17] and struggle with time management [S20]. Mitigations: MoSCoW contingency (about 20% of effort in Could Haves) [S9] and early milestones [S6][S7][S17]. (confirmed, weakly)
- **Late failure is hard to recover.** "Potential failures discovered near the end of a large project are far more difficult to retrieve." [S22] Mitigations: interim reports and mid-project demonstrations [S7][S8]. (single source for the claim; mitigations documented)
- **Tick-box extras.** Required artefacts can be done superficially ("making up content") [S17], and assessment can push students toward heavier processes than the task needs [S22]. Mitigation: add only extras that are actually used and then evaluated. (single source each; inference for the mitigation)
- **Unsupported claims.** Testing that is believed systematic but is not [S18], and conclusions with "barely any evidence" [S17]. An extra such as "accessibility" or "security" claimed without evidence will not meet evaluation criteria [S4][S5]. Automated accessibility checks alone do not prove conformance [S11]. (confirmed)
- **Scope changes mid-project.** About 46% of projects in one capstone offering changed topic or scope substantially after significant work, and about 16% launched late. There was "no statistical difference between prototype/success scores" for those teams (p = .05). High-scoring teams valued flexibility and time management. [S15] This suggests well-managed change need not reduce marks. (single source)
- **Ethics approval as an added burden.** Adding user studies can trigger ethics approval, which educators list as a common project-module challenge [S21]. Mitigation: plan for approval early. No opened source states timelines. (single source; inference)
- **Core work must still be the main thing.** The largest TCD weight (50%) is technical content and execution [S4], and BCS requires practical computing work [S2]. Extras that crowd out the core artefact risk the largest mark component. (inference from the rubric weights; single rubric)

## Conflicting evidence
- **Do scope changes hurt outcomes?** Practitioner and educator sources treat late changes and scope problems as risks [S17][S22]. The one controlled comparison found no statistical difference in success scores for teams that changed topic or started late [S15]. The difference may lie in how teams manage change rather than in the change itself, and the samples are not comparable.
- **Is formal process worth it?** Standards and rubrics reward systematic project management and documentation [S3][S6]. Two sources warn that required process artefacts can become box-ticking [S17] or heavier than the task needs [S22].
- **How many users to test with.** NN/g's five-user rule [S12] is from 2000 and has caveats about distinct user groups. NN/g's newer article on this question was not opened.
- **Which OWASP edition.** The 2021 edition is the current final list on the opened page, but a 2025 Release Candidate exists [S13]. The category names in the 2025 edition were not checked.

## Gaps and uncertainties
- **No systematic evidence on what students most often under-deliver** in final-year projects, such as a survey of assessors ranking weaknesses. The evidence is indirect: one introductory-student testing study [S18], one small CI study [S19], one preliminary graduate survey [S16], one instructor reflection [S17], and an undated educator resource [S22]. The full text of the most relevant recent work [S21] is embargoed until 12 November 2026.
- **No source quantifies the benefit to grades of any specific add-on** (accessibility, security, CI, sustainability). The case that each add-on helps rests on standards and rubrics valuing the quality, not on outcome data.
- **Effort estimates (low / medium / high) for each idea are not in any source.** The report's Effort column will need to be marked as the team's judgement or flagged as an evidence gap.
- MoSCoW's 60%/20% guidance [S9] comes from industry agile practice; no source was found that tests it on student projects.
- Rubrics come from UK, Irish and US/accreditation contexts. No Asian or Australian university rubric was opened, though Engineers Australia was [S3].
- Deployment and documentation (for example a README or user guide) as add-ons have only indirect support [S2][S3][S6].

## Not verified
- **ACM Code of Ethics and Professional Conduct (2018, final).** https://www.acm.org/code-of-ethics, https://ethics.acm.org/code-of-ethics/code-2018/ and the booklet PDF either failed to load or did not contain the principle text. Only "Draft 3" (CACM, January 2018, https://cacm.acm.org/magazines/2018/1/223896-acm-code-of-ethics/fulltext) was opened. It shows principles 1.2 "Avoid harm", 1.6 "Respect privacy", 2.1 high quality, and 2.5 "Give comprehensive and thorough evaluations of computer systems and their impacts, including analysis of possible risks". This is a draft, not the adopted text; do not cite it as the final Code.
- **OWASP Top 10:2025 Release Candidate** (owasp.org/Top10/2025/) was mentioned on the opened page but not opened.
- **NN/g "How Many Test Users in a Usability Study?"** (https://www.nngroup.com/articles/how-many-test-users/) was not opened.
- **ACM/IEEE CS2023 curriculum guidance on capstone projects** was not found or opened.
- **Capstone design national survey papers** (Howe et al., peer.asee.org, e.g. "capstone-design-courses-and-assessment-a-national-study.pdf") were listed in search results but not opened.
- **University of Sussex UG marking criteria** (sussex.ac.uk/ei/internal/documents/ugmarkingcriteria.pdf) were listed in search results but not opened.
- **The full text of S15** (PDF) and the full text of S18 were not read; only the abstracts and summary pages were.

## Method
- **Tools:** WebSearch (standard mode) and WebFetch were available and used. Bash and curl network access was not used, as instructed. No files were provided in 00-brief/.
- **Searches covered:**
  - ABET 2025–26 criteria;
  - final-year project marking criteria and handbooks (computer science);
  - BCS accreditation and individual project requirements;
  - Engineers Australia Stage 1 competencies;
  - ACM CS2023 capstone guidance;
  - MoSCoW (Agile Business Consortium);
  - WCAG 2.2, WebAIM Million, NN/g five users, OWASP Top 10, Green Software Foundation SCI, ACM Code of Ethics;
  - peer-reviewed work on capstone scope changes, student testing, CI in teaching, FYP supervision, and capstone pitfalls.
- **Fetches:** 22 sources were opened and are cited. Several fetches failed (the ACM Code pages) or returned only abstracts, as noted above. All were accessed on 14 October 2026.
- **Source order followed:** accreditation bodies and standards, then university rubrics and handbooks, then peer-reviewed studies, then educator resources.
- The work was paused by a usage limit and resumed. No sources were lost or changed by the interruption.
