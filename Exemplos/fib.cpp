#include <iostream>
#include <string>
using namespace std;

int fib() {
    int n = 10;
    int a = 0;
    int b = 1;
    cout << "Fib de ";
    cout << n;
    cout << "\n";
    cout << a;
    cout << " ";
    cout << b;
    while (n > 2.0){
        int c = (a + b);
        cout << c;
        cout << " ";
        a = b;
        b = c;
        n = (n - 1.0);
    }
    return 0.0;
}

int main(){
    fib();
    return 0;
}