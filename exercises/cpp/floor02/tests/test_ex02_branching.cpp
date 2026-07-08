#include "../../devtest.h"
#include "../ex02_branching.cpp"

int main() {
    CHECK_EQ(classify_roll(20), std::string("crit"), "nat 20");
    CHECK_EQ(classify_roll(1), std::string("miss"), "nat 1");
    CHECK_EQ(classify_roll(19), std::string("hit"), "19 hits");
    CHECK_EQ(classify_roll(11), std::string("hit"), "11 hits");
    CHECK_EQ(classify_roll(10), std::string("graze"), "10 grazes");
    CHECK_EQ(classify_roll(2), std::string("graze"), "2 grazes");
    CHECK_EQ(door_message(false, true), std::string("The door is locked."), "locked, no key");
    CHECK_EQ(door_message(true, true), std::string("The key turns. The door opens."), "locked, key");
    CHECK_EQ(door_message(true, false), std::string("The door creaks open."), "unlocked");
    CHECK_EQ(door_message(false, false), std::string("The door creaks open."), "unlocked, keyless");
    CHECK_EQ(potion_effect(10, 30), 20, "10 + 10 = 20");
    CHECK_EQ(potion_effect(25, 30), 30, "clamped at max");
    CHECK_EQ(potion_effect(30, 30), 30, "already full stays full");
    return dt_summary();
}
