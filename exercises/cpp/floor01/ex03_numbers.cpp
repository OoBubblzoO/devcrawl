// FLOOR C1 · EXERCISE c1-3 — Numbers & operators
// Lesson: c1.3
//
// Python's trap was / giving floats. C++ flips it: int / int TRUNCATES.
// 7 / 2 is 3 in C++. Free floor division — until it silently eats your
// percentages. Know which mode you're in.
//
// Run:  python3 dojo.py check c1-3
// Save: python3 dojo.py done c1-3

int base_damage = 6;
int strength_mod = 3;
int gold_found = 47;
int party_size = 4;
int turn_number = 7;

// --- Part 1: the damage formula -----------------------------------------------
// base damage plus twice the strength modifier
int total_damage() {
    int damage = base_damage + (strength_mod * 2);
    return damage;
}

// --- Part 2: splitting the loot -------------------------------------------------
// int division already floors — no special operator needed here.
int gold_each()      { int gold_taken = gold_found / party_size; return gold_taken; }
int gold_leftover()  { int gold_left = gold_found % party_size; return gold_left; }

// --- Part 3: whose turn? ----------------------------------------------------------
// true on odd turns (monsters move). A comparison already yields a bool.
bool is_monster_turn() {
    if (turn_number % 2 == 1) {
        return true; 
    }
    return false;
}

// --- Part 4: the health percentage trap ---------------------------------------------
// hp=24, max=30 → should be 80.0. But hp / max_hp in ints is 0 — the classic
// C++ bug. Cast one side to double FIRST:  (double)hp / max_hp * 100
double health_percent(int hp, int max_hp) {
    double health = double(hp) / max_hp * 100;
    return health;
}
