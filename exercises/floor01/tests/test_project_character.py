import importlib.util
import sys
from pathlib import Path

EX = Path(__file__).resolve().parents[1] / "project_character.py"

spec = importlib.util.spec_from_file_location("project_character", EX)
mod = importlib.util.module_from_spec(spec)
sys.modules["project_character"] = mod
spec.loader.exec_module(mod)


def test_make_character_shape():
    c = mod.make_character("Remy")
    assert c == {"name": "Remy", "hp": 30, "max_hp": 30, "level": 1, "gold": 10}


def test_make_character_uses_the_name_given():
    assert mod.make_character("Patches")["name"] == "Patches"


def test_status_line():
    c = mod.make_character("Crumb")
    assert mod.status_line(c) == "Crumb | Lv 1 | HP 30/30 | 10g"


def test_status_line_reflects_current_values():
    c = mod.make_character("Crumb")
    c["hp"] = 12
    c["gold"] = 99
    assert mod.status_line(c) == "Crumb | Lv 1 | HP 12/30 | 99g"


def test_level_up():
    c = mod.make_character("Crumb")
    c["hp"] = 4  # wounded before the ding
    result = mod.level_up(c)
    assert result["level"] == 2
    assert result["max_hp"] == 35
    assert result["hp"] == 35, "Leveling up should heal to the NEW max"


def test_level_up_twice():
    c = mod.make_character("Crumb")
    mod.level_up(c)
    mod.level_up(c)
    assert c["level"] == 3 and c["max_hp"] == 40 and c["hp"] == 40
