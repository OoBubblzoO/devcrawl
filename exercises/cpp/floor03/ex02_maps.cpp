// FLOOR C3 · EXERCISE c3-2 — std::map
// Lesson: c3.2
//
// The C++ dict. One glorious trap: map[key] on a MISSING key silently
// INSERTS a default value. Reading with [] can modify your data. Look up
// safely with .count(key) or .find(key).
//
// Run:  python3 dojo.py check c3-2
// Save: python3 dojo.py done c3-2

#include <string>
#include <map>

std::map<std::string, int> ITEM_DAMAGE = {
    {"rusty sword", 4}, {"steel sword", 9}, {"torch", 1}, {"protein bar", 0},
};
std::map<std::string, int> ITEM_VALUE = {
    {"rusty sword", 5}, {"steel sword", 40}, {"torch", 2}, {"protein bar", 3},
};
std::map<std::string, int> ITEM_HEALS = {
    {"protein bar", 8},
};

// Damage for an item, 0 if unknown — WITHOUT inserting into the map.
// (.count(name) first, or .find; [] alone would grow the map on misses.)
int item_damage(std::string name) {
    // TODO
    return -1;
}

// Edible = present in ITEM_HEALS.
bool is_edible(std::string name) {
    // TODO
    return false;
}

// Total value of ALL items in ITEM_VALUE.
// Loop:  for (auto& [name, value] : ITEM_VALUE) { ... }
int total_stock_value() {
    // TODO
    return -1;
}

// Name of the highest-value item — the best-so-far pattern.
std::string most_valuable() {
    // TODO
    return "";
}
