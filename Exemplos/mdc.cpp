#include <iostream>
#include <string>
using namespace std;

int mdc(int a, int b) {
    a = 50.0;
    b = 156.0;
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

int main(){
    mdc(0, 0);
    return 0;
}
