import importlib.util
import sys
from pathlib import Path

EX = Path(__file__).resolve().parents[1] / "ex01_lists.py"

spec = importlib.util.spec_from_file_location("ex01_lists", EX)
mod = importlib.util.module_from_spec(spec)
sys.modules["ex01_lists"] = mod
spec.loader.exec_module(mod)


def test_add_item():
    inv = ["torch"]
    assert mod.add_item(inv, "rope") == ["torch", "rope"]


def test_drop_item():
    assert mod.drop_item(["torch", "rope", "torch"], "torch") == ["rope", "torch"]


def test_drop_missing_item_is_safe():
    assert mod.drop_item(["torch"], "banana") == ["torch"], (
        "Dropping an item you don't have must not crash (.remove on a missing "
        "item raises ValueError — guard it)"
    )


def test_has_item():
    assert mod.has_item(["torch", "rope"], "rope") is True
    assert mod.has_item([], "rope") is False


def test_newest_item():
    assert mod.newest_item(["torch", "rope"]) == "rope"
    assert mod.newest_item([]) is None, "Empty inventory -> None, not a crash"
