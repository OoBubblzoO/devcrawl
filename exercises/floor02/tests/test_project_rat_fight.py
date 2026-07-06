import importlib.util
import sys
from pathlib import Path

EX = Path(__file__).resolve().parents[1] / "project_rat_fight.py"

spec = importlib.util.spec_from_file_location("project_rat_fight", EX)
mod = importlib.util.module_from_spec(spec)
sys.modules["project_rat_fight"] = mod
spec.loader.exec_module(mod)


def test_attack():
    assert mod.attack(6, 20) == 14
    assert mod.attack(10, 5) == -5


def test_is_defeated():
    assert mod.is_defeated(0) is True
    assert mod.is_defeated(-3) is True
    assert mod.is_defeated(1) is False


def test_player_wins_when_stronger():
    assert mod.fight(30, 10, 20, 3) == "player"


def test_rat_wins_when_player_is_weak():
    assert mod.fight(10, 2, 40, 8) == "rat"


def test_player_first_strike_advantage():
    # Mirror stats: player swings first, so the player wins the mirror match
    assert mod.fight(10, 10, 10, 10) == "player"


def test_fight_report():
    assert mod.fight_report(30, 10, 20, 3) == "player wins after 2 rounds"
    assert mod.fight_report(10, 2, 40, 8) == "rat wins after 2 rounds"
    assert mod.fight_report(10, 10, 10, 10) == "player wins after 1 rounds"
