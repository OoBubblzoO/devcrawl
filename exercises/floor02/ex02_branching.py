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
    if roll == 1:
        return "miss"
    elif roll == 20:
        return "crit"
    elif roll in range(2,11):
        return "graze"
    elif roll in range(11,20):
        return "hit"



def door_message(has_key, door_locked):
    """Return the right message:
        locked + no key  -> "The door is locked."
        locked + key     -> "The key turns. The door opens."
        unlocked         -> "The door creaks open."
    """
    # TODO
    if door_locked and not has_key:
        return "The door is locked."
    elif door_locked and has_key:
        return "The key turns. The door opens."
    else:
        return "The door creaks open."

def potion_effect(hp, max_hp):
    """Drinking a potion heals 10, but hp can NEVER exceed max_hp.
    Return the new hp. (This clamp shows up in every game ever made —
    forgetting it is how you get 38/30 HP bugs.)
    """
    # TODO
    hp = hp + 10
    if hp > max_hp:
        hp = max_hp
    return hp
