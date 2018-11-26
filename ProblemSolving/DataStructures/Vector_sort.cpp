#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    vector<int>data;
    int n, v;
    cin >> n;
    
    while (cin >> v) 
        data.push_back(v);
 
    sort(data.begin(), data.end());
    
    for(int i=0; i<n; i++)
        cout << data[i] << " ";
    
    return 0;
}
