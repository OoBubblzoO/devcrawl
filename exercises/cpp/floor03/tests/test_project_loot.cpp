#include "../../devtest.h"
#include "../project_loot.cpp"

int main() {
    CHECK_EQ(roll_loot(1), std::string("gold coin"), "low roll");
    CHECK_EQ(roll_loot(50), std::string("gold coin"), "boundary 50");
    CHECK_EQ(roll_loot(51), std::string("torch"), "boundary 51");
    CHECK_EQ(roll_loot(76), std::string("protein bar"), "76");
    CHECK_EQ(roll_loot(91), std::string("steel sword"), "91");
    CHECK_EQ(roll_loot(100), std::string("glowstick of the ancients"), "legendary");

    std::map<std::string, int> pack;
    add_to_pack(pack, "torch");
    CHECK_EQ(pack["torch"], 1, "first torch");
    add_to_pack(pack, "torch");
    CHECK_EQ(pack["torch"], 2, "stacks");

    std::map<std::string, int> chest;
    open_chest(chest, {3, 76, 3});
    CHECK_EQ(chest["gold coin"], 2, "two coins");
    CHECK_EQ(chest["protein bar"], 1, "one bar");

    std::map<std::string, int> rpt = {{"torch", 2}, {"gold coin", 5}};
    CHECK_EQ(pack_report(rpt), std::string("gold coin x5\ntorch x2"),
             "alphabetical report (std::map sorts for free)");
    CHECK_EQ(pack_report({}), std::string("(empty)"), "empty pack");
    return dt_summary();
}
