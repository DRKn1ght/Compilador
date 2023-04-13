#include <iostream>
#include <string>
using namespace std;

int fibonacci_helper(int n, int a, int b);
int fibonacci(int n);
int start();
int fibonacci_helper(int n, int a, int b) {
    if (n == 0.0){
        return 0.0;
    }
    cout << a;
    cout << " - ";
    fibonacci_helper((n - 1.0), b, (a + b));
    return 0.0;
}
int fibonacci(int n) {
    fibonacci_helper(n, 0.0, 1.0);
    cout << "\n";
    return 0.0;
}
int start() {
    int n = 10;
    fibonacci(n);
    return 0.0;
}

int main(){
    start();
    return 0;
}
