# Debate verdict — major-project-ideas

**Date:** 14 October 2026
**Inputs judged:** `01-research/research-notes.md` + `sources.md` (John, primary, [S1]–[S22]); `01-research/independent-research.md` + `independent-sources.md` (Jane, independent, [I1]–[I18]); `01-research/debate/primary-rebuttal.md`; `01-research/debate/independent-rebuttal.md`. All six files exist and are complete. Jane's §4 and §7, which John's rebuttal called empty placeholders, are now filled in. The pipeline log records that her report was updated during the debate round, so I judged the current version.

## Winner
**Primary (John) wins.** His report answers all four research questions directly, from the sources the brief prefers: three accreditation bodies, five university rubrics or module pages, and named standards. Jane's report deliberately leaves out accreditation and rubric evidence, has gaps on sustainability and deployment, and leans more on weak or pre-2015 sources. Jane's report adds evidence John lacks on effort, under-delivery, user-testing limits and ambition, and that evidence is carried over below.

## Scorecard

| Criterion | Weight | Primary (John): score + reason | Independent (Jane): score + reason |
|---|---|---|---|
| Argument | 20% | **4**: 5 of his 10 challenges upheld (including both majors), 4 partly upheld, 1 no longer applies. His concessions are generous and accurate, and his defence holds. | **4**: 5 of her 7 challenges upheld and 2 partly upheld. Her concessions are honest. But her rebuttal repeats the overreach that "four independent sources agree" on time underestimation (see C-J9). |
| Points | 20% | **4**: answers RQ1–RQ4 directly, with 12 candidate additions and a prioritisation method. He misses effort and cost evidence, the debate over how ambitious to be, and he calls his own under-delivery evidence thin. | **3**: strong on RQ3 and RQ4 and on the cost of each addition. But RQ1 ("what assessors value") rests on one supervisor page and one department, and RQ2 has gaps on sustainability and deployment, with security covered only through a vendor report. |
| References | 25% | **4**: ABET, BCS, Engineers Australia, W3C, OWASP, the Green Software Foundation, and peer-reviewed studies. Weaknesses: some sources were read only at abstract level ([S15][S18][S21]), [S12] is from 2000, [S22] is undated with no named author, and [S9] is wrongly recorded as undated. | **3**: has good sources ([I6][I9][I13][I15][I1]), but also Wikipedia [I4], a personal blog [I8], a vendor report [I18], three pre-2015 sources behind central claims ([I3][I12], and the 1994 study behind [I17]), and abstract-only reads ([I5][I10]). Every weakness is disclosed. |
| Content | 25% | **4**: accurate and specific, with confidence tags and uncertainty disclosed. One factual slip ([S9] "undated"), one gap that was in fact covered by an available source (ethics review timelines), and a CI entry that lists only benefits. | **4**: accurate and specific, with explicit fact / claim / interpretation labels and a thorough §6 on source quality. Two overreaches: rating time underestimation "moderate-to-high" on four sources when only two measure underestimation, and proposing 2009 data from professional teams [I12] as an effort anchor for students. |
| Formatting | 10% | **4**: clear structure by question, consistent tags and citations, with gaps and a "Not verified" list. | **4**: follows the independent-researcher structure (9 sections, now complete) with consistent tags and citations. |
| **Weighted total** | 100% | **4.00** | **3.55** |

**Guards:** not applied. John's References score is one point above Jane's, and Content is equal, so neither report trails by two or more on References or Content. The weighted totals are not tied.

## Challenges ruled on

