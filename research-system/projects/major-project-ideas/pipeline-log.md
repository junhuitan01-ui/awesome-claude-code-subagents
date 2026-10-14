# Pipeline log: major-project-ideas

- **Date:** 14 October 2026
- **Project:** major-project-ideas (example run requested by Junhui: "use john and jane and craft an example report with the topic on additional ideas for major project")
- **Orchestrator:** Claude Code cloud session running `/deliver major-project-ideas` by hand (the custom agents are run as general-purpose subagents given each agent file as their instructions, because this session was not started inside `research-system/`).
- **Required deliverables:** `report.docx`, `report.pdf`
- **Success criteria:** answers all four research questions with citations; at least eight concrete ideas with why and effort; a prioritisation method; every fact cited to an opened source, gaps disclosed; readable by a beginner.
- **Tools:** WebSearch and WebFetch work in this session. Direct downloads with curl are blocked by the network policy (not needed). python-docx, python-pptx, openpyxl, reportlab and pypdf are installed.

## Research angles (assigned before launch)
- **John (researcher), default angle:** official and primary sources first (university handbooks and rubrics, accreditation and standards bodies), then peer-reviewed work; answer each question directly.
- **Jane (independent-researcher), assigned angle:** differs in all three ways. *Search strategy:* counter-framed queries ("capstone scope creep", "why capstone projects fail", "gold plating", "student project overcommitment"). *Source mix:* education research on student and team experience, industry/practitioner sources on project risk, and employer/portfolio perspectives. *Perspective:* cost, trade-off and risk (what each addition costs and what can go wrong).

## Steps
| Step | Agent | Files produced | Outcome |
|------|-------|----------------|---------|
| 1b Independent research | independent-researcher (Jane) | 01-research/independent-sources.md, independent-research.md | Done. 18 sources opened ([I1]–[I18]), 6 leads listed as not verified. |
| 1a Research | researcher (John) | 01-research/sources.md, research-notes.md | Done after one interruption (the account hit its usage limit around 07:40 UTC; resumed at 11:04 UTC). 22 sources opened ([S1]–[S22]); ACM Code of Ethics final text could not be loaded (listed as not verified). |
| 1c Debate | researcher (John) + independent-researcher (Jane), run together | 01-research/debate/primary-rebuttal.md, independent-rebuttal.md; updated independent-research.md | Done. Both rebuttals cite only IDs that exist in the two sources files (checked with grep: S1–S22, I1–I18). |
| 2 Judge + Analyse | analyst | 02-analysis/debate-verdict.md, analysis.md | Done. Winner: John (primary), weighted 4.00 vs Jane 3.55; no guard applied. Nine carry-over points from Jane (CO1–CO9). No blocking research requests. |
| 3 Write | writer | 03-drafts/draft.md | Done. About 2,480 words (sections 1–7), 11 ideas, 7-step method, 2 evidence-gap markers. |
| 4 Review 1 | reviewer | 04-reviews/review-1.md | REVISE: 0 blocker, 1 major (R1: [I6] percentages were per-category, not of all issues), 10 minor. Reviewer spot-checked WebAIM, MoSCoW (confirms the 28 May 2026 date) and [I6] live. |
| 5 Improve 1 | improver | 05-revised/revised-1.md, changes-1.md | 11 fixed, 0 partly, 0 not fixable. Sections 1–7: 2,488 words. |
| 4 Review 2 | reviewer | 04-reviews/review-2.md | PASS. All 11 review-1 findings fixed. 2 new minor findings left open (R12: "four ideas have a cost source" but only three rows are unlabelled; R13: W3C and ISO not spelled out). No blocker or major open, so no second revision. |
| 6 Format | formatter | 06-formatted/report.md, format-notes.md | Done. 33 references numbered in order of first use ([S9]/[I1] merged). R13 applied. R12 left open (content). Body 2,472 words without citation tags. |
| 7 Build | builder | 07-deliverables/report.docx (48,725 bytes), report.pdf (93,903 bytes, 9 pages); build/ scripts | Done. Checker: all expected files passed. |
| 8 Validate | orchestrator | validation-report.md | Done. Both files PASS; all success criteria met; one minor review issue (R12) left open. |
