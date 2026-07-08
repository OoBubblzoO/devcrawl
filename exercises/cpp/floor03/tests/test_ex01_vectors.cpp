#include "../../devtest.h"
#include "../ex01_vectors.cpp"

int main() {
    std::vector<std::string> inv = {"torch"};
    add_item(inv, "rope");
    CHECK_EQ(inv.size(), (size_t)2, "add_item appends");
    CHECK_EQ(inv[1], std::string("rope"), "…to the end");

    std::vector<std::string> inv2 = {"torch", "rope", "torch"};
    drop_item(inv2, "torch");
    CHECK_EQ(inv2.size(), (size_t)2, "drop removes ONE");
    CHECK_EQ(inv2[0], std::string("rope"), "…the first match");

    std::vector<std::string> inv3 = {"torch"};
    drop_item(inv3, "banana");
    CHECK_EQ(inv3.size(), (size_t)1, "dropping a missing item is a no-op, not a crash");

    CHECK_EQ(has_item({"torch", "rope"}, "rope"), true, "has rope");
    CHECK_EQ(has_item({}, "rope"), false, "empty has nothing");

    CHECK_EQ(newest_item({"torch", "rope"}), std::string("rope"), "newest is back()");
    CHECK_EQ(newest_item({}), std::string(""), "empty -> \"\" (guarded, no UB)");
    return dt_summary();
}
