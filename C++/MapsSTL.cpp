#include <cstdio>
#include <iostream>
#include <map>
using namespace std;

int main() {
    int q, type;
    cin >> q; 
    map<string,int> student;
    string name;
    for (int i(0), result; i<q; ++i){
        cin >> type >> name;
        if (type == 1){
            cin >> result;
            student[name] += result;
        }
        else if (type == 2)
            student.erase(name);
        else
            cout << student[name] << "\n";
    }
    return 0;
}
