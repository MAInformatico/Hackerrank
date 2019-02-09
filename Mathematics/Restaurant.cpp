#include <iostream>
using namespace std;

int main() {
    int T,l,b,n,temp;
    cin >> T;
    int max=1000000;
    for(int i=0 ; i<T ; i++){        
        cin >> l >> b;
        for(int j=1; j<=l; j++){
            if(l%j==0 && b%j==0){
                n=(l*b)/(j*j);
                if(n<max) max=n;
            }
        }
        cout << max << endl; 
        max=1000000;
    } 
    return 0;
}
