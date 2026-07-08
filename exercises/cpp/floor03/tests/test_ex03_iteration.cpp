#include "../../devtest.h"
#include "../ex03_iteration.cpp"

int main() {
    std::vector<int> t = top_three({10, 50, 20, 90, 5});
    CHECK_EQ(t.size(), (size_t)3, "three results");
    CHECK(t.size() == 3 && t[0] == 90 && t[1] == 50 && t[2] == 20, "90, 50, 20 in order");
    std::vector<int> s = top_three({7, 3});
    CHECK(s.size() == 2 && s[0] == 7 && s[1] == 3, "short lists return what exists");

    std::vector<std::string> r = recent_log({"a", "b", "c", "d"}, 2);
    CHECK(r.size() == 2 && r[0] == "c" && r[1] == "d", "last two, oldest first");

    auto counts = count_rarities({"common", "rare", "common", "epic", "common"});
    CHECK_EQ(counts["common"], 3, "3 commons");
    CHECK_EQ(counts["rare"], 1, "1 rare");
    CHECK_EQ(counts["epic"], 1, "1 epic");

    auto strobe = every_other_tile({"#", ".", "#", ".", "#"});
    CHECK(strobe.size() == 3 && strobe[0] == "#" && strobe[2] == "#", "strobe pattern");
    return dt_summary();
}
