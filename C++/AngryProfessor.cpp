#include <bits/stdc++.h>
using namespace std;

string angryProfessor(int k, vector <int> a) {
    string result="YES";
    int count=0;
    for(int i=0; i<a.size();i++) if(a[i]<=0) count++;
    
    if(count>=k) result="NO";
return result;
}

int main() {
    int t;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        int n, k;
        cin >> n >> k;
        vector<int> a(n);
        for(int a_i = 0; a_i < n; a_i++) cin >> a[a_i];
        
        string result = angryProfessor(k, a);
        cout << result << endl;
    }
    return 0;
}
