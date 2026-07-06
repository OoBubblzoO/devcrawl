"""
FLOOR 3 · PROJECT — THE LOOT TABLE
Third organ of the roguelike: loot and a stacking inventory. When the
procgen floor generator arrives on Floor 7, it will pull from this table.

Run:  python3 dojo.py check 3-P
Save: python3 dojo.py done 3-P
"""

# Roll a d100. You get the FIRST entry whose max_roll is >= your roll.
LOOT_TABLE = [
    {"max_roll": 50, "item": "gold coin", "rarity": "common"},
    {"max_roll": 75, "item": "torch", "rarity": "common"},
    {"max_roll": 90, "item": "protein bar", "rarity": "uncommon"},
    {"max_roll": 99, "item": "steel sword", "rarity": "rare"},
    {"max_roll": 100, "item": "glowstick of the ancients", "rarity": "legendary"},
]


def roll_loot(roll):
    """Given a roll from 1-100, return the ITEM NAME won.
    Loop through LOOT_TABLE in order; first entry with max_roll >= roll wins.
        roll_loot(3)   -> "gold coin"
        roll_loot(76)  -> "protein bar"
        roll_loot(100) -> "glowstick of the ancients"
    """
    # TODO
    ...


def add_to_pack(pack, item):
    """The pack is a STACKING inventory — a dict of item -> count.
    Add one of `item` and return the pack.
        add_to_pack({}, "torch")            -> {"torch": 1}
        add_to_pack({"torch": 2}, "torch")  -> {"torch": 3}
    (That .get(key, 0) pattern from exercise 3-3 pays off immediately.)
    """
    # TODO
    ...


def open_chest(pack, rolls):
    """A chest gives several rolls at once. For each roll in `rolls`,
    roll the loot and add it to the pack. Return the pack.
        open_chest({}, [3, 76, 3]) -> {"gold coin": 2, "protein bar": 1}
    Compose your two functions — write no new logic.
    """
    # TODO
    ...


def pack_report(pack):
    """Return the pack as display lines, ALPHABETICAL by item, one string:
        pack_report({"torch": 2, "gold coin": 5})
        -> "gold coin x5\ntorch x2"
    sorted(pack) gives you the keys in order. Join lines with "\n".
    Empty pack -> "(empty)"
    """
    # TODO
    ...
