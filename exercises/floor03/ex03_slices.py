"""
FLOOR 3 · EXERCISE 3-3 — Slicing & iteration patterns
Lesson: 3.3 & 3.4

Slices carve pieces out of sequences: items[start:stop]. Combined with
sorted() and a few loop patterns, you can answer almost any question
about your game's data.

Run:  python3 dojo.py check 3-3
Save: python3 dojo.py done 3-3
"""


def top_three(scores):
    """Return the three highest scores, highest first.
        top_three([10, 50, 20, 90, 5]) -> [90, 50, 20]
    sorted(scores, reverse=True) then slice. Fewer than 3? Return them all.
    """
    # TODO
    ...


def recent_log(log, n):
    """Return the last n entries of the message log (a list of strings),
    oldest of those first — exactly what a game HUD shows.
        recent_log(["a","b","c","d"], 2) -> ["c", "d"]
    Negative slice indices are your friend.
    """
    # TODO
    ...


def count_rarities(items):
    """Given a list of rarity strings like
        ["common", "rare", "common", "epic", "common"]
    return a dict of counts: {"common": 3, "rare": 1, "epic": 1}.
    The counting-loop pattern (dict.get(key, 0) + 1) is used EVERYWHERE.
    """
    # TODO
    ...


def every_other_tile(tiles):
    """The rave-basement floor strobes: return every second tile starting
    from the first. tiles[::2] — the step slice.
        every_other_tile(["#", ".", "#", ".", "#"]) -> ["#", "#", "#"]
    """
    # TODO
    ...
