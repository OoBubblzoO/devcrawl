import importlib.util
import sys
from pathlib import Path

EX = Path(__file__).resolve().parents[1] / "ex02_branching.py"

spec = importlib.util.spec_from_file_location("ex02_branching", EX)
mod = importlib.util.module_from_spec(spec)
sys.modules["ex02_branching"] = mod
spec.loader.exec_module(mod)


def test_classify_roll():
    assert mod.classify_roll(20) == "crit"
    assert mod.classify_roll(1) == "miss"
    assert mod.classify_roll(19) == "hit"
    assert mod.classify_roll(11) == "hit"
    assert mod.classify_roll(10) == "graze"
    assert mod.classify_roll(2) == "graze"


def test_door_message():
    assert mod.door_message(False, True) == "The door is locked."
    assert mod.door_message(True, True) == "The key turns. The door opens."
    assert mod.door_message(True, False) == "The door creaks open."
    assert mod.door_message(False, False) == "The door creaks open."


def test_potion_heals():
    assert mod.potion_effect(10, 30) == 20


def test_potion_clamps_at_max():
    assert mod.potion_effect(25, 30) == 30, "10 healing from 25 must clamp to 30, not 35"
    assert mod.potion_effect(30, 30) == 30
