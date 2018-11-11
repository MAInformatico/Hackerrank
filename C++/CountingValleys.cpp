#include <bits/stdc++.h>

using namespace std;

int countingValleys(int n, string s) {
    int result=0;
    int level=0;    //level over the sea
    for(int i=0; i<s.size();i++){    
        if(s[i]=='D') level--;
        if(s[i]=='U') level++;
        if(level==0 && s[i]=='U') result++;
    }
    return result;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string s;
    getline(cin, s);

    int result = countingValleys(n, s);

    fout << result << "\n";

    fout.close();

    return 0;
}
