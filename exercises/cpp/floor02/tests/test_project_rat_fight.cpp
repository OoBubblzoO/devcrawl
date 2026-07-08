#include "../../devtest.h"
#include "../project_rat_fight.cpp"

int main() {
    CHECK_EQ(attack(6, 20), 14, "6 power vs 20 hp -> 14");
    CHECK_EQ(attack(10, 5), -5, "overkill goes negative");
    CHECK_EQ(is_defeated(0), true, "0 is down");
    CHECK_EQ(is_defeated(-3), true, "below 0 is down");
    CHECK_EQ(is_defeated(1), false, "1 hp fights on");
    CHECK_EQ(fight(30, 10, 20, 3), std::string("player"), "stronger player wins");
    CHECK_EQ(fight(10, 2, 40, 8), std::string("rat"), "Biscuit takes it");
    CHECK_EQ(fight(10, 10, 10, 10), std::string("player"), "mirror match: first strike wins");
    CHECK_EQ(fight_report(30, 10, 20, 3), std::string("player wins after 2 rounds"), "report");
    CHECK_EQ(fight_report(10, 2, 40, 8), std::string("rat wins after 2 rounds"), "report");
    CHECK_EQ(fight_report(10, 10, 10, 10), std::string("player wins after 1 rounds"), "report");
    return dt_summary();
}
