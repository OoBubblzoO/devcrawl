"""
FLOOR 3 · EXERCISE 3-2 — Dictionaries
Lesson: 3.2

A dict maps keys to values. Item stats, monster templates, the character
sheet you built on Floor 1 — dicts are the noun of game development.

Run:  python3 dojo.py check 3-2
Save: python3 dojo.py done 3-2
"""

ITEM_STATS = {
    "rusty sword": {"damage": 4, "value": 5},
    "steel sword": {"damage": 9, "value": 40},
    "torch": {"damage": 1, "value": 2},
    "protein bar": {"damage": 0, "value": 3, "heals": 8},
}


def item_damage(item_name):
    """Return the damage stat for an item, or 0 if the item is unknown.
    Unknown items must NOT crash — use .get() with a default instead of
    square brackets. (KeyError crashes on unknown keys are a classic.)
    """
    # TODO
    ...


def is_edible(item_name):
    """Return True if the item has a "heals" stat.
    (Hint: `"heals" in some_dict` checks for a KEY.)
    Unknown items are not edible.
    """
    # TODO
    ...


def price_list():
    """Return a NEW dict mapping each item name -> its value stat:
        {"rusty sword": 5, "steel sword": 40, ...}
    Loop over ITEM_STATS.items() and build it up.
    """
    # TODO
    ...


def most_valuable():
    """Return the NAME of the highest-value item in ITEM_STATS.
    Track a best-so-far name and value while looping. (max() with a key
    also works if you've met lambdas — both pass.)
    """
    # TODO
    ...
