# CLAUDE.md — Research & Deliverables System

This folder is a reusable multi-agent system. It turns a project brief into researched, reviewed, formatted files (reports, slide decks, spreadsheets, PDFs).

> If Claude Code also loads the parent repository's `CLAUDE.md` (the subagent catalog's contributor guide), ignore its "Contributing a New Subagent" rules while working here. They apply to the catalog, not to this system.

## How it works

You (the main Claude Code session) are the **orchestrator**. Subagents cannot call other subagents in Claude Code, so coordination always happens here, in the main session. The pipeline is defined in `.claude/commands/deliver.md` and started with:

```
/deliver <project-name>
```

| Step | Agent (`.claude/agents/`) | Reads | Writes |
|------|---------------------------|-------|--------|
| 1 Research | `researcher` | `00-brief/` | `01-research/sources.md`, `research-notes.md` |
| 2 Analyse | `analyst` | brief, research | `02-analysis/analysis.md` |
| 3 Write | `writer` | brief, research, analysis | `03-drafts/draft.md` |
| 4 Review | `reviewer` | draft + everything above | `04-reviews/review-N.md` (PASS/REVISE + findings table) |
| 5 Improve | `improver` | latest draft + review | `05-revised/revised-N.md`, `changes-N.md` |
| 6 Format | `formatter` | approved draft, style guide | `06-formatted/report.md`, `slides.md`, `tables/*.csv` |
| 7 Build | `builder` | formatted content, spec | `07-deliverables/*` (real files) + `build/` scripts |
| 8 Validate | orchestrator | everything | `validation-report.md` |

Review → Improve repeats **at most twice**. Anything still open after that is reported as unresolved; the pipeline does not loop forever.

## Folder layout

```
research-system/
├── CLAUDE.md                 # this file
├── README.md                 # setup + how to use
├── .claude/agents/           # the 7 specialist agents
├── .claude/commands/deliver.md   # the orchestrator pipeline (/deliver)
├── templates/                # project brief, deliverable spec, style guide
├── tools/check_deliverables.py   # checks output files exist, open, have content
└── projects/<name>/          # one folder per job
    ├── 00-brief/  01-research/  02-analysis/  03-drafts/  04-reviews/
    ├── 05-revised/  06-formatted/  07-deliverables/
    ├── pipeline-log.md
    └── validation-report.md
```

## Honesty rules (apply to every step)

1. **Never invent** research findings, sources, quotes, statistics, URLs or citations. Every fact traces to a source ID in `01-research/sources.md`.
2. **Never claim a check passed** unless it was actually run and its output seen. Don't describe test results you didn't get.
3. **Disclose gaps.** Missing evidence stays visible as `[EVIDENCE GAP: ...]` and is listed in the validation report.
4. **Files, not descriptions.** Format and Build steps must write real files. If a file can't be built (missing library, no tool), say so; never create a placeholder file that pretends to be the deliverable.
5. **Report capabilities honestly.** If web search, web fetch, a Python library or a converter isn't available, record that in `pipeline-log.md` and the final summary.

## What's actually available

- **Agents and the /deliver command**: built into Claude Code; work as soon as this folder is opened in Claude Code.
- **Web research**: uses Claude Code's `WebSearch` and `WebFetch` tools. They may be disabled or need permission approval in your setup. Without them, research is limited to files placed in `00-brief/`.
- **File generation**: done by Python scripts that need `python-docx`, `python-pptx`, `openpyxl`, `reportlab` (and optionally `pypdf` for checking PDFs, `pandoc` or LibreOffice as fallbacks). See README for install steps. Nothing else (no external APIs or services) is used.

## Working conventions

- One project = one folder under `projects/`. Start a new one by copying `templates/` files into `projects/<name>/00-brief/` and filling them in.
- Don't edit earlier versions of a draft; each revision is a new file so the history is visible.
- Keep agent instructions short and specific. If you change the pipeline, update both `.claude/commands/deliver.md` and the table above.
