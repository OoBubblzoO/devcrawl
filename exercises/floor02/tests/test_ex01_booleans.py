import importlib.util
import sys
from pathlib import Path

EX = Path(__file__).resolve().parents[1] / "ex01_booleans.py"

spec = importlib.util.spec_from_file_location("ex01_booleans", EX)
mod = importlib.util.module_from_spec(spec)
sys.modules["ex01_booleans"] = mod
spec.loader.exec_module(mod)


def test_is_hurt():
    assert mod.is_hurt is True, "7 < 30 -> hurt"


def test_is_critical():
    assert mod.is_critical is True, "7 <= 30 * 0.25 (7.5) -> critical"


def test_can_open_door():
    assert mod.can_open_door is True, "has_key and door_locked"


def test_should_retreat():
    assert mod.should_retreat is True, "critical and no potions -> run"


def test_in_darkness():
    assert mod.in_darkness is True, "not torch_lit and depth > 1"


def test_fatal():
    assert mod.fatal is False, "hp is 7 -> not fatal. The robust check: player_hp <= 0"
