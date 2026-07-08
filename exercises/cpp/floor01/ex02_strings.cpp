// FLOOR C1 · EXERCISE c1-2 — std::string & std::to_string
// Lesson: c1.2
//
// C++ has no f-strings. Strings are built with + and std::to_string(number).
// Same HUD as the Python wing — feel the difference in the hands.
//
// Run:  python3 dojo.py check c1-2
// Save: python3 dojo.py done c1-2

#include <string>

std::string player_name = "Crumb";
int player_hp = 24;
int player_max_hp = 30;
int depth = 2;

// --- Part 1: the HUD ----------------------------------------------------------
// Build EXACTLY:   Crumb | HP 24/30 | Floor 2
// from the variables above. Numbers must pass through std::to_string —
// gluing an int onto a string directly won't compile (try it, read the error).
std::string make_hud() {
    // TODO
    return "";
}

// --- Part 2: shouting ------------------------------------------------------------
// Uppercase the message. C++ has no .upper() on strings (!) — loop over the
// characters and use toupper from <cctype> on each. Yes, really. Welcome to
// C++: closer to the metal, batteries not included.
#include <cctype>
std::string shout(std::string msg) {
    // TODO: for (char& c : msg) { ... }   then return msg
    return "";
}

// --- Part 3: the popup ------------------------------------------------------------
// Return: You take 7 damage!   (for damage=7 — use the parameter, not a literal 7)
std::string damage_popup(int damage) {
    // TODO
    return "";
}
