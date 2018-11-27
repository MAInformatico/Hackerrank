#include <bits/stdc++.h>
using namespace std;

string ltrim(const string &);
string rtrim(const string &);


string dayOfProgrammer(int year) {
    const int firstdays = 215;
    int leap=0;
    if (year<1918)
      leap=year%4 ? 28 : 29;
    else if (year>1918)
      leap=!(year%400) || year%100&&!(year % 4) ? 29 : 28;
    else
      leap=15;
    leap=256-(leap + firstdays);
    return to_string(leap)+".09."+to_string(year);
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string year_temp;
    getline(cin, year_temp);

    int year = stoi(ltrim(rtrim(year_temp)));

    string result = dayOfProgrammer(year);

    fout << result << "\n";

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
