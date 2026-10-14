# Research & Deliverables System

A set of seven Claude Code agents plus one command that take a written brief and produce researched, reviewed, professionally formatted files: a Word report, a PDF, a PowerPoint deck and an Excel workbook.

```
Research → Analyse → Write → Review ⇄ Improve (max 2 rounds) → Format → Build Materials → Final validation
```

You type one command, `/deliver my-project`, and Claude runs every step, saves each step's work in its own folder, and finishes with a validation report that lists anything missing, failed or unverified.

## What's in this folder

| Path | What it is |
|------|------------|
| `.claude/agents/` | The seven specialist agents (researcher, analyst, writer, reviewer, improver, formatter, builder) |
| `.claude/commands/deliver.md` | The orchestrator: the step-by-step pipeline `/deliver` runs |
| `CLAUDE.md` | Rules every step follows (no invented sources, disclose gaps, real files only) |
| `templates/` | Project brief, deliverable spec and style guide to copy for each job |
| `tools/check_deliverables.py` | Checks that output files exist, open and contain content |
| `projects/` | One folder per job. `example-four-day-week/` is a complete test run |

## Setup (once)

You need [Claude Code](https://code.claude.com/docs) installed and signed in, and Python 3.

1. **Get the files.** Clone this repository, or download it as a ZIP from GitHub and unzip it.
2. **Install the libraries that create the files.** Open a terminal (Mac: *Terminal*; Windows: *PowerShell*) and run:
   ```bash
   python3 -m pip install python-docx python-pptx openpyxl reportlab pypdf
   ```
   On Windows, use `py -m pip install ...` if `python3` isn't found.
3. **Open the system in Claude Code.** In the terminal, go into this folder and start Claude:
   ```bash
   cd awesome-claude-code-subagents/research-system
   claude
   ```
   Type `/agents` to confirm the seven agents are listed.
4. **Web search.** Research uses Claude Code's built-in web search and web fetch. Claude asks permission the first time; choose "allow". If your account has web search turned off, the system still runs but only uses files you give it, and it says so in the report.

## Example workflow

1. **Create a project folder** (replace `my-project` with a short name, no spaces):
   ```bash
   mkdir -p projects/my-project/00-brief
   cp templates/*.md projects/my-project/00-brief/
   ```
   (Windows PowerShell: `mkdir projects\my-project\00-brief` then `copy templates\*.md projects\my-project\00-brief\`.)
2. **Fill in the brief.** Edit `project-brief.md` (what you want to know, and for whom) and `deliverable-spec.md` (which files, how long, which sections). Adjust `style-guide.md` if you need to. Put any source documents (PDFs, notes, data) in the same `00-brief/` folder.
3. **Run it.** In Claude Code, type:
   ```
   /deliver my-project
   ```
   Approve permission prompts as they appear (web search, writing files, running Python).
4. **Collect the results.**
   - `projects/my-project/07-deliverables/`: your finished files
   - `projects/my-project/validation-report.md`: what passed, what failed, what's still uncertain. **Read this first.**
   - The numbered folders `01`–`06`: each step's working files, so you can see how the result was reached

To see a finished run, open `projects/example-four-day-week/`.

## Reusing it on other projects

- **Another job here:** make a new folder under `projects/` (step 1 above). Each job stays separate.
- **Inside a different repository:** copy `.claude/agents/`, `.claude/commands/deliver.md`, `CLAUDE.md`, `templates/` and `tools/` into that repository's root, and create an empty `projects/` folder. Then run `/deliver` there.
- **Everywhere on your computer:** copy the agent files into `~/.claude/agents/` and `deliver.md` into `~/.claude/commands/`. You still need `templates/`, `tools/` and `projects/` in the folder you work in.

## Customising

- **Change house style:** edit `templates/style-guide.md` (all future projects) or the copy inside one project's `00-brief/`.
- **Change what an agent does:** edit its file in `.claude/agents/`. Each one is plain English instructions.
- **Change the order or the revision limit:** edit `.claude/commands/deliver.md` and update the table in `CLAUDE.md`.

## Limitations (be aware)

- **The orchestrator is your main Claude session, not an agent.** Claude Code doesn't let agents start other agents, so `/deliver` must be run from the main session.
- **Research quality depends on what Claude can reach.** Paywalled papers and sites that block automated access can't be read. They show up as "Not verified" in the research notes.
- **Files are built by Python scripts.** If a library from step 2 is missing, that file type isn't built and the validation report says so. No other services or APIs are used.
- **Validation checks structure and spot-checks facts.** It confirms files open, contain the required sections and match the research notes. It doesn't replace a human read-through before you send anything important.
- **Long jobs use a lot of usage.** A full run calls seven agents, with up to three reviews. Start with a short brief.
