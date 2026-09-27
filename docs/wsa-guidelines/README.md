# WSA Guidelines

Reference material the Finance Agent is built on: how WSA allocations work, the rules for each funding category, and how the process runs in practice.

| File | What it is |
|---|---|
| [wsa-club-finance-domain.md](wsa-club-finance-domain.md) | The canonical reference, written for people. Every fact carries a source tag and a rule ID (for example `EVT-03`). |
| [wsa-club-finance-rules.yaml](wsa-club-finance-rules.yaml) | The same facts as structured data, for the agent's rules checker. Its `rules_index` is rebuilt from the markdown, so edit the markdown first. |

## Ground rules

- **The markdown file is the source of truth.** If you change a rule there, update the matching entry in the YAML in the same pull request.
- **Check the source tag before trusting a line.** `[Step N]`, `[Step 4 instr]` and `[Templates F26]` are current official guidance. `[Inferred]` and `[Unconfirmed]` lines are not rules.
- **Use role mailboxes, not personal contacts.** Officer and staff names change every year. Individual contacts live in the team's private shared drive.
- **Open questions are tracked by ID** (`OQ-01` to `OQ-17`, `BS-01` to `BS-10`). When one is answered, update it here and link the source.
- **Never add the bylaws PDF or WSA's slides to this folder.** WSAAC asks that the bylaws not be reproduced. Cite them by section, like `[Bylaws F26 §5.04(g)]`, and keep the files in the team's shared drive.

Official WSA materials: [wmuwsa.org/allocations](https://wmuwsa.org/allocations)
