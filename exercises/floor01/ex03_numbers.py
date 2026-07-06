"""
FLOOR 1 · EXERCISE 1-3 — Numbers & operators
Lesson: 1.3

Stat math is game design. Damage formulas, gold splits, turn order — it's
all arithmetic, and Python has a few operators you MUST know:
    +  -  *      the obvious ones
    /            true division (ALWAYS gives a float: 7 / 2 == 3.5)
    //           floor division (drops the remainder: 7 // 2 == 3)
    %            modulo, the remainder (7 % 2 == 1)
    **           power (2 ** 3 == 8)

Run:  python3 dojo.py check 1-3
Save: python3 dojo.py done 1-3
"""

base_damage = 6
strength_mod = 3
gold_found = 47
party_size = 4
turn_number = 7

# --- Part 1: the damage formula ----------------------------------------------
# total_damage = base damage plus twice the strength modifier
# TODO:
total_damage = ...

# --- Part 2: splitting the loot ----------------------------------------------
# The party splits gold_found evenly. Nobody gets fractions of a coin.
#   gold_each      -> each member's share as a whole int (floor division)
#   gold_leftover  -> coins that couldn't be split (modulo)
# TODO:
gold_each = ...
gold_leftover = ...

# --- Part 3: whose turn? -------------------------------------------------------
# On even turn numbers the player moves; on odd turns the monsters move.
# Compute is_monster_turn as a boolean using % and == (no if statements yet —
# a comparison already produces True/False).
# TODO:
is_monster_turn = ...

# --- Part 4: crit! -------------------------------------------------------------
# A critical hit squares the strength modifier and adds it to total_damage.
# Use ** for the square. (Don't modify total_damage — new variable.)
# TODO:
crit_damage = ...
