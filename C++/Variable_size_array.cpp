#include <vector>
#include <iostream>
using namespace std;


int main() {
    int n,q; 
    cin >> n >> q;
	vector<vector<int>> data(n);

	for (int i = 0; i < n; i++) {
		int k;
		cin >> k;
		data[i].resize(k);
		for (int j = 0; j < k; j++) {
			cin >> data[i][j];
		}
	}

	for (int j = 0; j < q; j++) {
		int i, k;
		cin >> i >> k;
		cout << data[i][k] << endl;
	}

    return 0;
}
