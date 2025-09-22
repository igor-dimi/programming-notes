#include <iostream>

template<typename T>
T mysum(T value)
{
    return value;
}

template<typename T, typename... Args>
T mysum(T first, Args... rest)
{
    return first + mysum(rest...);
}

int main(int argc, char const *argv[])
{
    std::cout << mysum(10, 20, 30) << "\n";
    std::cout << mysum(1, 2, 3, 4, 5) << "\n";
    return 0;
}

