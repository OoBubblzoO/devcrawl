#include "../../devtest.h"
#include "../ex02_maps.cpp"

int main() {
    CHECK_EQ(item_damage("steel sword"), 9, "steel sword hits for 9");
    CHECK_EQ(item_damage("torch"), 1, "torch: 1");
    CHECK_EQ(item_damage("cursed spoon"), 0, "unknown items -> 0");
    size_t before = ITEM_DAMAGE.size();
    item_damage("another unknown thing");
    CHECK_EQ(ITEM_DAMAGE.size(), before,
             "looking up an unknown item must NOT insert it ([] trap!)");
    CHECK_EQ(is_edible("protein bar"), true, "gym fuel");
    CHECK_EQ(is_edible("torch"), false, "please don't");
    CHECK_EQ(total_stock_value(), 50, "5+40+2+3");
    CHECK_EQ(most_valuable(), std::string("steel sword"), "best-so-far finds it");
    return dt_summary();
}