| From | Challenged claim | Ruling | Why |
|---|---|---|---|
| John (C-J1) | Jane did not cover accreditation criteria or marking rubrics (§2) | **Upheld** (major) | Her §2 states it plainly. The brief's RQ1 asks what assessors value and names rubrics and accreditation bodies as preferred sources. Her RQ1 then rests on [I7] (a personal page) and [I9] (one department). Leaving them out was by design, but the brief still needs them. |
| John (C-J2) | "Your marks come from your dissertation, not your project" [I7] overstates the case | **Partly upheld** | [I7] is a single, undated personal page, but Jane labelled it "one supervisor's view; single source" and did not generalise it. John's counter-evidence is weaker than he presents it. [S4] is a *report* marking sheet, so its 50% technical weight is also judged through the report, and [S7] says a higher mark depends on report quality. The point that it should not be generalised stands. The point that it "overstates" the role of the report is not shown. |
| John (C-J3) | Evidence gap on sustainability | **Upheld** (major) | Jane's §8 records the gap. [S1] (outcome 2, "environmental ... factors"), [S3] (1.6c, 2.4f) and [S14] (SCI) give both a reason and a method. |
| John (C-J4) | Deployment covered only through secrets hygiene | **Partly upheld** | It is a gap in Jane's report. But John's own support is indirect: [S2] "real need in a wider context" and the CITP outcome "deploy, verify and maintain". He labels it "single source; indirect" himself. Both reports are weak here. |
| John (C-J5) | Security rests only on the vendor report [I18] | **Upheld** (minor) | [I18] is a vendor report (Jane flags this) and covers one narrow risk. Only [S13] (OWASP Top 10) gives a standard for the wider security idea. |
| John (C-J6) | 2009 TDD figures from professional teams [I12] proposed as an effort anchor | **Partly upheld** | The date and population caveats are correct, and Jane states them herself (§6). Proposing the figures as an anchor for student effort (§9.1) is an overreach. But John's alternative [S19] gives no time cost at all, so [I12] remains the only cost evidence for testing. Use it only as a caveated pointer. |
| John (C-J7) | Gold plating defined through Wikipedia [I4] | **Partly upheld** | The source has low reliability. Jane uses it only for a definition and says so. The term can be used, but it carries little evidential weight. |
| John (C-J8) | Planning-fallacy figures [I17] come second-hand from a 1994 study | **Upheld** (minor) | [I17] is a blog report, and the original is on Jane's own "Not verified" list. It falls well outside the brief's 2015+ window. |
| John (C-J9) | "Students and newcomers underestimate time [I3][I6][I11][I17]" tagged moderate-to-high | **Upheld** | [I3] measures "scheduling conflicts" and "lack of time management", and [I6] codes "time aspects and timeliness". Neither measures underestimation. Only [I11] (25 IT leaders, about newcomers to industry) and [I17] (a 1994 study reported second-hand) do. Jane's own RQ3 tag correctly cites only [I11][I17], but her §4, §8 and rebuttal widen it to four sources. The supportable reading is: time management is a well-supported weakness (medium-high), and underestimation specifically is low-medium. |
| John (C-J10) | Jane's §4 and §7 are empty placeholders | **Rejected (no longer applies)** | The current `independent-research.md` has both sections filled. They were completed during the debate round, which the placeholder text anticipated. Note: §7 was written after Jane saw John's report, so it is not a blind comparison. |
| Jane (C-I1) | "Effort estimates (low / medium / high) for each idea are not in any source" | **Partly upheld** (major) | John's statement is literally true: no source gives low/medium/high ratings. But cost evidence exists for four ideas: testing time [I12], number of usability-test users [I13], the scope of a basic accessibility pass [I15] and ethics-review lead time [I16]. The other ratings remain judgement. |
| Jane (C-I2) | "No opened source states timelines" for ethics approval | **Upheld** (minor) | [I16] states that referred cases "can take up to three weeks (longer if revisions are required)". It is one non-computing department at one university, so it is an example, not a norm. |
| Jane (C-I3) | Relies on the 2000 five-user article [S12] | **Upheld** (minor) | John flags the date, but [I13] (2021, same organisation) limits the five-user rule to qualitative studies, says quantitative claims need "usually more than 30" users, and notes the 31% assumption comes from the early 1990s. This is a material limit for students who report usability metrics. |
| Jane (C-I4) | CI benefits presented one-sidedly [S19] | **Partly upheld** | John's Q2 CI entry gives benefits only, from a small, self-reported study, with no cost. The only cost evidence ([I12]) is from 2009 and covers professional teams, so the omission is understandable, but the trade-off should be stated. |
| Jane (C-I5) | Under-delivery evidence is "thin" when [I6] exists | **Upheld** | John concedes it. [I6] (79 post-mortems, 13 teams, nine years, one institution) is the most systematic under-delivery evidence in either report. |
| Jane (C-I6) | The conflict over how ambitious to be is not addressed | **Upheld** | John concedes it. [I7][I8][I9] give conflicting advice, and none of John's sources resolve it. |
| Jane (C-I7) | [S9] recorded as an "undated web page" | **Upheld (provisionally)** | Same URL (agilebusiness.org/?p=1907). Jane recorded a specific date (28 May 2026) and a last-modified date (9 September 2026), and John did not dispute it (the rebuttals were written at the same time). I could not re-open the page: the analyst has no web tools. The more specific record is preferred. The reference should read Agile Business Consortium (2026), accessed 14 October 2026. The 2026 date is probably a republication date for long-standing DSDM guidance, not when MoSCoW was first written. |

