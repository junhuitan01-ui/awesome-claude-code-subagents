# Research notes: example-four-day-week

Date: 2026-10-14. Status: BLOCKED. No findings could be verified because no source was opened.

## Research questions
1. What did major four-day week trials (UK 2022 pilot and similar elsewhere) find about productivity, revenue and staff wellbeing?
2. What problems or limitations did the trials report, including reliability of methods?
3. What practical conditions made trials succeed or fail?

## Findings
No verified findings. Every claim below would need a source opened in a later attempt.

- Q1 productivity, revenue, wellbeing: [EVIDENCE GAP: no source opened; WebFetch unavailable]
- Q2 limitations and method reliability: [EVIDENCE GAP: no source opened; WebFetch unavailable]
- Q3 success and failure conditions: [EVIDENCE GAP: no source opened; WebFetch unavailable]

### Unverified leads from search-result summaries (NOT evidence; do not put in the report)
These come from search-tool summaries, which are not primary text. They only tell the next attempt what to check.
- UK 2022 pilot: reported as about 61 companies and about 2,900 staff, June to December 2022, with 56 of 61 continuing. The summary itself said revenue figures differ between accounts (1.4% average rise for 23 firms supplying data versus a 35% year-on-year comparison). Must be checked against [L1].
- Nature Human Behaviour 2025 paper [L3]: reported as 2,896 employees at 141 organisations in six countries, 12 control companies, 6-month trial, self-reported wellbeing gains, volunteer participants, mostly small firms in English-speaking countries, pre-trial coaching. Must be checked against the paper.
- Iceland [L4]: reported as 2,500 workers, public sector, 35-36 hour week at same pay, trial dates differing between accounts (2014-2019, 2015-2019, 2017-2021). Must be checked against the report.

## Conflicting evidence
Nothing verified. Leads already show possible conflicts to resolve: UK revenue figures (1.4% vs 35%, different bases) and Iceland trial dates.

## Gaps and uncertainties
- [EVIDENCE GAP: all three research questions unanswered with verified sources.]
- [EVIDENCE GAP: no trial table data can be confirmed; the table below is a checklist only.]
- [EVIDENCE GAP: Ireland, Australia/NZ, Portugal, Spain, Japan, US/Canada trials: no leads found yet.]
- [EVIDENCE GAP: independent critique of method quality (self-selection, no control group, self-reported data) not located.]

## Table-ready list of trials (unverified; fields left blank where no evidence)
| Trial | Country | Year | Organisations | Key result | Source |
|---|---|---|---|---|---|
| UK four-day week pilot | UK | 2022 | [EVIDENCE GAP: not verified] | [EVIDENCE GAP] | none verified (lead L1) |
| Global 4 Day Week trials (Nature Human Behaviour analysis) | Six countries | [EVIDENCE GAP] | [EVIDENCE GAP] | [EVIDENCE GAP] | none verified (lead L3) |
| Iceland shorter working week trials | Iceland | [EVIDENCE GAP] | [EVIDENCE GAP] | [EVIDENCE GAP] | none verified (lead L4) |
| Ireland pilot | Ireland | [EVIDENCE GAP] | [EVIDENCE GAP] | [EVIDENCE GAP] | none |
| Australia / New Zealand | Australia / NZ | [EVIDENCE GAP] | [EVIDENCE GAP] | [EVIDENCE GAP] | none |
| Portugal pilot | Portugal | [EVIDENCE GAP] | [EVIDENCE GAP] | [EVIDENCE GAP] | none |
| Spain pilot | Spain | [EVIDENCE GAP] | [EVIDENCE GAP] | [EVIDENCE GAP] | none |
| Japan trial | Japan | [EVIDENCE GAP] | [EVIDENCE GAP] | [EVIDENCE GAP] | none |
| US / Canada trials | US / Canada | [EVIDENCE GAP] | [EVIDENCE GAP] | [EVIDENCE GAP] | none |

## Not verified
All of L1 to L5 in sources.md: each fetch attempt returned "proxy refused the connection". Also not opened: news pages on the UK pilot (deeside.com, research-live.com, nysscpa.org, relocatemagazine.com, employeebenefits.co.uk, personneltoday.com), Fox-affiliate stories on Iceland, and the Wikipedia-style or vendor pages in the results (4dayweek.io is likely vendor-affiliated and should be avoided).

## Method
- Tools available: WebSearch worked (3 queries: UK 2022 pilot; Iceland trials; Nature Human Behaviour 2025 paper). WebFetch did NOT work: 7 attempts across salford-repository.worktribe.com, nature.com (two URLs), alda.is, cam.ac.uk and ideas.repec.org all failed with "proxy refused the connection". No Bash tool was available to run the proxy status check in /root/.ccr/README.md, so the cause (likely an egress policy block) is undiagnosed. I did not try to bypass the proxy.
- Search summaries were treated as leads only, because the research rules bar citing unopened sources.
- No other searches were run, since further searching could not produce openable sources.
- No files were provided in 00-brief/.
- To unblock: allow WebFetch for the hosts above (or place the UK report, the Nature paper and the Iceland report PDFs in 00-brief/), then rerun this step.
