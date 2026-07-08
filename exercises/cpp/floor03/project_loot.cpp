// FLOOR C3 · PROJECT — THE LOOT TABLE (C++ edition)
// Same d100 table, same stacking pack — with a gift at the end: std::map
// keeps its keys sorted automatically, so the alphabetized report that took
// Python a sorted() call falls out for free.
//
// Run:  python3 dojo.py check c3-P
// Save: python3 dojo.py done c3-P

#include <string>
#include <vector>
#include <map>

struct LootEntry {
    int max_roll;
    std::string item;
};

std::vector<LootEntry> LOOT_TABLE = {
    {50,  "gold coin"},
    {75,  "torch"},
    {90,  "protein bar"},
    {99,  "steel sword"},
    {100, "glowstick of the ancients"},
};

// d100 roll: first entry whose max_roll >= roll wins.
std::string roll_loot(int roll) {
    // TODO
    return "";
}

// Stacking pack: item -> count. pack[item]++ does everything.
void add_to_pack(std::map<std::string, int>& pack, std::string item) {
    // TODO
}

// For each roll, roll_loot then add_to_pack. Compose — no new logic.
void open_chest(std::map<std::string, int>& pack, const std::vector<int>& rolls) {
    // TODO
}

// "gold coin x5\ntorch x2" — alphabetical. std::map iterates in key order
// already; just build the lines. Empty pack -> "(empty)"
std::string pack_report(const std::map<std::string, int>& pack) {
    // TODO
    return "";
}
