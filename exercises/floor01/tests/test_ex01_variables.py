import importlib.util
import sys
from pathlib import Path

EX = Path(__file__).resolve().parents[1] / "ex01_variables.py"


def load():
    spec = importlib.util.spec_from_file_location("ex01_variables", EX)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["ex01_variables"] = mod
    spec.loader.exec_module(mod)
    return mod


def test_renamed_weapon():
    mod = load()
    assert getattr(mod, "first_weapon", None) == "rusty sword", (
        "first_weapon should hold the string 'rusty sword'"
    )


def test_meaningful_torch_name():
    mod = load()
    assert getattr(mod, "torch_count", None) == 3, "torch_count should be 3"
    assert not hasattr(mod, "x"), (
        "Delete the old `x = 3` line — one value, one good name."
    )


def test_character_types():
    mod = load()
    assert isinstance(mod.player_name, str) and len(mod.player_name) > 0, (
        "player_name must be a non-empty string"
    )
    assert isinstance(mod.player_level, int) and mod.player_level == 1, (
        "player_level must be the integer 1"
    )
    assert isinstance(mod.is_alive, bool) and mod.is_alive is True, (
        "is_alive must be the boolean True — no quotes! 'True' is a string."
    )


def test_potion_heal():
    mod = load()
    assert isinstance(mod.player_hp, int), "player_hp must be an integer"
    assert mod.player_hp == 35, (
        "player_hp should end at 35: start at 30, then player_hp = player_hp + 5"
    )
