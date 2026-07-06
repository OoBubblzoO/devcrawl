"""
FLOOR 2 · PROJECT — RAT FIGHT
Your roguelike gets its second organ: the combat loop. A sparring rat named
Biscuit has volunteered (rats are training partners in this dungeon, not
vermin — be respectful).

Deterministic for now — randomness arrives on Floor 7, and deterministic
combat is TESTABLE combat. Remember that word.

Run:  python3 dojo.py check 2-P
Save: python3 dojo.py done 2-P
"""


def attack(attacker_power, defender_hp):
    """One attack lands. Return the defender's new hp (can go below 0)."""
    # TODO
    ...


def is_defeated(hp):
    """Return True when hp is 0 or below."""
    # TODO
    ...


def fight(player_hp, player_power, rat_hp, rat_power):
    """Run a full turn-based fight. The PLAYER always strikes first.

    Each round:
      1. Player attacks the rat. If the rat is defeated, stop: player wins.
      2. Rat attacks the player. If the player is defeated, stop: rat wins.
      3. Repeat.

    Return the string "player" or "rat" — whoever wins.
    Use the two helpers you just wrote. Build small, compose up:
    that habit is the whole reason big programs stay sane.
    """
    # TODO
    ...


def fight_report(player_hp, player_power, rat_hp, rat_power):
    """Return: "<winner> wins after <N> rounds"

    A round = one player attack (plus the rat's reply, if it survives).
    Example: fight_report(30, 10, 20, 3) -> "player wins after 2 rounds"
    You'll need to count rounds inside a loop — a modified copy of fight()
    is fine here. On Floor 4 you'll learn how to avoid the duplication.
    """
    # TODO
    ...


if __name__ == "__main__":
    print("You square up. Biscuit squeaks encouragingly.")
    print(f"Winner: {fight(30, 6, 25, 4)}")
    print(fight_report(30, 6, 25, 4))
