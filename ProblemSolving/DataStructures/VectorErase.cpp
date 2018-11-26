#include <vector>
#include <iostream>
using namespace std;

int main() {
    int n,pos,v,v1,v2;
    cin >> n;
    vector<int> data;
    for(int i=0; i<n;i++){
        cin >> v;
        data.push_back(v);
    }
    cin >> pos;
    data.erase(data.begin()+pos-1);
    cin >>v1 >> v2;
    data.erase(data.begin()+v1-1,data.begin()+v2-1);
    cout << data.size() << endl;
    for(int j=0; j<data.size();j++)
        cout << data[j] << " "; 
    
    return 0;
}
