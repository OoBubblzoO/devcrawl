import importlib.util
import sys
from pathlib import Path

EX = Path(__file__).resolve().parents[1] / "ex03_numbers.py"


def load():
    spec = importlib.util.spec_from_file_location("ex03_numbers", EX)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["ex03_numbers"] = mod
    spec.loader.exec_module(mod)
    return mod


def test_total_damage():
    mod = load()
    assert mod.total_damage == 12, "base_damage + strength_mod * 2 -> 6 + 6 = 12"


def test_gold_split():
    mod = load()
    assert mod.gold_each == 11, "47 // 4 should be 11 (floor division, not /)"
    assert isinstance(mod.gold_each, int), "Use //, not / — no float coins"
    assert mod.gold_leftover == 3, "47 % 4 should be 3"


def test_turn_parity():
    mod = load()
    assert mod.is_monster_turn is True, (
        "Turn 7 is odd -> monsters move. turn_number % 2 == 1 gives a real boolean."
    )
    assert isinstance(mod.is_monster_turn, bool), (
        "Compute it with a comparison (== ), not by writing True by hand"
    )


def test_crit():
    mod = load()
    assert mod.crit_damage == 21, "total_damage + strength_mod ** 2 -> 12 + 9 = 21"
