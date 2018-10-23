#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
   int n,v;
   cin >> n;
   vector<int> data;
   for (int i=0; i<n; i++){
       cin >> v;
       data.push_back(v);
   }
   int q, val;
   cin >> q;
   for (int i=0; i<q; i++){
       cin >> val;
       vector<int>::iterator low = lower_bound(data.begin(), data.end(), val);
       if (data[low - data.begin()] == val)
           cout << "Yes " << (low - data.begin()+1) << endl;
       else
           cout << "No " << (low - data.begin()+1) << endl;
   }
   return 0;
}
