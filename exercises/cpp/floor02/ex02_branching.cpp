// FLOOR C2 · EXERCISE c2-2 — if / else if / else
// Lesson: c2.2
//
// Run:  python3 dojo.py check c2-2
// Save: python3 dojo.py done c2-2

#include <string>

// d20 attack roll:
//   20 -> "crit"    1 -> "miss"    11..19 -> "hit"    2..10 -> "graze"
// Order matters — most specific first.
std::string classify_roll(int roll) {
    // TODO
    return "";
}

// locked + no key -> "The door is locked."
// locked + key    -> "The key turns. The door opens."
// unlocked        -> "The door creaks open."
std::string door_message(bool has_key, bool door_locked) {
    // TODO
    return "";
}

// Heal 10, but NEVER exceed max_hp — the clamp. Return new hp.
int potion_effect(int hp, int max_hp) {
    // TODO
    return -1;
}
