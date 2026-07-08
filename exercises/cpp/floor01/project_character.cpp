// FLOOR C1 · PROJECT — THE ROLL (character creator, C++ edition)
// The same first organ you built in Python — now with a struct instead of a
// dict, and a preview of references (&). Follow the recipe; structs get
// their full lesson later.
//
// Run:  python3 dojo.py check c1-P
// Save: python3 dojo.py done c1-P

#include <string>

const int STARTING_HP = 30;
const int STARTING_LEVEL = 1;
const int STARTING_GOLD = 10;

// A struct is a bundle of named fields — the C++ answer to your Python dict,
// except the fields and their types are fixed at compile time.
struct Character {
    std::string name;
    int hp;
    int max_hp;
    int level;
    int gold;
};

// Build and return a Character using the constants above.
// Struct fields are set with dot syntax:  c.hp = STARTING_HP;
// (or brace-init in one line: return {name, STARTING_HP, ...} — field order!)
Character make_character(std::string name) {
    // TODO
    return {};
}

// Return EXACTLY:  Crumb | Lv 1 | HP 30/30 | 10g
// (std::to_string for every number)
std::string status_line(Character c) {
    // TODO
    return "";
}

// Level up the character: level +1, max_hp +5, hp restored to new max.
// NOTE the &: Character& means "the actual character, not a copy."
// Without it you'd level up a copy, the original stays weak, and you'd
// hunt that bug for an hour. (Python's dicts behaved this way for free.)
void level_up(Character& c) {
    // TODO
}
