import importlib.util
import sys
from pathlib import Path

EX = Path(__file__).resolve().parents[1] / "ex03_slices.py"

spec = importlib.util.spec_from_file_location("ex03_slices", EX)
mod = importlib.util.module_from_spec(spec)
sys.modules["ex03_slices"] = mod
spec.loader.exec_module(mod)


def test_top_three():
    assert mod.top_three([10, 50, 20, 90, 5]) == [90, 50, 20]


def test_top_three_short_list():
    assert mod.top_three([7, 3]) == [7, 3]


def test_recent_log():
    assert mod.recent_log(["a", "b", "c", "d"], 2) == ["c", "d"]
    assert mod.recent_log(["a"], 3) == ["a"]


def test_count_rarities():
    assert mod.count_rarities(["common", "rare", "common", "epic", "common"]) == {
        "common": 3,
        "rare": 1,
        "epic": 1,
    }
    assert mod.count_rarities([]) == {}


def test_every_other_tile():
    assert mod.every_other_tile(["#", ".", "#", ".", "#"]) == ["#", "#", "#"]
