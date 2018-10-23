#include <iostream>
#include <deque> 
using namespace std;

int findMax(deque<int> data){
    
    int maxValue = data[0];
    for (int i=0; i<data.size(); i++){
        if(maxValue<data[i]){
            maxValue = data[i];
        }
    }
    return maxValue;
}

void printKMax(int arr[], int n, int k){
    deque<int> data;
    int aux;
    for (int i=0; i < k; i++){
        data.push_back(arr[i]);        
    }
    aux=findMax(data);
    cout << aux<< " ";
    for(int i=0; i<n-k; i++){
        if(aux!= data.front() && aux > arr[i+k]){
            cout << aux << " ";
            data.pop_front();
            data.push_back(arr[i+k]);
        }
        else if(aux!= data.front() && aux < arr[i+k]){
            aux = arr[i+k];
            cout << aux << " ";
            data.pop_front();
            data.push_back(arr[i+k]);
        }
        else{
            data.pop_front();
            data.push_back(arr[i+k]);
            aux =  findMax(data);
            cout << aux << " ";
        }
    }
    cout << endl;
}

int main(){
  
	int t;
	cin >> t;
	while(t>0) {
		int n,k;
    	cin >> n >> k;
    	int i;
    	int arr[n];
    	for(i=0;i<n;i++)
      		cin >> arr[i];
    	printKMax(arr, n, k);
    	t--;
  	}
  	return 0;
}
