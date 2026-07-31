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
    std::string roll_type = "";
    if(roll == 20){ roll_type = "crit";}
    else if(roll == 1){ roll_type = "miss"; }
    else if(roll >= 11 && roll <= 19){ roll_type = "hit" ;}
    else if(roll >= 2 && roll <= 10){ roll_type = "graze" ;}
    return roll_type;
}

// locked + no key -> "The door is locked."
// locked + key    -> "The key turns. The door opens."
// unlocked        -> "The door creaks open."
std::string door_message(bool has_key, bool door_locked) {
    std::string door_status = "";
    if(!has_key && door_locked) { door_status = "The door is locked.";}
    else if(has_key && door_locked) { door_status = "The key turns. The door opens.";}
    else if(!door_locked) { door_status = "The door creaks open.";}
    return door_status;
}

// Heal 10, but NEVER exceed max_hp — the clamp. Return new hp.
int potion_effect(int hp, int max_hp) {
    
    hp += 10;
    if(hp > max_hp){hp = max_hp;}
    return hp;
}
