import importlib.util
import re
import sys
from pathlib import Path

EX = Path(__file__).resolve().parents[1] / "ex02_strings.py"


def load():
    spec = importlib.util.spec_from_file_location("ex02_strings", EX)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["ex02_strings"] = mod
    spec.loader.exec_module(mod)
    return mod


def test_hud_line():
    mod = load()
    assert mod.hud_line == "Crumb | HP 24/30 | Floor 2"


def test_hud_uses_variables_not_literals():
    source = EX.read_text()
    hud_assignment = [l for l in source.splitlines() if l.strip().startswith("hud_line")]
    assert hud_assignment, "hud_line assignment is missing"
    line = hud_assignment[-1]
    assert re.search(r"""f["']""", line), "Use an f-string: hud_line = f\"...\""
    assert "player_hp" in line and "depth" in line, (
        "Interpolate the variables ({player_hp}, {depth}) — don't hardcode 24 or 2"
    )


def test_loud():
    mod = load()
    assert mod.loud == "A WILD RAT APPROACHES"


def test_popup():
    mod = load()
    assert mod.popup == "You take 7 damage!"
