#include <bits/stdc++.h>

using namespace std;

int main()
{
  int n, k, q;
  cin >> n >> k >> q;
  int a[n];
  for (int i=0; i<n; i++)
    cin >> a[i];

  int dest= k%n;
  int b[n];
  for (int i=0; i<n; i++) {
    b[dest++]=a[i];
    if (dest==n)
      dest= 0;
  }

  for (int i=0; i<q; i++) {
    int m;
    cin >> m;
    cout << b[m] << endl;
  }
}
