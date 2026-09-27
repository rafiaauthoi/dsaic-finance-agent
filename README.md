# DSAIC Finance Agent

An AI agent that drafts Western Student Association (WSA) funding requests for student organizations at Western Michigan University, so finance directors spend their time reviewing documents instead of building them from scratch.

Built by the [Data Science & AI Club (DSAIC)](https://www.linkedin.com/company/data-science-club-wmu) at WMU.

> **Status:** Early development. We're building the data foundation from past approved funding requests and WSA's current rules.

## The problem

Student organizations at WMU request funding from WSA, the student government. Every request has to follow WSA's rules, and operational, event, conference, and collaboration budgets each come with their own criteria. Since September 2026, every request also needs proof the club has sought outside funding.

For a finance director, that means hours of administrative data entry, repeated for every event the organization wants funded. And when officers graduate, their knowledge of what gets approved leaves with them.

## What the agent does

1. **Learns from what's worked before.** It studies previously approved funding requests and WSA's criteria for each budget type.
2. **Takes in what the org needs.** The event or purpose, the items, the costs, and why they're needed.
3. **Drafts the request.** It fills out WSA's official template following the rules for the right budget type.
4. **Flags problems early.** Anything that breaks a WSA rule, or matches a common reason proposals get rejected, is highlighted before submission.
5. **A human makes the final call.** The finance director reviews, edits, and submits. The agent never submits anything on its own.

## Roadmap

- [ ] **Phase 1: Data foundation.** Collect and anonymize past approved requests; document WSA rules for each budget type
- [ ] **Phase 2: Tasks and design.** Decide exactly what to automate and choose the tech stack
- [ ] **Phase 3: First drafts.** Generate event budget requests
- [ ] **Phase 4: Full coverage.** Support operational, conference, and collaboration budgets, plus rule checking
- [ ] **Phase 5: Deploy and track.** Per-organization setup, deployment on DSAIC's own AI inference server, then purchase tracking

## How it's built

- **Python** for the agent and data processing
- **Per-organization settings** so each club gets an experience fitted to how it works

## Repository structure

```
data/
  raw/              real documents (never committed)
  processed/        cleaned real data (never committed)
  sample/           anonymized example data
docs/
  wsa-guidelines/   WSA funding rules, checked against the current bylaws
orgs/               per-organization settings
src/finance_agent/  agent code
tests/
```

## Data privacy

Real funding requests, receipts, and generated drafts never go in this repository. The `.gitignore` blocks documents and spreadsheets outside the sample folder, and all example data is anonymized. WSA's bylaws and slides are cited by section, never copied in.

## Getting started

New to the project? Start with [docs/getting-started.md](docs/getting-started.md), then read [CONTRIBUTING.md](CONTRIBUTING.md).

## Team

Project lead: Rafia Authoi ([@rafiaauthoi](https://github.com/rafiaauthoi))

Built with members of the Data Science & AI Club at Western Michigan University. See [docs/team.md](docs/team.md).