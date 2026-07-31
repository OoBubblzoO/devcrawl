// FLOOR C2 · EXERCISE c2-1 — Booleans & comparisons
// Lesson: c2.1
//
// Same state checks as the Python wing — with C++'s own trap: = vs ==.
// `if (hp = 0)` ASSIGNS zero and evaluates false. It compiles. It ruins
// evenings. (Compile with -Wall and the compiler warns you — dojo does.)
//
// Run:  python3 dojo.py check c2-1
// Save: python3 dojo.py done c2-1

int player_hp = 7;
int player_max_hp = 30;
bool has_key = true;
bool door_locked = true;
int potions = 0;
int depth = 3;
bool torch_lit = false;

// hurt when below max
bool is_hurt()   { if (player_hp < player_max_hp) { return true; } return false; }

// at or below 25% of max. CAREFUL: player_max_hp / 4 in ints is 7 (30/4
// truncates). Here that happens to work — but write it robustly with a
// double: player_hp <= player_max_hp * 0.25
bool is_critical()  { if (double(player_hp) <= player_max_hp * 0.25) { return true; } return false; }

// has the key AND the door is locked
bool can_open_door() { if (has_key && door_locked) {return true; } return false; }

// critical AND out of potions
bool should_retreat() { if(potions == 0 && is_critical()){ return true; } return false; }

// torch NOT lit and deeper than floor 1
bool in_darkness()  { if (!torch_lit && depth > 1) { return true; } return false; }

// the robust death check: 0 or below (never ==)
bool fatal()        { if (player_hp <= 0) return true; else return false; }
