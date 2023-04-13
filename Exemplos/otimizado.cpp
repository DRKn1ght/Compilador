#include <iostream>
#include <string>
using namespace std;

int optimize() {
    int a = 4187.0;
    int b = (14 + (3 * a));
    if (a > 1563.0){
        cout << "é maior";
        return a;
    }
    cout << "é menor";
    return ((a + 129.0) + 3.0);
}

int main(){
    optimize();
    return 0;
}
