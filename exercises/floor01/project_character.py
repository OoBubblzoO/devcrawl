"""
FLOOR 1 · PROJECT — THE ROLL (character creator)
This is the first piece of your final roguelike. Everything you build in
later floors will act on the character dict you create here.

Functions get their full lesson on Floor 4 — for now, follow the recipe:
the skeletons are written, you fill in the bodies. A function takes inputs
(parameters), does work, and hands back a result with `return`.

Run:  python3 dojo.py check 1-P
Save: python3 dojo.py done 1-P
"""

STARTING_HP = 30
STARTING_LEVEL = 1
STARTING_GOLD = 10


def make_character(name):
    """Build and return the character dict.

    Return a dict with exactly these keys:
        "name"  -> the name that was passed in
        "hp"    -> STARTING_HP
        "max_hp"-> STARTING_HP
        "level" -> STARTING_LEVEL
        "gold"  -> STARTING_GOLD

    Use the CONSTANTS above, not raw numbers — when you rebalance the game
    later, you change one line instead of ten.
    """
    # TODO: build the dict and return it
    ...


def status_line(character):
    """Return the HUD string for a character dict, EXACTLY in this shape:

        Crumb | Lv 1 | HP 30/30 | 10g

    (using the character's actual values, via an f-string)
    Dict values are read with square brackets: character["name"]
    """
    # TODO
    ...


def level_up(character):
    """Level the character up, then return the (same) dict.

    Leveling up means:
        level  +1
        max_hp +5
        hp     restored to the new max_hp   (ding heals — classic RPG rule)
    """
    # TODO
    ...


if __name__ == "__main__":
    # Play with your creation! `python3 exercises/floor01/project_character.py`
    hero = make_character("Crumb")
    print(status_line(hero))
    level_up(hero)
    print(status_line(hero))
