import importlib.util
import sys
from pathlib import Path

EX = Path(__file__).resolve().parents[1] / "project_loot.py"

spec = importlib.util.spec_from_file_location("project_loot", EX)
mod = importlib.util.module_from_spec(spec)
sys.modules["project_loot"] = mod
spec.loader.exec_module(mod)


def test_roll_loot_boundaries():
    assert mod.roll_loot(1) == "gold coin"
    assert mod.roll_loot(50) == "gold coin"
    assert mod.roll_loot(51) == "torch"
    assert mod.roll_loot(76) == "protein bar"
    assert mod.roll_loot(91) == "steel sword"
    assert mod.roll_loot(100) == "glowstick of the ancients"


def test_add_to_pack():
    assert mod.add_to_pack({}, "torch") == {"torch": 1}
    assert mod.add_to_pack({"torch": 2}, "torch") == {"torch": 3}


def test_open_chest():
    assert mod.open_chest({}, [3, 76, 3]) == {"gold coin": 2, "protein bar": 1}


def test_open_chest_empty_rolls():
    assert mod.open_chest({"torch": 1}, []) == {"torch": 1}


def test_pack_report():
    assert mod.pack_report({"torch": 2, "gold coin": 5}) == "gold coin x5\ntorch x2"
    assert mod.pack_report({}) == "(empty)"
