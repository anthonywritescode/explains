#include <iostream>

int main() {

    // 1. initialize
    // 2. check
    // 3. do work
    // 4. update

    int x; // initialize
    std::cin >> x; // initialize
    while (std::cin) { // check
        std::cout << "got x: " << x << std::endl; // do work

        std::cin >> x; // update
    }
}
