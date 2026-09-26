# Getting Started: Your First Contribution

This guide takes you from zero to your first change in the project. No coding experience needed. It takes about 30 to 45 minutes the first time. After that, the same steps take about 5 minutes.

If you get stuck at any step, stop and ask in the team channel or at the Friday meeting. Getting stuck on setup is normal and not your fault.

---

## Part 1: Accept your invites

You should have received two invites from rafiaauthoi.

1. Go to [github.com/notifications](https://github.com/notifications), or check the email tied to your GitHub account.
2. Open the invite to **dsaic-finance-agent** and click **Accept invitation**.
3. Open the invite to the **DSAIC Finance Agent** project board and accept it too.

Invites expire after 7 days. If yours expired, ask the project lead to send a new one.

---

## Part 2: Install the tools

You need two free programs. Skip any you already have.

**Visual Studio Code (VS Code)**, the editor we all use:
1. Go to [code.visualstudio.com](https://code.visualstudio.com/) and click the big download button.
2. Open the downloaded file and click through the installer. The default options are fine.

**Git**, the program that tracks changes:
- **Windows:** go to [git-scm.com/downloads](https://git-scm.com/downloads), click **Windows**, download the installer, and click **Next** on every screen. The defaults are fine.
- **Mac:** open the **Terminal** app, type `git --version`, and press Enter. If a popup asks to install developer tools, click **Install**. If it prints a version number, you already have Git.

After installing both, **restart your computer** (or at least close and reopen VS Code).

---

## Part 3: Tell Git who you are (one time only)

Git labels every change you make with your name and email.

1. Open VS Code.
2. Open the terminal: in the top menu, click **Terminal**, then **New Terminal**. A panel opens at the bottom of the window.
3. Copy and paste this line, replace the name with yours, and press Enter:

```
git config --global user.name "Your Name"
```

4. Copy and paste this line, replace the email with the one on your GitHub account, and press Enter:

```
git config --global user.email "you@example.com"
```

Nothing will appear to happen. That's normal, and it means it worked.

---

## Part 4: Download the project to your computer

This is called **cloning**. You only do it once.

1. In VS Code, press `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (Mac). A search bar opens at the top.
2. Type `Git: Clone` and press Enter.
3. Choose **Clone from GitHub**.
4. If VS Code asks to sign in to GitHub, click **Allow**, sign in through the browser window that opens, and approve it.
5. Type `dsaic-finance-agent`, then select **rafiaauthoi/dsaic-finance-agent** from the list.
6. Pick a folder to save it in (Documents is fine) and click **Select as Repository Destination**.
7. When VS Code asks "Would you like to open the cloned repository?", click **Open**.

You should now see the project files on the left side: `data`, `docs`, `README.md`, and more.

---

## Part 5: Your first contribution: add yourself to the team list

You'll make a small change and send it in the same way every real task works. Here's the path:

**make a branch, then edit, then save a checkpoint (commit), then upload (push), then ask for review (pull request), then merge**

### Step 1: Make your own branch

A branch is your own safe copy of the project. Nothing you do on it affects anyone else until it's reviewed.

1. Look at the **bottom-left corner** of VS Code. You'll see the word `main`.
2. Click `main`. A menu opens at the top.
3. Click **+ Create new branch...**
4. Type `docs/add-yourname` (for example, `docs/add-jordan`), all lowercase with no spaces, and press Enter.

The bottom-left corner should now show your branch name instead of `main`.

### Step 2: Make your change

1. On the left, open the `docs` folder and click `team.md`.
2. Click at the end of the last line and press Enter to start a new line.
3. Add a row in the same format as the one above it, with your details:

```
| Your Name | [@yourusername](https://github.com/yourusername) | Your Role |
```

4. Save the file: `Ctrl+S` (Windows) or `Cmd+S` (Mac).

If you don't have a role yet, write `Team Member`.

### Step 3: Save a checkpoint (commit)

1. On the far left edge of VS Code, click the **Source Control** icon. It looks like three dots connected by lines, and it shows a small number badge.
2. Under **Changes**, you'll see `team.md`. Hover over it and click the **+** that appears. This picks the change to include.
3. In the **Message** box above, type a short description, like `Add Jordan to team list`.
4. Click the **Commit** button.

If VS Code asks "There are no staged changes. Would you like to stage all?", click **Yes**.

### Step 4: Upload your branch (push)

1. In the same Source Control panel, click **Publish Branch**.
2. If it asks whether to publish to a public repository, choose the `origin` option (rafiaauthoi/dsaic-finance-agent).

Your branch is now on GitHub.

### Step 5: Ask for a review (pull request)

1. Go to [github.com/rafiaauthoi/dsaic-finance-agent](https://github.com/rafiaauthoi/dsaic-finance-agent).
2. A yellow banner near the top says your branch had recent pushes. Click **Compare & pull request**.
   - No banner? Click the **Pull requests** tab, then **New pull request**. Leave the left box as `main`, set the right box to your branch, and click **Create pull request**.
3. The title is filled in from your commit message. Leave it.
4. The description box already has a template. Fill it in:
   - **What changed:** `Added myself to the team list.`
   - **Why:** `Practice run of the contribution workflow.`
   - **Closes #:** delete this line.
   - **Checklist:** click each box that applies.
5. Click **Create pull request**.

### Step 6: Wait for review

A teammate or the project lead will review it. You'll get a notification when they respond.

- **If they approve it,** they'll merge it. You'll see a purple **Merged** badge. You're done.
- **If they ask for changes,** make the fix in VS Code on the same branch, then repeat Steps 3 and 4. For Step 4, the button will say **Sync Changes** instead of Publish. Your pull request updates automatically.

### Step 7: Get back in sync

After your pull request is merged:

1. In VS Code, click your branch name in the bottom-left corner and choose `main`.
2. Click the **circular arrows** next to `main` in the bottom-left corner (or the **Sync Changes** button in Source Control). This downloads everyone's latest changes.

Open `docs/team.md`, and your name should be there. **You've made your first contribution.**

---

## Part 6: For every real task after this

It's the same path every time:

1. Pick a task from the **Ready** column on the [project board](https://github.com/users/rafiaauthoi/projects/1) and assign yourself.
2. In VS Code, switch to `main` and sync (Part 5, Step 7).
3. Create a new branch named for the task (see the branch names in [CONTRIBUTING.md](../CONTRIBUTING.md)).
4. Do the work, then commit, then push, then open a pull request. This time, in the **Closes #** line, type the issue number, like `Closes #7`.
5. After it's merged, switch back to `main` and sync.

**Never put real funding documents, names, or account numbers in the project.** Real documents live in the team's private shared drive, never on GitHub.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `git` is not recognized | Git isn't installed, or VS Code needs a restart. Reinstall Git (Part 2) and reopen VS Code. |
| I can't find the repository when cloning | Accept your invite first (Part 1), then try again. |
| "Permission denied" or "403" when pushing | Your invite wasn't accepted, or VS Code is signed in to the wrong GitHub account. |
| I made changes on `main` by accident | Don't commit. Click `main` in the bottom-left corner, create a new branch, and your changes come with you. |
| My pull request says "Review required" | That's normal. Everyone's changes need one approval before merging. |
| Something else | Ask in the team channel. Screenshot what you see, and someone will help. |