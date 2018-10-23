#include <cstdio>
#include <iostream>
#include <set>
using namespace std;


int main() {
    int q;
    int v1,v2=0;
    set<int> queries;
    cin >> q;
    for(int i=0; i<q;++i){
        cin >> v1 >> v2;
        if(v1==1){
            queries.insert(v2);
        }
        if(v1==2){
            queries.erase(v2);
        }
        if(v1==3){
            cout << (queries.find(v2) == queries.end() ? "No" : "Yes") << endl;
        }
    }
    return 0;
}
