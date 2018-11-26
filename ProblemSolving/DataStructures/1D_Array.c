#include <stdio.h>

int main() {
    int v,i,r=0;
    scanf("%d",&v);
    int *arr = (int*)malloc(v * sizeof(int));
    for (i=0;i<v;i++){
        scanf("%d",&arr[i]);
        r+= arr[i];
    }
    printf("%d",r);
    free(arr);
    return 0;
}
