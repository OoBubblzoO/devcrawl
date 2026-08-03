// FLOOR C2 · PROJECT — RAT FIGHT (C++ edition)
// Biscuit returns for round two. Same deterministic combat you built in
// Python — feel how the static types change the experience.
//
// Run:  python3 dojo.py check c2-P
// Save: python3 dojo.py done c2-P

#include <string>

// One attack lands: return the defender's new hp (may go below 0).
int attack(int attacker_power, int defender_hp) {
    // while (defender_hp > 0) {
    //     defender_hp -= attacker_power;
    //     break;   
    // }
    return defender_hp -= attacker_power;
}

// 0 or below = down.
bool is_defeated(int hp) {
    // TODO
    return hp <= 0;
}

// Full turn-based fight, PLAYER strikes first each round.
// Return "player" or "rat". Compose your two helpers.
std::string fight(int player_hp, int player_power, int rat_hp, int rat_power) {
    std::string winner = "";
    while (player_hp > 0 || rat_hp > 0){
        rat_hp -= player_power;
        if (rat_hp <= 0){
            winner = "player";
            break;
        }
        player_hp -= rat_power;
        if (player_hp <= 0){
            winner = "rat";
            break;
        }
    }
    return winner;
}

// "<winner> wins after <N> rounds" — a round is one player attack
// (plus the rat's reply if it survives). std::to_string for N.
std::string fight_report(int player_hp, int player_power, int rat_hp, int rat_power) {
    int turns = 0;
    std::string winner = "";

    while (player_hp > 0 || rat_hp > 0){
        rat_hp = attack(player_power, rat_hp);
        turns += 1;
        if (is_defeated(rat_hp)){
            winner = "player";
            break;
        }
        player_hp = attack(rat_power, player_hp);
        if (is_defeated(player_hp)){
            winner = "rat";
            break;
        }
    }
    return winner + " wins after " + std::to_string(turns) + " rounds";
}
