"""
FLOOR 1 · EXERCISE 1-1 — Variables & types
Lesson: 1.1 (read it in the app first)

A variable is a name bound to a value. Python figures out the type from the
value you assign. Your job: fix and complete this character sheet so the
tests pass.

Run:  python3 dojo.py check 1-1
Save: python3 dojo.py done 1-1
"""

# --- Part 1: fix the broken names -------------------------------------------
# Two of these variable names are illegal or terrible. Fix them:
#   - Python names can't start with a digit
#   - Names should describe the value (single letters are a trap)
# The VALUES must stay the same — only rename.

# 1st_weapon = "rusty sword"
first_weapon = "rusty sword"  # <- assign "rusty sword"

torch_count = 3  # <- assign the same value x had, then delete the x line


# --- Part 2: create your character ------------------------------------------
# Create these four variables with the right TYPES:
#   player_name  -> a string, any name you want (not empty!)
#   player_hp    -> the integer 30
#   player_level -> the integer 1
#   is_alive     -> the boolean True   (careful: True, not "True")

# TODO: your four variables here
player_name = "Cheeto"
player_hp = 30
player_level = 1
is_alive = True


# --- Part 3: reassignment ----------------------------------------------------
# Variables can be rebound. The player drinks a potion: add 5 to player_hp
# by REUSING the variable (player_hp = player_hp + 5), don't just write 35.

# TODO: heal the player by 5 here

player_hp = player_hp + 5
