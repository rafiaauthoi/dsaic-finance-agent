# Anonymization Checklist

Use this checklist before any real funding document, or anything copied from one, leaves the private shared drive. That includes files going into `data/sample/` in this repo, which is public.

**Who does it:** one person anonymizes, a second person checks (usually the Systems & Security Lead). Nothing is committed until both have signed off on the issue.

**Golden rule:** if you are not sure whether something identifies a person or a club, remove it.

---

## Before you start

- [ ] Work on a **copy** of the file, never the original in the drive.
- [ ] Work on your own computer or in the private drive, not in a public place like a Teams channel or GitHub.
- [ ] Open the issue for this sample (for example #11) so you can record what you did.

## 1. People

Replace with placeholders like `Representative A`, `Student 1`, `Staff Member`.

- [ ] Names in the identity block (RSO Representative, Typed Signature)
- [ ] Contact emails and phone numbers
- [ ] Conference attendee lists: first names, last names, **WIN numbers**. Delete the whole list and replace it with a count, for example `12 attendees`.
- [ ] Names in the Optional Notes box
- [ ] Names of WSA or OSE staff on funding letters
- [ ] Speakers, performers, or contractors who are individual people (a business name like "Example Pizza Co." can stay; a person's name cannot)

## 2. The club

Replace with the club's Org Code from the private key file, for example `ORG-03`.

- [ ] Full RSO Name in the identity block
- [ ] RSO name in the file name (templates are named `..._Proposal_-_[Full RSO Name].xlsx`)
- [ ] RSO name in the header, notes, event name, or anywhere else in the text
- [ ] Event or conference names that would identify the club on their own. Generalize them, for example "Annual Hackathon" becomes "Student Tech Event".
- [ ] RSO meeting day, time, and room
- [ ] Logos or branding in images

## 3. Money and payment details

- [ ] Card numbers, including the last four digits on receipts
- [ ] Bank statement screenshots: remove entirely
- [ ] Home or mailing addresses on receipts or vendor quotes
- [ ] Order numbers, invoice numbers, or account numbers tied to a person

**Keep:** item names, vendor business names, costs, amounts requested, amounts approved, budget type, and the month and fiscal year. These are what the project actually learns from.

## 4. Dates and places

- [ ] Exact event dates: change to the same month, day 1 (for example `10/01/2025`), unless the exact date matters for a rule like the 10-business-day window. If it does, note that in the issue instead.
- [ ] Specific room numbers. A building name is fine if many clubs use it.

## 5. Hidden places people forget

- [ ] **File properties.** In Excel: File > Info > Check for Issues > Inspect Document > remove Document Properties and Personal Information. This removes the author name saved in the file.
- [ ] Comments and tracked changes
- [ ] Hidden rows, columns, and sheets
- [ ] Screenshots and vendor quotes pasted outside the template border
- [ ] Email threads or forwarding headers pasted into notes

## 6. Final check

- [ ] Search the file (Ctrl+F) for: the club's name, `@`, `wmich.edu`, `WIN`, and any person's first name you saw in the original. Nothing should come up.
- [ ] Rename the file to something neutral, for example `sample-event-request-01.xlsx`.
- [ ] Second person checks the file against this list and comments **"Anonymization checked"** on the issue.
- [ ] Only then: open a pull request adding the file to `data/sample/`.

---

## If something slips through

If identifying information ends up on GitHub, **do not try to fix it with a new commit**. The old version stays in the history. Tell the Project Lead and the Systems & Security Lead right away so they can remove it properly.
