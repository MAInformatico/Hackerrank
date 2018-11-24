#include <bits/stdc++.h>

using namespace std;

int pageCount(int n, int p) {
    int n1=abs(p/2);
    if(n%2==0) n++;
    int n2=abs((p-n)/2);
    return n1 < n2 ? n1 : n2;        
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int p;
    cin >> p;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    int result = pageCount(n, p);

    fout << result << "\n";

    fout.close();

    return 0;
}
