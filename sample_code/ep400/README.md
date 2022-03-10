# [what is inlining? and how does it make code faster? (intermediate)](https://youtu.be/ct-eBvjsPck)

Today I introduce the concept of "inlining" and how an optimizing compiler can use it to make code faster!

## Interactive examples

### C++

Godbolt examples:

```cpp
#include <iostream>

int add(int x, int y) {
    return x + y;
}

int main() {
    std::cout << add(1, 2) << std::endl;
}
```

```cpp
#include <iostream>

int add(int x, int y) {
    return x + y;
}

int main() {
    int x;
    std::cin >> x;
    std::cout << add(x, 2) << std::endl;
}
```

```cpp
#include <iostream>

inline int add(int x, int y) {
    return x + y;
}

int main() {
    int x;
    std::cin >> x;
    std::cout << add(x, 2) << std::endl;
}
```
