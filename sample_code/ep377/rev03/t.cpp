#include <iostream>

int main() {
    // for (int i = 0; i < 10; i += 1) {
    //     std::cout << "got " << i << std::endl;
    // }
    {
        int i = 0;
        while (i < 10) {
            std::cout << "got " << i << std::endl;

            i += 1;
        }
    }
}
