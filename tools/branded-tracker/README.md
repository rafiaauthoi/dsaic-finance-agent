# Branded Finance Tracker

Builds a finance tracker workbook (.xlsx) in a club's own colors and logo. It's an add-on that comes with the Finance Agent, maintained by the project lead. **Team members: please don't edit these files.** Open an issue if something looks wrong.

## What the workbook includes

| Tab | What it does |
|---|---|
| Dashboard | Approved, spent, and remaining money by funding source, how much of each cap is used, and anything that needs attention |
| How to Use | One-page guide for the club's finance officer |
| Settings | Caps, semester end dates, and member names |
| Funding | One row per item on a funding letter; the expiration date fills itself in |
| Purchases | One row per receipt, linked to the funding item |
| WSAAC Tracker | WSAAC's official RSO Budget Tracker layout, filled in automatically |
| Inventory | What the club owns, who has it, and when it was last checked |

WSA rules built in: the $6,500 yearly cap, the $1,500 collaboration cap, the $500 start-up cap, and when each budget type's money expires. Sources are in [docs/wsa-guidelines](../../docs/wsa-guidelines).

## Adding a club

1. Make a folder `orgs/<club>/` with the club's logo as `logo.png`.
2. Add `orgs/<club>/brand.yaml`:

```yaml
name: Data Science & AI Club
short_name: DSAIC
logo: logo.png
colors:
  primary: "25197A"
  accent: "7346C2"
  on_primary: "FFFFFF"
  on_accent: "FFFFFF"
font: null
members: []
```

`primary` is used for headers and titles, and `accent` for highlights. `on_primary` and `on_accent` are the text colors that sit on top of them. `font: null` uses Arial. Leave `members` empty here, since names don't belong in a public repo. The club adds them in the Settings tab.

## Building a tracker

```powershell
pip install -r tools/branded-tracker/requirements.txt
python tools/branded-tracker/build_tracker.py orgs/dsaic --out outputs/DSAIC_Finance_Tracker_2026-27.xlsx
```

Optional flags: `--fiscal-year 2026-27`, `--fall-end 2026-12-19`, `--spring-end 2027-05-01`. Defaults come from WMU's 2026-27 academic calendar.

Generated workbooks are never committed (`.xlsx` files are in `.gitignore`). A filled-in tracker holds members' names and receipts, so it lives only in the club's private drive.
