import importlib.util
import sys
from pathlib import Path

EX = Path(__file__).resolve().parents[1] / "ex02_dicts.py"

spec = importlib.util.spec_from_file_location("ex02_dicts", EX)
mod = importlib.util.module_from_spec(spec)
sys.modules["ex02_dicts"] = mod
spec.loader.exec_module(mod)


def test_item_damage():
    assert mod.item_damage("steel sword") == 9
    assert mod.item_damage("torch") == 1


def test_unknown_item_damage_is_zero():
    assert mod.item_damage("cursed spoon") == 0, "Unknown items -> 0, never a KeyError"


def test_is_edible():
    assert mod.is_edible("protein bar") is True
    assert mod.is_edible("torch") is False
    assert mod.is_edible("cursed spoon") is False


def test_price_list():
    assert mod.price_list() == {
        "rusty sword": 5,
        "steel sword": 40,
        "torch": 2,
        "protein bar": 3,
    }


def test_most_valuable():
    assert mod.most_valuable() == "steel sword"
