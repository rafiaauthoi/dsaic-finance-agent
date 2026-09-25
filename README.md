# DSAIC Finance Agent

An AI agent that drafts Western Student Association (WSA) funding requests for student organizations at Western Michigan University, so finance directors spend their time reviewing documents instead of building them from scratch.

Built by the [Data Science & AI Club (DSAIC)](https://github.com/rafiaauthoi/dsaic-finance-agent) at WMU.

> **Status:** Early development. We're building the data foundation from past approved funding requests.

## The problem

Student organizations at WMU request funding from WSA, the student government. Every request has to follow WSA's rules, and operational, event, and conference budgets each come with their own criteria.

For a finance director, that means hours of administrative data entry, repeated for every event the organization wants funded. And when officers graduate, their knowledge of what gets approved leaves with them.

## What the agent does

1. **Learns from what's worked before.** It studies previously approved funding requests and WSA's criteria for each budget type.
2. **Takes in what the org needs.** The event or purpose, the items, the costs, and why they're needed.
3. **Drafts the request.** It fills out the request following the rules for the right budget type.
4. **Flags problems early.** Anything that might break a WSA rule gets highlighted before submission.
5. **A human makes the final call.** The finance director reviews, edits, and submits. The agent never submits anything on its own.

## Roadmap

- [ ] **Phase 1: Data foundation.** Collect and anonymize past approved requests; document WSA rules for each budget type
- [ ] **Phase 2: First drafts.** Generate event budget requests
- [ ] **Phase 3: Full coverage.** Support operational and conference budgets, plus rule checking
- [ ] **Phase 4: Purchase tracking.** Keep a record of what the organization bought with approved funds
- [ ] **Phase 5: Built for every org.** Per-organization setup, and deployment on DSAIC's own AI inference server

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
  wsa-guidelines/   WSA funding rules by budget type
orgs/               per-organization settings
src/finance_agent/  agent code
tests/
```

## Data privacy

Real funding requests, receipts, and generated drafts never go in this repository. The `.gitignore` blocks documents and spreadsheets outside the sample folder, and all example data is anonymized.

## Getting started

Setup instructions will be added with the first working prototype.

## Team

Project lead: Rafia Authoi ([@rafiaauthoi](https://github.com/rafiaauthoi))

Built with members of the Data Science & AI Club at Western Michigan University.