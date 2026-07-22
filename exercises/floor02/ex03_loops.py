"""
FLOOR 2 · EXERCISE 2-3 — Loops
Lesson: 2.3 & 2.4

A game IS a loop: while the player is alive, keep taking turns.
`while` runs as long as a condition holds; `for` runs over a sequence.

Run:  python3 dojo.py check 2-3
Save: python3 dojo.py done 2-3
"""


def turns_to_defeat(monster_hp, damage_per_turn):
    """How many turns to bring monster_hp to 0 or below, hitting for
    damage_per_turn each turn? Use a WHILE loop and count the turns.
    (Yes, math could do it — but this is the skeleton of your combat loop.)
    """
    # TODO
    turns = 0
    while monster_hp > 0:
        monster_hp -= damage_per_turn
        turns += 1
    return turns


def total_xp_to_reach(level):
    """XP needed to reach `level` from level 1, where each level-up costs
    (current_level * 100) XP. Use a FOR loop over range.
        level 1 -> 0        (you start there)
        level 2 -> 100      (1*100)
        level 3 -> 300      (1*100 + 2*100)
        level 4 -> 600
    """
    # TODO
    xp = 0 
    for current_lvl in range(1, level):
        xp = xp + current_lvl * 100
        print(f"Level {current_lvl} costs {current_lvl * 100} XP, total: {xp}")
    return xp


def torch_countdown(turns):
    """Return the dungeon's torch warning as ONE string built in a loop:
        torch_countdown(3) -> "3... 2... 1... darkness."
    Build it up with a loop counting DOWN (hint: range(turns, 0, -1)),
    then add "darkness." at the end.
    """
    # TODO
    darkness = ""
    for count in range(turns, 0, -1):
        darkness += f"{count}... "
    darkness += "darkness."
    # print(darkness)
    return darkness
