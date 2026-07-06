import importlib.util
import sys
from pathlib import Path

EX = Path(__file__).resolve().parents[1] / "ex03_loops.py"

spec = importlib.util.spec_from_file_location("ex03_loops", EX)
mod = importlib.util.module_from_spec(spec)
sys.modules["ex03_loops"] = mod
spec.loader.exec_module(mod)


def test_turns_exact_kill():
    assert mod.turns_to_defeat(20, 5) == 4


def test_turns_with_overkill():
    assert mod.turns_to_defeat(22, 5) == 5, "5 hits: 22 -> 17 -> 12 -> 7 -> 2 -> -3"


def test_turns_one_shot():
    assert mod.turns_to_defeat(3, 50) == 1


def test_xp_curve():
    assert mod.total_xp_to_reach(1) == 0
    assert mod.total_xp_to_reach(2) == 100
    assert mod.total_xp_to_reach(3) == 300
    assert mod.total_xp_to_reach(4) == 600
    assert mod.total_xp_to_reach(10) == 4500


def test_torch_countdown():
    assert mod.torch_countdown(3) == "3... 2... 1... darkness."
    assert mod.torch_countdown(1) == "1... darkness."
