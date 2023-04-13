#include <iostream>
#include <string>
using namespace std;

int mdc(int a, int b);
int start();
int mdc(int a, int b) {
    while (a != b){
        if (a > b){
            a = (a - b);
        }
        if (a <= b){
            b = (b - a);
        }
    }
    cout << a;
    return 0.0;
}
int start() {
    cout << "MDC de 50 e 156:";
    cout << "\n";
    mdc(50.0, 156.0);
    return 0.0;
}

int main(){
    start();
    return 0;
}
