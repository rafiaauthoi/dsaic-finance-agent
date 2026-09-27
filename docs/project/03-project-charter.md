<img src="images/dsaic-logo.png" width="110" alt="Data Science and AI Club at WMU logo">

# DSAIC Finance Agent: Project Charter

**Document 3 of 3.** Roles, expectations, deliverables, and how we'll run the project.

| | |
|---|---|
| **Project**          | DSAIC Finance Agent                                            |
| **Project lead**     | Rafia Authoi                                                   |
| **Sponsor**          | Data Science & AI Club (DSAIC) E-Board                         |
| **Team size**        | 4 to 5 members, including the project lead                     |
| **Methodology**      | Agile (sprint-based), tracked on a public GitHub project board |
| **Version / status** | 2.1 \| Draft for team review                                   |

## 1. Project Overview

### 1.1 Purpose

Student organizations at WMU request funding from the Western Student Association (WSA) through budget requests that must follow WSA's rules, with separate criteria for operational, event, conference, and collaboration budgets. Finance directors build these requests by hand, one at a time, and the knowledge of what gets approved is lost every year. This project builds an AI agent that drafts WSA funding requests from previously approved examples, checks them against WSA's rules, and hands them to a finance director for review before submission.

### 1.2 Vision statement

> *Any club finance director can describe what their organization needs and receive a complete, rule-checked WSA funding request ready for their review, built on what WSA has approved before, with their data kept private to their organization.*

### 1.3 Project details

