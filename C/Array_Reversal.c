#include <stdio.h>

int main(){
    
    int num, *arr, i;
    scanf("%d", &num);
    arr = (int*) malloc(num * sizeof(int));
    for(i = 0; i < num; i++) 
        scanf("%d", arr + i);
    
    int l = num - 1;
    int aux;
    for (int i=l; i>=num/2; i--) {
        aux = *(arr+i);
        *(arr+i) = *(arr+l-i);
        *(arr+l-i) = aux;
    }
      
    for(i = 0; i < num; i++)
        printf("%d ", *(arr + i));
    return 0;
}
