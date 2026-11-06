# Keeping API keys safe

The agent will need API keys, for example to talk to the DSAIC AI server. A key works like a password: anyone who has it can use the service as us, and some services charge for every request. This repository is public, so a key that gets committed is exposed to the whole internet.

This guide covers where keys go, how to load them, what our checks catch, and what to do if a key leaks.

## The short version

1. Keys go in a file named `.env` on your own computer. Never in code, never in an issue, never in chat.
2. Load them in Python with `os.environ`.
3. If a key is ever committed, tell Rafia and Saad right away. Then the key gets replaced. Deleting the commit is not enough.

## Where keys go

The repository has a file called `.env.example`. It lists the names of the settings the agent needs, with fake placeholder values.

To set up your own copy:

1. Copy the file and name the copy `.env`:

   ```bash
   cp .env.example .env
   ```

2. Open `.env` and replace each placeholder with the real value. Ask Saad for the server address and your key.

3. That's it. Git already ignores `.env` (see `.gitignore`), so it stays on your computer.

Rules:

- **Never** put a real value in `.env.example`. That file is public.
- **Never** paste a key into code, a notebook, an issue, a pull request, a commit message, or the team chat. Send keys only in a private message, and only to the person who needs them.
- **Don't share your key with teammates.** Each person or project gets its own, so one can be turned off without breaking everyone else's.

## Loading keys in Python

Install the small helper that reads `.env` files:

```bash
pip install python-dotenv
```

Then, in your code:

```python
import os

from dotenv import load_dotenv

load_dotenv()  # reads .env in the project folder

LLM_URL = os.environ["FINANCE_AGENT_LLM_URL"]
LLM_KEY = os.environ["FINANCE_AGENT_LLM_KEY"]
LLM_MODEL = os.environ.get("FINANCE_AGENT_LLM_MODEL", "club-default")
```

`os.environ["NAME"]` stops with an error if the setting is missing, which is what you want: it tells you to fill in your `.env` instead of failing in a confusing way later.

Don't `print()` a key or write it to a log file. If you need to check that it loaded, print only the first few characters, like `LLM_KEY[:6]`.

## What our checks catch, and what they don't

| Check | What it catches | What it misses |
| --- | --- | --- |
| `.gitignore` | Keeps `.env` and `.env.*` files out of commits (except `.env.example`) | A key typed straight into code or another file |
| Data check (runs on every pull request) | Emails, 9-digit ID numbers, and phone numbers under `data/`; spreadsheets and PDFs outside the allowed folders | **API keys.** It does not look for keys at all |
| GitHub push protection | Many well-known key formats (for example OpenAI, AWS, Google), blocked before the push goes through | Keys in formats GitHub doesn't recognize, including keys from our own AI server |

So the checks are a safety net, not a guarantee. The real protection is keeping keys in `.env` and never anywhere else. Before every commit, look at what you're committing in VS Code's Source Control panel.

If GitHub blocks your push because it found a secret, **don't** use the option to bypass it. Remove the key from your code, move it to `.env`, and commit again. Then tell Saad, since the key may need replacing anyway.

## If a key is ever committed

This can happen to anyone. Fixing it fast matters more than whose fault it was.

1. **Tell Rafia and Saad right away,** even if you already deleted it. Say which key it was and where it appeared.
2. **The key gets rotated.** Saad turns off the leaked key and issues a new one. Put the new key in your `.env`.
3. **Then clean up** the commit or file with help from Rafia.

Why deleting the commit is not enough: Git keeps history, GitHub keeps copies of pushed commits, and automated bots scan public repositories for keys within minutes. Once a key has been pushed, assume someone else has it. Only replacing the key makes the old one useless.

## Questions

Ask Saad (Systems & Security Lead) or Rafia (Project Lead) in the team channel. See also [CONTRIBUTING.md](../CONTRIBUTING.md) and the [anonymization checklist](anonymization-checklist.md) for data rules.
