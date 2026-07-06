#!/usr/bin/env python3
"""
dojo.py — the DEVCRAWL progress keeper.

Your GitHub repo IS your save file. This tool runs the pytest suite for an
exercise, and if the tests pass, marks it complete in docs/progress.json and
commits. Push, and your progress follows you anywhere.

Usage:
    python3 dojo.py status              show your descent
    python3 dojo.py next                what to do next
    python3 dojo.py check 1-1           run tests for exercise 1-1 (no save)
    python3 dojo.py done 1-1            run tests; if green, save + commit
    python3 dojo.py lesson 1.2          mark a reading lesson complete + commit
    python3 dojo.py push                git push (sync your save)

Requires: Python 3.10+, pytest (pip install pytest), git.
"""

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROGRESS_FILE = ROOT / "docs" / "progress.json"

# exercise id -> (exercise file, test file)
MANIFEST = {
    "1-1": ("exercises/floor01/ex01_variables.py",  "exercises/floor01/tests/test_ex01_variables.py"),
    "1-2": ("exercises/floor01/ex02_strings.py",    "exercises/floor01/tests/test_ex02_strings.py"),
    "1-3": ("exercises/floor01/ex03_numbers.py",    "exercises/floor01/tests/test_ex03_numbers.py"),
    "1-P": ("exercises/floor01/project_character.py", "exercises/floor01/tests/test_project_character.py"),
    "2-1": ("exercises/floor02/ex01_booleans.py",   "exercises/floor02/tests/test_ex01_booleans.py"),
    "2-2": ("exercises/floor02/ex02_branching.py",  "exercises/floor02/tests/test_ex02_branching.py"),
    "2-3": ("exercises/floor02/ex03_loops.py",      "exercises/floor02/tests/test_ex03_loops.py"),
    "2-P": ("exercises/floor02/project_rat_fight.py", "exercises/floor02/tests/test_project_rat_fight.py"),
    "3-1": ("exercises/floor03/ex01_lists.py",      "exercises/floor03/tests/test_ex01_lists.py"),
    "3-2": ("exercises/floor03/ex02_dicts.py",      "exercises/floor03/tests/test_ex02_dicts.py"),
    "3-3": ("exercises/floor03/ex03_slices.py",     "exercises/floor03/tests/test_ex03_slices.py"),
    "3-P": ("exercises/floor03/project_loot.py",    "exercises/floor03/tests/test_project_loot.py"),
}

ORDER = list(MANIFEST.keys())

GREEN = "\033[92m"
RED = "\033[91m"
MAGENTA = "\033[95m"
AMBER = "\033[93m"
DIM = "\033[2m"
RESET = "\033[0m"


def load_progress() -> dict:
    if PROGRESS_FILE.exists():
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return {"lessons": [], "exercises": [], "updated": None}


def save_progress(progress: dict) -> None:
    progress["updated"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    PROGRESS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(PROGRESS_FILE, "w") as f:
        json.dump(progress, f, indent=2)
        f.write("\n")


def run_tests(ex_id: str) -> bool:
    if ex_id not in MANIFEST:
        print(f"{RED}Unknown exercise id: {ex_id}{RESET}")
        print(f"Known ids: {', '.join(ORDER)}")
        sys.exit(1)
    _, test_file = MANIFEST[ex_id]
    print(f"{DIM}Running {test_file}…{RESET}\n")
    result = subprocess.run(
        [sys.executable, "-m", "pytest", str(ROOT / test_file), "-v", "--no-header"],
        cwd=ROOT,
    )
    return result.returncode == 0


def git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)


def commit(message: str, extra_paths: list[str] | None = None) -> None:
    paths = ["docs/progress.json"] + (extra_paths or [])
    git("add", *paths)
    result = git("commit", "-m", message)
    if result.returncode == 0:
        print(f"{MAGENTA}Committed:{RESET} {message}")
        print(f"{DIM}Run `python3 dojo.py push` to sync your save.{RESET}")
    else:
        out = (result.stdout + result.stderr).strip()
        print(f"{DIM}Nothing new to commit ({out.splitlines()[-1] if out else 'no changes'}).{RESET}")


def cmd_status() -> None:
    progress = load_progress()
    done_ex = set(progress.get("exercises", []))
    done_ls = set(progress.get("lessons", []))
    print(f"\n{MAGENTA}═══ DEVCRAWL — your descent ═══{RESET}\n")
    print(f"Lessons cleared:   {len(done_ls)}")
    print(f"Exercises green:   {len(done_ex)}/{len(MANIFEST)} (floors 1–3 wired so far)\n")
    for ex_id in ORDER:
        mark = f"{GREEN}✔{RESET}" if ex_id in done_ex else f"{DIM}·{RESET}"
        label = "PROJECT" if ex_id.endswith("P") else "exercise"
        print(f"  {mark} {ex_id:<4} {DIM}{label:<9}{RESET} {MANIFEST[ex_id][0]}")
    print()


def cmd_next() -> None:
    progress = load_progress()
    done_ex = set(progress.get("exercises", []))
    for ex_id in ORDER:
        if ex_id not in done_ex:
            ex_file, _ = MANIFEST[ex_id]
            print(f"\nNext up: {AMBER}{ex_id}{RESET} → open {ex_file}")
            print(f"Then run: {DIM}python3 dojo.py done {ex_id}{RESET}\n")
            return
    print(f"\n{GREEN}Floors 1–3 fully cleared. Time to generate the next floors!{RESET}\n")


def cmd_check(ex_id: str) -> None:
    ok = run_tests(ex_id)
    print()
    if ok:
        print(f"{GREEN}Tests green.{RESET} Save it with: python3 dojo.py done {ex_id}")
    else:
        print(f"{RED}Tests failing — read the assertion messages, they tell you exactly what's wrong.{RESET}")


def cmd_done(ex_id: str) -> None:
    ok = run_tests(ex_id)
    print()
    if not ok:
        print(f"{RED}Not yet — tests must be green before progress saves. No participation trophies in the dungeon.{RESET}")
        sys.exit(1)
    progress = load_progress()
    if ex_id not in progress["exercises"]:
        progress["exercises"].append(ex_id)
        save_progress(progress)
    ex_file, _ = MANIFEST[ex_id]
    print(f"{GREEN}✔ {ex_id} cleared.{RESET}")
    commit(f"devcrawl: clear exercise {ex_id}", extra_paths=[ex_file])


def cmd_lesson(lesson_id: str) -> None:
    progress = load_progress()
    if lesson_id not in progress["lessons"]:
        progress["lessons"].append(lesson_id)
        save_progress(progress)
        print(f"{GREEN}✔ lesson {lesson_id} marked complete.{RESET}")
        commit(f"devcrawl: complete lesson {lesson_id}")
    else:
        print(f"{DIM}Lesson {lesson_id} was already complete.{RESET}")


def cmd_push() -> None:
    result = subprocess.run(["git", "push"], cwd=ROOT)
    if result.returncode == 0:
        print(f"{GREEN}Save synced. Your progress now lives on GitHub.{RESET}")


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return
    cmd, rest = args[0], args[1:]
    if cmd == "status":
        cmd_status()
    elif cmd == "next":
        cmd_next()
    elif cmd == "check" and rest:
        cmd_check(rest[0])
    elif cmd == "done" and rest:
        cmd_done(rest[0])
    elif cmd == "lesson" and rest:
        cmd_lesson(rest[0])
    elif cmd == "push":
        cmd_push()
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
