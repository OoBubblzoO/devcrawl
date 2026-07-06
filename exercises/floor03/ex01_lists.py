"""
FLOOR 3 · EXERCISE 3-1 — Lists
Lesson: 3.1

A list is an ordered, changeable collection. Your inventory, the monsters
in a room, the log of everything that happened — all lists.

Run:  python3 dojo.py check 3-1
Save: python3 dojo.py done 3-1
"""


def add_item(inventory, item):
    """Add item to the END of the inventory, then return the inventory."""
    # TODO
    ...


def drop_item(inventory, item):
    """Remove the FIRST matching item if present, then return the inventory.
    If the item isn't there, return the inventory unchanged — dropping
    nothing should never crash the game. (Check with `in` first.)
    """
    # TODO
    ...


def has_item(inventory, item):
    """Return True if the item is in the inventory."""
    # TODO
    ...


def newest_item(inventory):
    """Return the most recently added item, or None for an empty inventory.
    (Negative indexing is the pythonic move: inventory[-1].)
    """
    # TODO
    ...
