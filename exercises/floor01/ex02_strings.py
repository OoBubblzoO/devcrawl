"""
FLOOR 1 · EXERCISE 1-2 — Strings & f-strings
Lesson: 1.2

Every roguelike is a machine that prints strings. HUD lines, damage popups,
death screens — all strings. f-strings are how Python builds them cleanly.

Run:  python3 dojo.py check 1-2
Save: python3 dojo.py done 1-2
"""

player_name = "Crumb"
player_hp = 24
player_max_hp = 30
depth = 2

# --- Part 1: f-string HUD ----------------------------------------------------
# Build EXACTLY this string using an f-string and the variables above
# (don't type the numbers by hand — the HUD must update when the vars do):
#
#   Crumb | HP 24/30 | Floor 2
#
# TODO:
hud_line = ...

# --- Part 2: methods ---------------------------------------------------------
# The dungeon announcer SHOUTS. Take the quiet message below and produce
# the loud version using a string method (hint: .upper()).

quiet = "a wild rat approaches"
# TODO:
loud = ...

# --- Part 3: spot the trap ---------------------------------------------------
# Someone tried to build a damage popup by adding a number to a string and
# the game crashed (TypeError: can only concatenate str to str).
# Fix it with an f-string instead of the broken + version.

damage = 7
# broken:  popup = "You take " + damage + " damage!"
# TODO — same text, but working:
popup = ...
