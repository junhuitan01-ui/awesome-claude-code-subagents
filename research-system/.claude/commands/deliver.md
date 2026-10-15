---
description: Run the full research-to-deliverables pipeline for a project in projects/<name>
argument-hint: <project-name>
---

You are the **orchestrator** for the project in `projects/$ARGUMENTS/`. Run the pipeline below, in order, using the specialist subagents. Follow the rules in `CLAUDE.md`.

If no project name was given, list the folders in `projects/` and ask which one to run. Stop there.

## 0. Read the brief (before anything else)
1. Check `projects/$ARGUMENTS/00-brief/` contains `project-brief.md` and `deliverable-spec.md`. If either is missing or still has unfilled template text, stop and tell the user what to fill in. If `style-guide.md` is missing, copy `templates/style-guide.md` there.
2. Read all three files and any source files in `00-brief/`.
3. Create the work folders if missing, with one command: `mkdir -p projects/$ARGUMENTS/01-research/debate projects/$ARGUMENTS/02-analysis projects/$ARGUMENTS/03-drafts projects/$ARGUMENTS/04-reviews projects/$ARGUMENTS/05-revised projects/$ARGUMENTS/06-formatted projects/$ARGUMENTS/07-deliverables/build`.
4. Start `projects/$ARGUMENTS/pipeline-log.md` with: date, project name, the list of required deliverables (from "Files to deliver"), and the success criteria from the brief. Append one line per step below: step, agent, files produced, outcome.

**Saving agent output.** Claude Code doesn't let subagents save report files, so the research, analysis, writing, review, improve and format agents return their files in their reply between `=== FILE: <path> ===` and `=== END FILE ===` markers. After each of those agents finishes, save every block yourself with the Write tool, exactly as returned (don't edit or summarise), at the path given. Check the path is inside `projects/$ARGUMENTS/`. If an expected file block is missing, ask the agent once more; if it's still missing, log it as a failed step. The builder is different: it writes its scripts and files itself.

**Bash commands.** Run one plain command per Bash call from the `research-system` folder (no `cd`, `&&`, pipes or loops). `.claude/settings.json` pre-approves only simple commands such as `python3 tools/check_deliverables.py ...`; anything else stops for the user's approval.

When you call each subagent, give it: the project folder path, the exact files to read and write, the relevant parts of the brief (questions, audience, deliverables), and the step number. Each subagent starts with no memory of earlier steps, so pass anything it needs.

## 1. Research → `researcher` and `independent-researcher` (two separate tasks, then a debate)
Run two independent investigations of the same research questions, then one debate round where each argues its report is stronger. All of it finishes before step 2 starts.

**1a + 1b. Launch both researchers as separate tasks.** Issue the two subagent calls together in one message so they run in parallel and neither can see the other's output.
- **Before launching, assign the angles and log them.** The `researcher` uses its default angle (official and primary sources first, answering each question directly). Choose a *different* angle for the `independent-researcher`, differing in at least two of: search strategy, source mix, analytical perspective (see its agent file for options), fitted to this brief. The independent angle must always differ from the primary one. Record both angles in `pipeline-log.md`.
- `researcher`: pass the research questions from the brief. Returns `01-research/sources.md` and `research-notes.md` (source IDs `[S#]`).
- `independent-researcher`: pass the same research questions, the brief's scope and any ethical limits, the deliverables it must support, the style guide path, and its assigned angle. Tell it not to read the primary research files. Returns `01-research/independent-sources.md` and `independent-research.md` (source IDs `[I#]`).

**Check the research.**
- Save each researcher's file blocks as soon as it finishes (see "Saving agent output"). Confirm all four files exist. If the researchers report that web search or fetch was unavailable, record that in the log.
- If **neither** researcher found any verified evidence for the research questions, stop here and report to the user what was blocked and how to unblock it (for example, put the source documents in `00-brief/`). Don't continue to build files from no evidence.
- If only **one** researcher found verified evidence, skip the debate (1c), record which one came back empty and why in the log, and tell the analyst there is only one report to work from. Carry this to the validation report as a limitation.