## Where the reports agree
Where two different angles reach the same reading, confidence rises. Three of these points rest on the *same* sources, so that agreement is not fully independent.
- **MoSCoW and its effort limits.** Must Haves typically ≤60% of effort, Could Haves about 20% as contingency, and Won't Haves recorded. Both note it is industry guidance not tested on students [S9]=[I1]. *Shared source.*
- **Accessibility.** 95.9% of the top one million home pages have detected WCAG 2 failures, averaging 56.1 errors per page, and automated checks do not prove conformance [S11]=[I15]. *Shared source.*
- **Scope change.** About 46% of projects in one capstone offering changed substantially, with no statistical difference in outcomes. How change is managed matters more than whether it happens [S15]=[I5]. *Shared source; abstract-only in both reports.*
- **Time management is a common student weakness.** This agreement is independent: [S17][S20][S22] versus [I3][I6].
- **Evaluation and the write-up matter for marks.** This agreement is independent: rubrics and accreditation [S2][S4][S5][S6] versus supervisor guidance [I7].
- **Extras without evidence earn no credit** ([S4][S5][S11][S17]; [I7]).
- **User studies bring an ethics-approval burden** ([S21]; [I16]).
- **No source quantifies how much any addition raises a grade.** Both reports list this as a gap.

## Strong points from the losing report (Jane)

| # | Point | Sources | Carry over? |
|---|---|---|---|
| CO1 | [S9]'s date: dated 28 May 2026, last modified 9 September 2026 | [I1] | **Carry over** (corrects a factual error) |
| CO2 | Ethics review can take up to three weeks, longer if revisions are needed (one department); Sussex expects ethics to be considered by the Interim Report | [I16][I9] | **Carry over** (corrects "no opened source states timelines") |
| CO3 | Five users are enough only for *qualitative* usability tests; quantitative claims need >30 users (40+ for narrow intervals); the model's assumptions date from the early 1990s | [I13] | **Carry over** (material limit on [S12]) |
| CO4 | Automated testing has a real time cost: industrial TDD teams took 15–35% longer for 60–90% lower defect density; coverage is not the best measure of quality (2009, professional teams) | [I12] | **Carry over** with caveats (material limit on the one-sided CI entry) |
| CO5 | Under-delivery is mostly non-technical: timeliness 26.15%, documentation 21.77%, requirements 20.16% of coded issues; "technical issues tend to be less challenging than non-technical ones"; time-management barriers in a 2010 engineering survey | [I6][I3] | **Carry over** (fills the gap the winner calls thin) |
| CO6 | Supervisors disagree on how ambitious to be (modest proposal with extensions held back vs "insufficiently ambitious" / go "deeper rather than wider" vs "as ambitious as possible" while planning for setbacks) | [I7][I8][I9] | **Carry over** (material for scoping advice) |
| CO7 | Six error types cover 96% of automatically detected accessibility errors, so a basic pass is cheap and full conformance is not | [I15] | **Carry over** (effort evidence the brief requires) |
| CO8 | Students underestimate time (estimated 33.9 days, took 55.5 days); newcomers underestimate task difficulty | [I17][I11] | **Carry over** at low-medium confidence (supports holding a buffer; old, second-hand and non-student caveats) |
| CO9 | Do not use the "64% of features rarely or never used" statistic (it comes from four internal applications) | [I14] | **Carry over** as a guard |
| — | Keep secrets (API keys) out of public portfolio repositories | [I18] | Not carry over. Optional low-effort security example, with a vendor-source caveat |
| — | Gold plating and the second-order costs of each addition (its own tests, documentation and evaluation) | [I4][I6] | Not carry over. Optional, labelled interpretation; [I4] is low reliability |
| — | Time-boxed milestones in a student design module drew positive feedback | [I10] | Not carry over. Optional support for John's checkpoints (abstract only, no outcome data) |
| — | Propose a modest project and list extensions in the proposal | [I7] | Used inside CO6 and the prioritisation method |
