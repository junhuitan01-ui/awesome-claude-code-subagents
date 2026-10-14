# Independent rebuttal (Jane)

## Opening statement

- **The brief asks about trade-offs, and my report measures them.** Two of the four research questions (RQ3 and RQ4) are about scoping and risk. RQ2 asks for ideas with "how much effort it costs". My report gives evidence on what specific additions cost:
  - testing at 15–35% extra time [I12];
  - five vs 30–40+ users for usability testing [I13];
  - a six-issue accessibility pass vs full conformance [I15];
  - ethics review taking up to three weeks or more [I16].
  
  John's report says plainly that "Effort estimates (low / medium / high) for each idea are not in any source" (Gaps).
- **My under-delivery evidence is more systematic.** John calls his under-delivery evidence "thin". My report adds a systematic qualitative analysis of 79 capstone post-mortems [I6]. It also adds converging evidence on time underestimation from students, newcomers and planning research [I3][I6][I11][I17].
- **My report surfaces a real conflict that John's leaves out.** Supervisors disagree on how ambitious a project should be [I7][I8][I9]. Students need this tension resolved to make scoping decisions, and John's report does not cover it.
- **My report flags limits on repeated rules of thumb.** I used NN/g's 2021 article [I13] instead of the 2000 one. I also flagged the unsound "64% of features never used" statistic [I14].

## Strongest points

1. **Cost evidence for the Effort column.** The figures above come from [I12], [I13], [I15] and [I16]. They let the writer rate effort with sources rather than leave every rating as an evidence gap.
2. **Time underestimation is well supported.** Four independent sources agree:
   - Students' honours theses took 55.5 days against an estimate of 33.9 days, which was beyond even their pessimistic estimate [I17].
   - IT leaders say newcomers "tend to underestimate the difficulty of the tasks" [I11].
   - Timeliness was the top organisational challenge in SE capstone post-mortems [I6].
   - Lack of time management was the second barrier in engineering capstones, cited by 46.6% [I3].
   
   Together these justify holding contingency before adding any extras.
3. **Non-technical issues were the bigger challenge.** "technical issues tend to be less challenging than non-technical ones" [I6]. Documentation and requirements were the most frequent professional and technical challenges [I6].
4. **Ambition: depth versus breadth.** The supervisor sources conflict:
   - one advises a modest proposal with extensions held back [I7];
   - one says most students are insufficiently ambitious, but to go "deeper rather than wider" and avoid bolt-on apps [I8];
   - Sussex tells supervisors to encourage ambition while planning for setbacks [I9].
   
   My report proposes a reconciliation: be ambitious in the core problem and cautious about bolt-on extras. This is labelled as interpretation.
5. **Second-order costs of additions.** Each extra itself needs testing, documentation and evaluation [I4][I6]. Unfinished extras add risk without marks [I7][I12] (interpretation).
6. **Secrets hygiene for public portfolio repositories.** GitGuardian found 28,649,024 secrets in public GitHub commits in 2025 [I18]. This is a cheap, concrete security idea. It is a vendor source, as flagged in my report.

## Challenges to the other report