**1c. Debate round.** Subagents can't message each other, so you run the debate in turns. Launch both calls together in one message, so neither sees the other's rebuttal:
- `researcher` in debate mode: give it `independent-research.md` and `independent-sources.md` to rebut. Returns `01-research/debate/primary-rebuttal.md`.
- `independent-researcher` in debate mode: give it `research-notes.md` and `sources.md` to rebut. Returns `01-research/debate/independent-rebuttal.md` and the full updated `independent-research.md` (save it over the first version).
- One round only. Check each rebuttal cites only IDs that exist in the two sources files; if not, send it back once.

## 2. Judge and Analyse → `analyst`
Pass both research reports, both sources files and both rebuttals. The analyst judges the debate on argument, points, references, content and formatting, picks the stronger report on evidence, then writes the analysis on top of it. Confirm `02-analysis/debate-verdict.md` (winner, scorecard, challenge rulings, strong points from the losing report) and `analysis.md` were returned and saved. Log the winner and the weighted totals.

If the analyst asks for more research on a specific gap, you may run the `researcher` (or the `independent-researcher`, if the gap is about counter-evidence) once more for that gap, then re-run the analyst. Only once. Don't re-run the debate.

## 3. Write → `writer`
Output: `03-drafts/draft.md` (+ slides outline / tables if needed).

## 4–5. Review and Improve (at most two revision cycles)
- Run `reviewer` on `03-drafts/draft.md` → `04-reviews/review-1.md`.
- If the verdict is **REVISE**: run `improver` with review-1 → `05-revised/revised-1.md`; then `reviewer` on revised-1 → `review-2.md`.
- If review-2 is still **REVISE**: run `improver` → `revised-2.md`; then `reviewer` → `review-3.md`.
- Stop after that. Any blocker or major finding still open in the last review is an **unresolved issue**: record it in the log and carry it to the final report. Continue to Format with the latest version.
- Check each review is actionable (every finding has location, problem, evidence, fix). If not, send it back to the reviewer once with that instruction.

## 6. Format → `formatter`
Tell it which file is the latest approved version (draft.md, revised-1.md or revised-2.md, plus companion files). Confirm `06-formatted/` now contains real files (`report.md`, and `slides.md` / `tables/*.csv` if required). If `format-notes.md` lists factual problems, add them to the unresolved issues.

## 7. Build Materials → `builder`
Pass the list of "Files to deliver" from the spec. Confirm the builder ran `tools/check_deliverables.py`.

## 8. Final validation (do this yourself, don't delegate)
1. Run `python3 tools/check_deliverables.py projects/$ARGUMENTS --dump` with Bash.
2. For each required file: it exists and passed the check; and its content meets the spec (required sections/slides/sheets present, length/slide limits, audience, citation style, references included). Compare the dumped text against the spec — don't assume.
3. Spot-check three important numbers or claims in the final files against `01-research/research-notes.md` or `independent-research.md` (whichever the citation points to).
4. Write `projects/$ARGUMENTS/validation-report.md`:
   - **Deliverables**: table of file | status (PASS / FAIL / NOT BUILT / NOT VERIFIED) | what was checked
   - **Brief requirements**: each success criterion | met / partly met / not met | evidence
   - **Unresolved review issues** (from the last review)
   - **Evidence gaps** (every `[EVIDENCE GAP]` marker and research gap, from both research reports)
   - **Debate result**: which report won and its weighted score, plus any strong points from the losing report that were not carried into the deliverable
   - **Failed or skipped checks** and why
   - **Tools/capabilities that were unavailable** (e.g. web search, a library)

## 9. Report to the user
Reply with a short summary: the files in `07-deliverables/`, overall status, and — prominently — anything failed, unresolved, missing or unverified. Never describe a check as passed unless you ran it and saw it pass.
