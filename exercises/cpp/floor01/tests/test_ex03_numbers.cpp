#include "../../devtest.h"
#include "../ex03_numbers.cpp"

int main() {
    CHECK_EQ(total_damage(), 12, "6 + 3*2 = 12");
    CHECK_EQ(gold_each(), 11, "47 / 4 in ints truncates to 11 — free floor division");
    CHECK_EQ(gold_leftover(), 3, "47 % 4 = 3");
    CHECK_EQ(is_monster_turn(), true, "turn 7 is odd -> monsters move");
    CHECK(health_percent(24, 30) > 79.9 && health_percent(24, 30) < 80.1,
          "24/30 should be ~80.0 — cast to double BEFORE dividing");
    CHECK(health_percent(1, 3) > 33.0 && health_percent(1, 3) < 33.4,
          "1/3 should be ~33.3, not 0 — int/int truncates");
    return dt_summary();
}
