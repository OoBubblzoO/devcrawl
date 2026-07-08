// tests for c1-1 — compile+run via: python3 dojo.py check c1-1
#include "../../devtest.h"
#include "../ex01_variables.cpp"

int main() {
    CHECK_EQ(torch_count, 3, "torch_count should be an int holding 3");
    CHECK_EQ(first_weapon, std::string("rusty sword"), "first_weapon should be 'rusty sword'");
    CHECK(player_name.size() > 0, "player_name must be a non-empty std::string");
    CHECK_EQ(player_level, 1, "player_level must be 1");
    CHECK_EQ(is_alive, true, "is_alive must be the bool true");
    CHECK_EQ(STARTING_GOLD, 10, "STARTING_GOLD must be a const int 10");
    CHECK_EQ(heal_check(), 35, "heal_check(): 30 + 5 = 35, computed by reusing player_hp");
    return dt_summary();
}
