#include <iostream>
#include <string>
using namespace std;

int fatorial(int n);
int start();
int fatorial(int n) {
    int result = 1;
    int i = 1;
    while (i <= n){
        result = (result * i);
        i = (i + 1.0);
    }
    cout << result;
    return result;
}
int start() {
    cout << "O fatorial de 10 é: ";
    fatorial(10.0);
    return 0.0;
}

int main(){
    start();
    return 0;
}
