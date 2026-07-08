// FLOOR C3 · EXERCISE c3-3 — Iteration patterns
// Lesson: c3.3 & c3.4
//
// The same three patterns from the Python wing — transform, count,
// best-so-far — plus C++'s sort-then-trim in place of slices.
//
// Run:  python3 dojo.py check c3-3
// Save: python3 dojo.py done c3-3

#include <string>
#include <vector>
#include <map>
#include <algorithm>   // std::sort

// Three highest, highest first. No slices in C++: sort a COPY descending
// (std::sort(v.begin(), v.end(), std::greater<int>())), then v.resize(3)
// — but only if it has more than 3!
std::vector<int> top_three(std::vector<int> scores) {   // note: already a copy
    // TODO
    return {};
}

// Last n log entries, oldest of those first.
// Hint: while (log.size() > (size_t)n) log.erase(log.begin());
std::vector<std::string> recent_log(std::vector<std::string> log, int n) {
    // TODO
    return {};
}

// Count each rarity. Here the [] "trap" becomes a FEATURE:
// counts[r]++ inserts 0 on first sight, then increments. One line.
std::map<std::string, int> count_rarities(const std::vector<std::string>& items) {
    // TODO
    return {};
}

// Every second tile starting from the first — index loop with i += 2.
std::vector<std::string> every_other_tile(const std::vector<std::string>& tiles) {
    // TODO
    return {};
}
