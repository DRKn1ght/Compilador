#include <iostream>
#include <string>
using namespace std;

int power(int x, int n);
int start();
int power(int x, int n) {
    int result = 1;
    int i = 1;
    while (i <= n){
        result = (result * x);
        i = (i + 1.0);
    }
    cout << result;
    return result;
}
int start() {
    cout << "5^10 = ";
    power(5.0, 10.0);
    return 0.0;
}

int main(){
    start();
    return 0;
}
