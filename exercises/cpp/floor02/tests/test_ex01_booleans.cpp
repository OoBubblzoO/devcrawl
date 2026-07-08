#include "../../devtest.h"
#include "../ex01_booleans.cpp"

int main() {
    CHECK_EQ(is_hurt(), true, "7 < 30 -> hurt");
    CHECK_EQ(is_critical(), true, "7 <= 30*0.25 (7.5) -> critical");
    CHECK_EQ(can_open_door(), true, "has_key && door_locked");
    CHECK_EQ(should_retreat(), true, "critical && potions == 0");
    CHECK_EQ(in_darkness(), true, "!torch_lit && depth > 1");
    CHECK_EQ(fatal(), false, "hp is 7 -> not fatal; the check is hp <= 0");
    return dt_summary();
}
