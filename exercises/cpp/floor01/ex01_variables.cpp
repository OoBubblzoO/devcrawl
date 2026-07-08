// FLOOR C1 · EXERCISE c1-1 — Variables & static types
// Lesson: c1.1 (read it in the app first)
//
// HEADS UP: this file does NOT compile as shipped. That is the exercise.
// In C++ the compiler is your first test — read its errors bottom-to-top
// of each block, fix, recompile. Lesson c1.4 teaches you how to read them.
//
// Run:  python3 dojo.py check c1-1
// Save: python3 dojo.py done c1-1

#include <string>

// --- Part 1: fix the broken declarations ------------------------------------
// C++ variables MUST declare a type, and names can't start with a digit.

// TODO: this one is missing its type (it should be an int):
torch_count = 3;

// TODO: this name is illegal — rename to first_weapon (keep the value):
std::string 1st_weapon = "rusty sword";


// --- Part 2: create your character ------------------------------------------
// Declare these four, with the right types:
//   player_name  -> std::string, any non-empty name
//   player_hp    -> int, 30
//   player_level -> int, 1
//   is_alive     -> bool, true      (lowercase true — this isn't Python!)

// TODO: your four variables here


// --- Part 3: const -----------------------------------------------------------
// Some values must never change. Declare:
//   const int STARTING_GOLD = 10;
// Then try (just once, to see the error) adding STARTING_GOLD = 99; below it.
// The compiler refuses — that refusal is a feature. Delete the bad line after.

// TODO: STARTING_GOLD here


// --- Part 4: reassignment ------------------------------------------------------
// The player drinks a potion. Add 5 to player_hp by REUSING the variable
// (player_hp = player_hp + 5;) — note this is a STATEMENT here at file scope,
// so wrap it in the provided function instead:

int heal_check() {
    // TODO: add 5 to player_hp, then return player_hp
    return 0;
}
