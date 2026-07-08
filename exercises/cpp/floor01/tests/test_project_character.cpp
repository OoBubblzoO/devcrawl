#include "../../devtest.h"
#include "../project_character.cpp"

int main() {
    Character c = make_character("Remy");
    CHECK_EQ(c.name, std::string("Remy"), "name is the one passed in");
    CHECK_EQ(c.hp, 30, "hp starts at STARTING_HP");
    CHECK_EQ(c.max_hp, 30, "max_hp starts at STARTING_HP");
    CHECK_EQ(c.level, 1, "level starts at 1");
    CHECK_EQ(c.gold, 10, "gold starts at 10");

    Character h = make_character("Crumb");
    CHECK_EQ(status_line(h), std::string("Crumb | Lv 1 | HP 30/30 | 10g"), "status line");
    h.hp = 12; h.gold = 99;
    CHECK_EQ(status_line(h), std::string("Crumb | Lv 1 | HP 12/30 | 99g"),
             "status line reflects current values");

    Character w = make_character("Crumb");
    w.hp = 4;                       // wounded before the ding
    level_up(w);
    CHECK_EQ(w.level, 2, "level_up: +1 level");
    CHECK_EQ(w.max_hp, 35, "level_up: +5 max hp");
    CHECK_EQ(w.hp, 35, "level_up heals to the NEW max — and must modify the ORIGINAL (that's the &)");
    level_up(w);
    CHECK_EQ(w.max_hp, 40, "stacks on repeat");
    return dt_summary();
}
