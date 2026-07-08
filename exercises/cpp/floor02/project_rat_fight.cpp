// FLOOR C2 · PROJECT — RAT FIGHT (C++ edition)
// Biscuit returns for round two. Same deterministic combat you built in
// Python — feel how the static types change the experience.
//
// Run:  python3 dojo.py check c2-P
// Save: python3 dojo.py done c2-P

#include <string>

// One attack lands: return the defender's new hp (may go below 0).
int attack(int attacker_power, int defender_hp) {
    // TODO
    return -999;
}

// 0 or below = down.
bool is_defeated(int hp) {
    // TODO
    return false;
}

// Full turn-based fight, PLAYER strikes first each round.
// Return "player" or "rat". Compose your two helpers.
std::string fight(int player_hp, int player_power, int rat_hp, int rat_power) {
    // TODO
    return "";
}

// "<winner> wins after <N> rounds" — a round is one player attack
// (plus the rat's reply if it survives). std::to_string for N.
std::string fight_report(int player_hp, int player_power, int rat_hp, int rat_power) {
    // TODO
    return "";
}