|                             |                                                                                                  |
|-----------------------------|--------------------------------------------------------------------------------------------------|
| **Start date**              | TBD (see project board)                                                                          |
| **Target completion**       | TBD (see project board)                                                                          |
| **First procedure**         | WSA funding requests: operational, event, conference, and collaboration budgets                  |
| **Next procedure**          | Purchase tracking: recording what each organization bought with approved funds                   |
| **Development environment** | Team members' laptops, using anonymized sample data only                                         |
| **Production environment**  | Container on DSAIC's AI Inference Server                                                         |
| **Key dependency**          | AI Inference Server project (needed for Phase 5)                                                 |
| **Repository**              | [github.com/rafiaauthoi/dsaic-finance-agent](https://github.com/rafiaauthoi/dsaic-finance-agent) |
| **Project board**           | [DSAIC Finance Agent board](https://github.com/users/rafiaauthoi/projects/1)                     |
| **Meetings**                | Fridays, 6:30 PM, at the Student Center or online                                                |

## 2. Objectives and Success Measures

Each objective has a way to measure it, so we can tell when we're actually done. Target values will be confirmed with the team once Phase 1 shows us what the data looks like.

| **ID** | **Objective**                                               | **How we'll measure it**                                           | **Target**  |
|--------|-------------------------------------------------------------|--------------------------------------------------------------------|-------------|
| **O1** | Build a library of past approved WSA requests               | Approved requests collected, anonymized, and tagged by budget type | TBD         |
| **O2** | Document WSA's rules in a form both people and code can use | Rules written up for all four budget types, with sources           | All 4 types |
| **O3** | Generate complete draft requests                            | Share of drafts a finance director accepts with only minor edits   | TBD         |
| **O4** | Catch rule problems before submission                       | Share of known rule violations the checker flags on a test set     | TBD         |
| **O5** | Save finance directors real time                            | Time to prepare a request, before vs. after, reported by directors | TBD         |
| **O6** | Run privately for multiple organizations                    | Agent runs on the club server, each org's data kept separate       | Deployed    |

## 3. Scope

Defining scope protects the team from scope creep, which is when a project keeps growing until nothing gets finished. If an idea isn't in scope, it goes on a "future ideas" list instead of into the current work.

| **In scope**                                                                                                 | **Out of scope (for now)**                                   |
|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| Collecting and anonymizing past approved WSA requests                                                        | Submitting requests to WSA on anyone's behalf                |
| Documenting WSA rules for operational, event, conference, and collaboration budgets                          | Guaranteeing WSA approval                                    |
| Drafting WSA funding requests from a director's description, including the required proof of outside funding | Funding sources other than WSA                               |
| Automatically checking drafts against WSA rules                                                              | Moving money, making purchases, or approving expenses        |
| A review step where a finance director edits and approves                                                    | Replacing official WSA or university records                 |
| Per-organization setup with data kept separate                                                               | Purchase tracking (planned as the next procedure)            |
| Deployment to DSAIC's AI Inference Server                                                                    | Building or maintaining the server itself (separate project) |

## 4. Work Breakdown Structure

A Work Breakdown Structure (WBS) splits the project into smaller, manageable pieces. Each numbered box becomes one or more issues on the project board. The order follows the plan agreed with the club president: collect the data, identify the tasks to automate, then choose the tech stack and design from what we learn.

![Figure 1. Work Breakdown Structure](images/charter-work-breakdown-structure.png)

*Figure 1. Work Breakdown Structure*

## 5. Team and Roles

The team is 4 to 5 people. Each person has one primary role, but everyone helps where needed. If the team has 4 members, the Docs & Comms responsibilities are shared between the project lead and the Rules & QA Analyst. Roles are assigned at the first meeting.

![Figure 2. Project team structure](images/charter-project-team-structure.png)

*Figure 2. Project team structure*

### 5.1 Role descriptions

#### Project Lead

|   |   |
|---|---|
| **Good fit if you...** | Assigned to Rafia Authoi. |
| **Responsibilities** | Sets priorities, runs meetings, and keeps the project board current<br>Unblocks teammates and makes final decisions on scope and design<br>Reviews and approves pull requests; controls access to real funding documents<br>Coordinates with the DSAIC E-Board, WSA contacts, and the AI Inference Server team |
| **Deliverables** | Project board and sprint plans<br>Tech stack decision record (Phase 2)<br>Status updates to the E-Board |

#### Data Steward

|   |   |
|---|---|
| **Good fit if you...** | You like spreadsheets, organizing things, and noticing details. No coding required. |
| **Responsibilities** | Collects past approved WSA requests from the shared drive and tracks what's missing<br>Standardizes line items, categories, dates, and amounts using the clean-data rules<br>Anonymizes requests so samples can safely go in the public repository<br>Maps every field on the WSA request form and what goes in it |
| **Deliverables** | Tracking sheet of all collected requests<br>Anonymized sample requests for each budget type<br>Form field map (docs/wsa-guidelines/form-fields.md) |

#### Rules & QA Analyst

|   |   |
|---|---|
| **Good fit if you...** | You like reading rules closely and asking "how do we know that's right?" No coding required. |
| **Responsibilities** | Writes up WSA's rules for all four budget types, with sources<br>Builds a test set: sample requests with known rule problems the checker should catch<br>Reviews the agent's drafts and records what it gets right and wrong<br>Gathers feedback from finance directors during the pilot |
| **Deliverables** | Rules docs for all four budget types<br>Test set of requests with known issues<br>Draft quality reports each sprint<br>Pilot feedback summary |

#### Agent Developer

|   |   |
|---|---|
| **Good fit if you...** | You want to write code, or you want to learn. Some Python helps but isn't required to start. |
| **Responsibilities** | Runs the Hermes Agent experiment and compares it with other options in Phase 2<br>Builds the drafting agent that turns a director's description into a request<br>Builds the rules checker that reads the rules file and flags problems<br>Works with the project lead to containerize and deploy to the AI server |
| **Deliverables** | Tech stack experiment write-up<br>Working draft generator<br>Rules checker with tests<br>Deployment container and setup notes |

#### Docs & Comms Lead

|   |   |
|---|---|
| **Good fit if you...** | You like writing, organizing, and keeping people in sync. No coding required. |
| **Responsibilities** | Takes notes at Friday meetings and posts action items<br>Keeps the README, contributing guide, and setup instructions accurate<br>Helps keep issues and the project board tidy and up to date<br>Prepares demo materials and recruiting posts for DSAIC's LinkedIn and Instagram |
| **Deliverables** | Meeting notes and action items<br>Up-to-date README and guides<br>Final demo and showcase materials |

### 5.2 Responsibility matrix (RACI)

A RACI matrix shows who does what. For each task: R is Responsible (does the work), A is Accountable (owns the outcome and signs off), C is Consulted (gives input), and I is Informed (kept updated).

| **Task**                                   | **Lead** | **Data** | **Rules/QA** | **Dev** | **Docs** |
|--------------------------------------------|----------|----------|--------------|---------|----------|
| **Set up shared drive for real documents** | R/A      | C        | I            | I       | I        |
| **Collect and anonymize past requests**    | A        | R        | C            | I       | I        |
| **Map WSA form fields**                    | A        | R        | C            | C       | I        |
| **Document WSA rules**                     | A        | C        | R            | C       | C        |
| **Choose tasks and tech stack**            | R/A      | C        | C            | R       | I        |
| **Hermes Agent experiment**                | A        | I        | C            | R       | I        |
| **Build draft generator**                  | A        | C        | C            | R       | I        |
| **Build rules checker**                    | A        | I        | C            | R       | I        |
| **Test drafts and run director pilot**     | A        | C        | R            | C       | I        |
| **Deploy to AI server**                    | A        | I        | C            | R       | I        |
| **README, guides, and showcase**           | A        | C        | C            | C       | R        |

## 6. Deliverables

**Deadlines:** all due dates are TBD and will be set during sprint planning. Always check the project board for current deadlines.

| **ID**  | **Deliverable**                 | **Owner**       | **Phase** | **Done when...**                                         | **Due** |
|---------|---------------------------------|-----------------|-----------|----------------------------------------------------------|---------|
| **D1**  | Team setup complete             | All             | 0         | Everyone can clone the repo and open a pull request      | TBD     |
| **D2**  | Shared drive for real documents | Project Lead    | 1         | Private folder exists, access limited to the team        | TBD     |
| **D3**  | Past request library            | Data Steward    | 1         | Approved requests collected and tracked by budget type   | TBD     |
| **D4**  | Form field map                  | Data Steward    | 1         | Every WSA form field documented                          | TBD     |
| **D5**  | WSA rules docs                  | Rules & QA      | 1         | Rules for all four budget types written up with sources  | TBD     |
| **D6**  | Anonymized samples              | Data Steward    | 1         | At least one per budget type, checked by a second person | TBD     |
| **D7**  | Tech stack decision             | Lead & Dev      | 2         | Options tested, choice and reasons written in the repo   | TBD     |
| **D8**  | Event request drafts            | Agent Developer | 3         | Agent drafts event requests that pass the rules checker  | TBD     |
| **D9**  | All budget types + pilot        | Dev & Rules/QA  | 4         | Finance directors approve drafts with minor edits        | TBD     |
| **D10** | Deployed agent                  | Agent Developer | 5         | Runs on the AI server, data separated by organization    | TBD     |
| **D11** | Documentation & showcase        | Docs & Comms    | 5         | A new member can set up the project from the docs alone  | TBD     |

## 7. Phases and Milestones

The project runs in six phases. Each phase ends at a milestone gate: a clear check that must be met before moving on. Within each phase, work happens in sprints. Purchase tracking begins after Phase 5 as the next procedure.

![Figure 3. Project phases and milestone gates (dates TBD)](images/charter-project-phases-and-milestone-gates.png)

*Figure 3. Project phases and milestone gates (dates TBD)*

| **Phase**                   | **Focus**                                                                        | **Milestone gate (exit criteria)**                             | **Target date** |
|-----------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------------|-----------------|
| **0. Kickoff & Onboarding** | Roles, laptop setup, first practice pull request                                 | Every member has merged one practice PR                        | TBD             |
| **1. Data Foundation**      | Collect past approved requests, map the form, document the rules                 | Request library, form map, and rules docs approved by the lead | TBD             |
| **2. Tasks & Design**       | Decide exactly what to automate; test Hermes Agent and alternatives              | Tech stack chosen and written up, with evidence                | TBD             |
| **3. First Drafts: Event**  | Draft generator and rules checker for event budgets                              | Event drafts pass the rules checker on the test set            | TBD             |
| **4. Full Coverage**        | Operational, conference, and collaboration budgets; pilot with finance directors | Directors approve drafts with only minor edits                 | TBD             |
| **5. Deploy & Handoff**     | Move to the AI server, per-org setup, finish docs                                | Runs on the server; docs verified by a new member              | TBD             |

## 8. Team Expectations

These are our working agreements. They exist so everyone knows what they can count on from each other.

### 8.1 Working agreements

- **Show up or give notice.** Attend the Friday meetings. If you can't make one, post your update in the team channel beforehand.

- **Keep the board honest.** If you're working on a task, its card shows it. If you're blocked, say so on the card.

- **Ask early.** Stuck for more than a day? Ask for help. Asking early is a strength, not a weakness.

- **Say it when you're overloaded.** Exams and busy weeks happen. Tell the lead as early as you can so work can be shifted.

- **Everything goes through a pull request.** No one pushes directly to main, including the project lead.

- **Problem before tools.** New tools are exciting, but every technical choice has to trace back to a real task from Phase 1 and 2.

- **Review kindly, receive openly.** Comment on the work, not the person. Assume good intent.

### 8.2 Privacy and confidentiality

> **Non-negotiable**
>
> - The repository is public. Real funding requests never go on GitHub, in group chats, or on personal cloud drives. They stay in the team's private shared drive.
>
> - Only anonymized samples go in the repository, and a second teammate checks each one before it's merged.
>
> - One organization's data is never used in, or visible from, another organization's drafts.
>
> - Passwords and API keys stay in .env files and are never committed.
>
> - Internal planning documents (like statements of work) stay within the team until finalized.
>
> - If you think data was exposed, tell the project lead immediately.

### 8.3 Definition of Done

A task is only "done" when all of the following are true:

|     | **Definition of Done**                                                  |
|-----|-------------------------------------------------------------------------|
| ☐   | The work is merged into main through an approved pull request           |
| ☐   | It was reviewed by at least one other team member                       |
| ☐   | It contains no real funding documents, personal information, or secrets |
| ☐   | Any related documentation (README, rules docs, form map) is updated     |
| ☐   | The issue is closed and the card is in the Done column                  |

## 9. Risk Management

A risk is something that could go wrong. Listing risks early means we can plan for them instead of being surprised. The heat map shows how likely each risk is and how much damage it would do; risks in the darker upper-right cells get the most attention.

![Figure 4. Risk heat map](images/charter-risk-heat-map.png)

*Figure 4. Risk heat map*

| **ID** | **Risk**                                   | **Likelihood** | **Impact** | **Response plan**                                                                                | **Owner**       |
|--------|--------------------------------------------|----------------|------------|--------------------------------------------------------------------------------------------------|-----------------|
| **R1** | Past requests are incomplete or messy      | High           | High       | Track what's missing instead of guessing; start with the budget type that has the most examples  | Data Steward    |
| **R2** | Personal data exposed or mixed across orgs | Low            | High       | Real data only in the private drive; second-person check on every sample; separate setup per org | Project Lead    |
| **R3** | A draft breaks a WSA rule unnoticed        | Medium         | High       | Rules enforced by code, not just the AI; test set with known problems; director always reviews   | Rules & QA      |
| **R4** | Team members get busy mid-semester         | High           | Medium     | Small tasks; early heads-up rule; documented work so others can pick it up                       | Project Lead    |
| **R5** | AI Inference Server isn't ready on time    | Medium         | Medium     | Keep the laptop version working; coordinate with the server team                                 | Project Lead    |
| **R6** | Picking tools before the problem is clear  | Medium         | Low        | Time-boxed Hermes experiment in Phase 2; stack decision written up with evidence                 | Agent Developer |

## 10. Communication Plan

| **What**                          | **Who**                  | **How often**              | **Where**                                                    |
|-----------------------------------|--------------------------|----------------------------|--------------------------------------------------------------|
| **Team meeting**                  | Whole team               | Weekly, Fridays at 6:30 PM | Student Center or online                                     |
| **Sprint review & reflection**    | Whole team               | End of each sprint         | Friday meeting                                               |
| **Quick questions and updates**   | Whole team               | Anytime                    | Microsoft Teams channel (email the project lead to be added) |
| **Task discussion**               | Task owner and reviewers | As needed                  | On the GitHub issue or pull request                          |
| **Status update to sponsor**      | Project Lead to E-Board  | TBD                        | E-Board meetings                                             |
| **Recruiting and showcase posts** | Docs & Comms Lead        | At milestones              | DSAIC LinkedIn and Instagram                                 |

## 11. Assumptions and Constraints

#### Assumptions

- Past approved WSA requests in the shared drive can be used by the team to build and test the agent.

- WSA's rules for each budget type are available in written form and change rarely during a semester.

- The AI Inference Server will be available to host the agent by Phase 5.

- Team members have a laptop that can run VS Code, Git, and Python.

#### Constraints

- Team members are students with changing schedules; timelines must allow for exams and breaks.

- The repository is public, so real financial data must stay out of it at every stage.

- The project uses free and open-source tools and existing club hardware.

## 12. Approval

By signing, team members confirm they've read this charter and agree to its working agreements and privacy rules.

| **Name**     | **Role**                | **Signature** | **Date** |
|--------------|-------------------------|---------------|----------|
| Rafia Authoi | Project Lead            |               |          |
|              | Data Steward            |               |          |
|              | Rules & QA Analyst      |               |          |
|              | Agent Developer         |               |          |
|              | Docs & Comms Lead       |               |          |
|              | Sponsor (DSAIC E-Board) |               |          |

---

**Project documents:** [1. Project Brief](01-project-brief.md) | [2. Refresher Guide](02-refresher-guide.md) | [3. Project Charter](03-project-charter.md)

Word versions of these documents are kept in the team's shared drive. Questions? Email the project lead, Rafia Authoi, at rafiahasan.authoi@wmich.edu.
