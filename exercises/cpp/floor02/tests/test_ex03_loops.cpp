#include "../../devtest.h"
#include "../ex03_loops.cpp"

int main() {
    CHECK_EQ(turns_to_defeat(20, 5), 4, "exact kill in 4");
    CHECK_EQ(turns_to_defeat(22, 5), 5, "overkill still counts the last turn");
    CHECK_EQ(turns_to_defeat(3, 50), 1, "one-shot");
    CHECK_EQ(total_xp_to_reach(1), 0, "you start at 1");
    CHECK_EQ(total_xp_to_reach(2), 100, "1*100");
    CHECK_EQ(total_xp_to_reach(4), 600, "100+200+300");
    CHECK_EQ(total_xp_to_reach(10), 4500, "the curve");
    CHECK_EQ(torch_countdown(3), std::string("3... 2... 1... darkness."), "countdown 3");
    CHECK_EQ(torch_countdown(1), std::string("1... darkness."), "countdown 1");
    return dt_summary();
}
