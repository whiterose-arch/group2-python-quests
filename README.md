# group2-python-quests

Team learning-Python-by-coding project. This repo is the shared workspace for our 3-person group to complete the **Learn Python by Coding** quests, submit our work, and review two peer groups.

## 👥 Team

| Name | GitHub handle |
|---|---|
| _Member 1_ | @whiterose-arch |
| _Member 2_ | @ |
| _Member 3_ | @ |

## 📁 Structure

```
group2-python-quests/
├── quests/
│   ├── quest_01_first_spell.py
│   ├── quest_02_naming_ceremony.py
│   ├── ...
│   └── quest_30_reflective_scribe.py
└── README.md
```

All 30 quest files already exist as scaffolds with:
- A multi-line docstring header describing the **Level**, **Concept**, **Why it matters**, **Logical reasoning**, and **The Quest (task)** — copied straight from the quest sheet.
- An `Assigned to` / `Status` block to fill in and update as you work.
- A `# TODO` marker showing exactly where your solution code goes.

We only need to **attempt at least 4 tasks per level** (6 levels = 24 minimum), but anyone can pick up any quest — see the rules below.

## 🚦 Workflow — read this carefully, no exceptions

These rules exist so three people can work on the same repo at once without stepping on each other. Follow them exactly.

1. **One quest, one branch, one Pull Request — no exceptions.**
   A Pull Request must touch **exactly one file** in `quests/`. If a PR contains changes to more than one quest file — even a stray space or a single-quote fix in a second file — it will be **rejected** and you'll need to split it up.

2. **Every branch is created from `main`, and every branch is created from the GitHub website (not the command line).**
   Use the **"Create branch"** button on GitHub (from the `main` branch dropdown, or from the file view). This avoids accidental typos, avoids branching off someone else's in-progress branch, and lets everyone see in the branch list who's working on what — all from the UI, no local `git checkout -b` guesswork.

3. **Branch naming convention (mandatory):**
   ```
   <your-github-handle>/quest_XX_slug
   ```
   — your GitHub handle, a slash, then the quest filename **without** the `.py` extension. Example:
   ```
   yembot31013/quest_01_first_spell
   ```
   This tells everyone at a glance *who* is working on *which* quest, so nobody accidentally duplicates work.

4. **Only claim a quest you're starting right now.**
   Don't create a branch today for a quest you plan to start tomorrow. If you know you won't touch it until later, leave it unclaimed so someone else can pick it up. A branch that sits empty blocks others from knowing whether it's really taken.

5. **Never merge into `main` yourself.**
   Once your PR is ready, open it and wait. Nobody merges their own PR (or anyone else's) solo. We review PRs together as a group and merge them together once everyone's happy. `main` should never receive a direct push or a solo merge from any of us.

6. Update the `Assigned to` and `Status` lines in the file's docstring header as part of your PR, so the merged history shows who did it and when.

### Step by step

1. On GitHub, go to the `quests/` folder → pick an unclaimed quest file.
2. From the branch dropdown (make sure `main` is selected as the source), click **"Create branch"** and name it `<your-handle>/quest_XX_slug`.
3. Edit `quest_XX_slug.py` **only** — either directly on GitHub or by pulling just that branch locally.
4. Fill in the `Assigned to` line, tick the `Status` box, write your solution under `# TODO`, and add short `#` comments for anything non-obvious.
5. Test it locally before pushing: `python quest_XX_slug.py` (or `python3 ...`).
6. Commit with a clear message, e.g. `Complete Quest 01: Your First Spell`.
7. Open a Pull Request into `main`. Double-check the PR's "Files changed" tab shows **exactly one file**.
8. Wait for the group to review together — do not merge it yourself.

### Minimum requirement checklist

- [ ] Level 1 — at least 4 of Quests 1–5 completed
- [ ] Level 2 — at least 4 of Quests 6–10 completed
- [ ] Level 3 — at least 4 of Quests 11–15 completed
- [ ] Level 4 — at least 4 of Quests 16–20 completed
- [ ] Level 5 — all 4 of Quests 21–24 completed (Level 5 only has 4 quests)
- [ ] Level 6 — at least 4 of Quests 25–30 completed

## 🔍 Peer Review (Deliverable 2)

We've been assigned **two peer groups** to review. For each peer group:

1. Browse their `quests/` folder (or their open PRs).
2. For each attempted quest, check:
   - Does it run without errors? (`python quest_XX_slug.py`)
   - Does it actually solve what "The Quest" asks for?
   - Is the logic sound, even if the style differs from ours?
   - Are there comments explaining non-obvious code?
3. Leave feedback as GitHub **Issues** or **PR comments** on their repo — specific and constructive.
4. Note anything genuinely clever — peer review is a two-way learning tool, not just error-hunting.

## 🛠 Requirements

- Python 3 installed — verify with:
  ```bash
  python --version
  # or
  python3 --version
  ```
- A GitHub account with access to this repo.

## 🤝 Ground rules (recap)

- 1 quest file = 1 branch = 1 PR. Multi-file PRs get rejected.
- Branches only from GitHub's UI, always off `main`, named `<handle>/quest_XX_slug`.
- Only branch a quest you're starting immediately — don't reserve quests for later.
- Nobody merges to `main` alone — we review and merge together as a group.
