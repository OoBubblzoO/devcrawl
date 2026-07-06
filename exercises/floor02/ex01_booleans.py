"""
FLOOR 2 · EXERCISE 2-1 — Booleans & comparisons
Lesson: 2.1

Games are made of decisions, and decisions are made of booleans.
Comparisons (== != < > <= >=) produce True/False; and/or/not combine them.

Run:  python3 dojo.py check 2-1
Save: python3 dojo.py done 2-1
"""

player_hp = 7
player_max_hp = 30
has_key = True
door_locked = True
potions = 0
depth = 3
torch_lit = False

# --- Part 1: state checks ------------------------------------------------------
# is_hurt        -> True when hp is below max
# is_critical    -> True when hp is at or below 25% of max (use <=)
# TODO:
is_hurt = ...
is_critical = ...

# --- Part 2: combining ---------------------------------------------------------
# can_open_door  -> True when the player has the key AND the door is locked
#                   (opening an unlocked door needs no key logic)
# should_retreat -> True when critical AND out of potions
# TODO:
can_open_door = ...
should_retreat = ...

# --- Part 3: `not`, and the dark ------------------------------------------------
# in_darkness    -> True when the torch is NOT lit and depth is greater than 1
# TODO:
in_darkness = ...

# --- Part 4: spot the trap -------------------------------------------------------
# A previous adventurer wrote:   fatal = player_hp == 0 or -1
# That is ALWAYS truthy (or -1 doesn't do what they hoped — Python reads it
# as (player_hp == 0) or (-1), and -1 counts as True).
# Write it correctly: fatal is True when hp is 0 OR hp is -1... but the
# robust version every game uses is simply "hp is 0 or below".
# TODO:
fatal = ...
