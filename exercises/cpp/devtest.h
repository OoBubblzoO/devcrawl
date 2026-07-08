// devtest.h — DEVCRAWL's tiny test harness for the C++ wing.
// No install, no framework: tests #include this, run CHECKs, return dt_summary().
// Read it! It's ~40 lines and demystifies what test frameworks actually do.
#pragma once
#include <iostream>
#include <string>
#include <sstream>

static int dt_checks = 0;
static int dt_failures = 0;

template <typename T>
std::string dt_str(const T& v) { std::ostringstream os; os << v; return os.str(); }
inline std::string dt_str(bool v) { return v ? "true" : "false"; }

#define CHECK(cond, msg) do { \
    dt_checks++; \
    if (!(cond)) { dt_failures++; \
        std::cout << "  FAIL  " << msg << "\n        check: " << #cond << "\n"; } \
} while (0)

#define CHECK_EQ(actual, expected, msg) do { \
    dt_checks++; \
    auto dt_a = (actual); auto dt_e = (expected); \
    if (!(dt_a == dt_e)) { dt_failures++; \
        std::cout << "  FAIL  " << msg \
                  << "\n        expected: " << dt_str(dt_e) \
                  << "\n        got:      " << dt_str(dt_a) << "\n"; } \
} while (0)

inline int dt_summary() {
    if (dt_failures == 0) {
        std::cout << "  all " << dt_checks << " checks green\n";
        return 0;
    }
    std::cout << "  " << dt_failures << "/" << dt_checks << " checks failing\n";
    return 1;
}
