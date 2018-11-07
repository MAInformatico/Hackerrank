#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the gradingStudents function below.
 */
vector<int> gradingStudents(vector<int> grades) {
    vector<int> result;
    int v=0;
    for(int i=0; i<grades.size();i++){
        if(grades[i]>=38 && grades[i]<=100){
            v=grades[i]+1;
            if(v%5==0)
                result.push_back(v);
            
            else if((v+1)%5==0){
                v=grades[i]+2;
                result.push_back(v);
            }
            else
                result.push_back(grades[i]);                        
        }
        else
            result.push_back(grades[i]);
    }
    return result;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    vector<int> grades(n);

    for (int grades_itr = 0; grades_itr < n; grades_itr++) {
        int grades_item;
        cin >> grades_item;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        grades[grades_itr] = grades_item;
    }

    vector<int> result = gradingStudents(grades);

    for (int result_itr = 0; result_itr < result.size(); result_itr++) {
        fout << result[result_itr];

        if (result_itr != result.size() - 1) {
            fout << "\n";
        }
    }

    fout << "\n";

    fout.close();

    return 0;
}