| Their claim (quote + location) | Problem | Evidence | Severity |
|---|---|---|---|
| "Effort estimates (low / medium / high) for each idea are not in any source." (Gaps and uncertainties) | **Missing evidence.** Cost evidence exists for several ideas. The brief requires an Effort column, so John's report leaves the writer to guess or to flag every row as a gap. | [I12][I13][I15][I16] | major |
| "No opened source states timelines." (Q4, ethics approval) | **Missing evidence.** One department states review "can take up to three weeks (longer if revisions are required)". | [I16] | minor |
| Nielsen recommends "testing no more than 5 users"… "the article is from 2000." (Q2, user testing) | **Outdated source.** John flags the date himself, but relies on it. NN/g's 2021 article limits the five-user rule to qualitative studies. It says quantitative claims need "usually more than 30" users, and that the 31% assumption comes from early-1990s projects. Students claiming usability metrics from five users would be making unsupported claims. | [I13] | minor |
| Automated testing and CI: "73% of respondents agreed… 88% would consider CI" (Q2) | **One-sided.** Only benefits are presented, from a small, mostly self-reported study (John's own reliability note on [S19]). The time cost is not mentioned, although the brief asks for effort. Industrial TDD teams took 15–35% longer. | [S19][I12] | minor |
| "What students under-deliver (evidence is thin; see Gaps)" (Q1) | **Missing evidence.** The evidence is thinner than it needs to be. A systematic analysis of 79 capstone post-mortems ranks timeliness, documentation and requirements among the top challenges. | [I6][I3] | minor |
| "Keep scope appropriate to the assessment … it is 'difficult to judge an appropriate and comparable level of complexity'" (Q3) | **Missing question.** John's report does not address the conflicting advice students actually receive on ambition, so a student gets no guidance on whether to aim higher or lower. | [I7][I8][I9] | minor |
| [S9] "undated web page" (sources.md) | **Wrong.** The same page (same URL) is dated 28 May 2026 and was last modified 9 September 2026. | [I1] | minor |

## Concessions

- **RQ1, what assessors value: John's report is clearly stronger.** It uses three accreditation bodies [S1][S2][S3] and five university rubrics or module specifications [S4][S5][S6][S7][S8], with mark weights such as TCD's 15% for testing and evaluation and 50% for technical content [S4]. My report deliberately left these sources out, so on this question it rests on one supervisor page [I7] and one department page [I9].
- **RQ2, breadth of ideas: John's report is stronger.** It ties each idea to a named standard:
  - WCAG 2.2 [S10];
  - OWASP Top 10 [S13];
  - SCI for sustainability [S14];
  - risk registers [S3];
  - budgeting [S16].
  
  My report has an explicit evidence gap on sustainability and deployment. The brief prefers accreditation and standards sources, and John's source mix matches that preference better.
- **Evidence on student testing.** John's [S18] and [S19] show student testing is weak and can be improved. My report had no student-specific testing evidence; its [I12] comes from professional teams.
- **Agreement on shared findings.** We independently reached the same reading of three shared sources:
  - MoSCoW's 60% Must / about 20% Could guidance [S9]=[I1];
  - the WebAIM figures and the caveat that automated checks do not prove conformance [S11]=[I15];
  - the finding that scope change need not lower outcomes, so how teams manage change matters more [S15]=[I5].
  
  Our separate searches converged on these points, which makes them more reliable.
- **Recency and source quality.** John's sources are generally more recent and more authoritative. Mine include pre-2015 sources [I3][I12][I17], a Wikipedia page [I4], a vendor report [I18] and a personal blog [I8].
- **Tick-box process artefacts.** John found evidence that required process artefacts can be done for show [S17][S22]. This is a useful risk my report did not cover.

## Defence

- **"Jane's sources are older and weaker."** This is partly true. [I3] (2010), [I12] (2009) and the 1994 study behind [I17] fall outside the brief's rough window, and I flagged them as such. They were the best cost and estimation evidence I found. Their direction is supported by newer sources: [I6] from 2020 and [I11] from 2023 on underestimation, and [I13] from 2021 on user testing. I would accept the Analyse agent preferring the newer sources where they overlap.
- **"Opinion pieces and Wikipedia."** [I4] is used only for a definition, and [I8] only for one side of a conflict that is labelled as opinion. Neither supports a factual claim about outcomes.
- **"The TDD figures don't apply to students."** I agree, and said so in section 6 of my report. They are a ceiling-style indicator that testing costs real time, not a student estimate.
- **"The GitGuardian report is a vendor source."** This was disclosed. The recommendation drawn from it, keeping secrets out of the repository, does not depend on the exact figure.
- **"No accreditation coverage."** That was by design under my assigned angle. I concede it is a weakness for RQ1 (see Concessions).
