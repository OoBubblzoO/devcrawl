"""
FLOOR 2 · EXERCISE 2-2 — if / elif / else
Lesson: 2.2

Branching turns booleans into behavior. Order matters: Python takes the
FIRST branch that's true and skips the rest.

Run:  python3 dojo.py check 2-2
Save: python3 dojo.py done 2-2
"""


def classify_roll(roll):
    """A d20 attack roll. Return one of:
        "crit"   for a natural 20
        "miss"   for a natural 1
        "hit"    for anything 11 through 19
        "graze"  for anything 2 through 10
    Use if / elif / else — and think about the ORDER of your checks.
    """
    # TODO
    ...


def door_message(has_key, door_locked):
    """Return the right message:
        locked + no key  -> "The door is locked."
        locked + key     -> "The key turns. The door opens."
        unlocked         -> "The door creaks open."
    """
    # TODO
    ...


def potion_effect(hp, max_hp):
    """Drinking a potion heals 10, but hp can NEVER exceed max_hp.
    Return the new hp. (This clamp shows up in every game ever made —
    forgetting it is how you get 38/30 HP bugs.)
    """
    # TODO
    ...
