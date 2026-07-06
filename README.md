# DEVCRAWL

**Descend. Debug. Survive.** A self-hosted learning platform where the curriculum is a dungeon: 10 floors of Python, each floor's project building one organ of a final terminal roguelike. Lessons + quizzes run in the browser; exercises are real files verified by real pytest tests. Your GitHub repo is your save file.

## Setup (once)

```bash
pip install pytest        # the only dependency
```

Push this repo to GitHub, then turn on the site:
**Settings → Pages → Source: Deploy from a branch → `main` / `docs`**

Your dungeon is live at `https://<you>.github.io/<repo>/` — works on your phone too.

## The loop

1. Open the site, read the next lesson, pass its two checkpoints.
2. Open the matching exercise file in `exercises/` — fix the TODOs.
3. Verify and save:

```bash
python3 dojo.py next          # what's next
python3 dojo.py check 1-1     # run the tests (red = information)
python3 dojo.py done 1-1      # green → progress.json updated + committed
python3 dojo.py lesson 1.2    # record a browser lesson in the repo
python3 dojo.py push          # sync your save to GitHub
```

`done` refuses to save unless tests pass. No participation trophies in the dungeon.

## What's built vs. what's an outline

| | |
|---|---|
| **Floors 1–3** | Fully built: 12 lessons w/ quizzes, 9 exercises, 3 projects, 59 tests |
| **Floors 4–10** | Outlined in the app + `exercises/floorNN/README.md` stubs |
| **C++ / Swift / JS-TS / SQL tracks** | Outlined on the Tracks page |

## Expanding the dungeon

When you clear Floor 3, ask Claude (or Claude Code pointed at this repo):

> "Generate Floor 4 of DEVCRAWL following the Floor 1–3 format: lessons with
> quizzes added to the `PY_FLOORS` data in `docs/index.html`, rustlings-style
> exercise files + pytest tests in `exercises/floor04/`, and ids wired into
> `dojo.py`'s MANIFEST. Set the floor's status to 'ready'."

The Floor 1–3 files are the template — same structure, same voice, same test style. Tracks unlock the same way.

## Repo map

```
devcrawl/
├── dojo.py                 # progress keeper: check / done / status / push
├── docs/                   # GitHub Pages site
│   ├── index.html          # the whole app (single file, no build step)
│   └── progress.json       # YOUR SAVE FILE — committed by dojo.py
└── exercises/
    ├── floor01/  … floor03/   # exercise files + tests/ (built)
    └── floor04/  … floor10/   # README stubs (generate on arrival)
```
