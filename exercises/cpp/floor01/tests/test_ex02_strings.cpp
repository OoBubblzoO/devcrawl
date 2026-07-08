#include "../../devtest.h"
#include "../ex02_strings.cpp"

int main() {
    CHECK_EQ(make_hud(), std::string("Crumb | HP 24/30 | Floor 2"), "HUD line");
    CHECK_EQ(shout("a wild rat approaches"), std::string("A WILD RAT APPROACHES"), "shout()");
    CHECK_EQ(damage_popup(7), std::string("You take 7 damage!"), "popup for 7");
    CHECK_EQ(damage_popup(12), std::string("You take 12 damage!"),
             "popup must use the parameter, not a hardcoded 7");
    return dt_summary();
}
