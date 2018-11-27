#include <bits/stdc++.h>
using namespace std;

string ltrim(const string &);
string rtrim(const string &);


string dayOfProgrammer(int year) {
    int leap=0;
    if(year%4==0) leap++;
    int day=256-(31+(28+leap)+31+30+31+30+31+31);
    string date = to_string(day);
    string dia=to_string(day);
    string month=to_string(9); 
    string anno=to_string(year);       
    return date+".0"+month+"."+anno;
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
