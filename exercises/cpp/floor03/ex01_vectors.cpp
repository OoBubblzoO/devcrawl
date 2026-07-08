// FLOOR C3 · EXERCISE c3-1 — std::vector
// Lesson: c3.1
//
// The C++ inventory. Like a Python list, but every element is the same
// type, declared up front: std::vector<std::string>.
// Note the & on parameters — pass by reference, modify the real thing.
//
// Run:  python3 dojo.py check c3-1
// Save: python3 dojo.py done c3-1

#include <string>
#include <vector>
#include <algorithm>   // std::find

// Add to the END:  inv.push_back(item)
void add_item(std::vector<std::string>& inv, std::string item) {
    // TODO
}

// Remove the FIRST match if present; missing items are a safe no-op.
// The C++ incantation:
//   auto it = std::find(inv.begin(), inv.end(), item);
//   if (it != inv.end()) inv.erase(it);
void drop_item(std::vector<std::string>& inv, std::string item) {
    // TODO
}

// Is it in there? std::find + compare against end().
bool has_item(const std::vector<std::string>& inv, std::string item) {
    // TODO
    return false;
}

// Most recently added, or "" for empty. inv.back() on an EMPTY vector is
// undefined behavior — C++ won't even crash politely. Guard with .empty().
std::string newest_item(const std::vector<std::string>& inv) {
    // TODO
    return "?";
}
