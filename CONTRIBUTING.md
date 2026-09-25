# Contributing to DSAIC Finance Agent

Thanks for helping build this. You don't need to be a programmer to contribute. Organizing data, writing test cases, and improving docs matter just as much as code.

## Getting set up

1. Make a [GitHub account](https://github.com/signup) and send your username to the project lead.
2. Install [VS Code](https://code.visualstudio.com/) and [Git](https://git-scm.com/downloads).
3. Accept the collaborator invite from your email or GitHub notifications.
4. Clone the repo:

```
git clone https://github.com/rafiaauthoi/dsaic-finance-agent.git
```

## How work gets done

Every change follows the same path:

1. **Pick an issue** from the project board and assign yourself.
2. **Make a branch** from the latest `main`.
3. **Do the work** and commit as you go.
4. **Open a pull request** and fill out the template.
5. **Get a review** from at least one teammate.
6. **Squash and merge** once it's approved.

Nobody pushes directly to `main`, including the project lead. The branch rules enforce this.

## Branch names

Name branches by type and task, using lowercase and hyphens:

| Prefix | Use it for | Example |
|---|---|---|
| `data/` | Collecting, cleaning, or anonymizing data | `data/event-budget-samples` |
| `eval/` | Test cases and accuracy checks | `eval/conference-rule-checks` |
| `docs/` | README, guides, WSA guidelines | `docs/wsa-event-rules` |
| `feature/` | New agent functionality | `feature/draft-event-request` |
| `fix/` | Fixing something broken | `fix/date-format-parsing` |

## Commit messages

Write them as short commands describing what the commit does:

- Good: `Add anonymized event budget samples`
- Good: `Fix date parsing for fall 2024 requests`
- Not helpful: `stuff`, `updates`, `final version`

## Data rules

These are not optional:

- **Real funding requests, receipts, and generated drafts never go in this repo.** They live in the team's shared drive and get copied into your local `data/raw/` folder, which Git ignores.
- **Sample data must be anonymized.** Replace names, emails, student IDs, account numbers, and signatures with fake values.
- **Passwords and API keys go in a `.env` file**, never in code.
- **If you think something sensitive was committed, tell the project lead right away.** Fixing it fast matters more than whose fault it was.

## Reviewing pull requests

When you review someone's PR:

- Comment on the work, not the person.
- Ask questions instead of making demands ("What happens if the date is blank?").
- Approve once it works and follows the data rules. It doesn't have to be perfect.

## Getting help

Stuck for more than a day? Comment on your issue and tag the project lead, or ask in the team channel. Asking early saves everyone time.