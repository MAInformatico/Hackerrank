#include <stdio.h>

int main(){
    int n;
    scanf("%d", &n);
  	    int max = n*2 - 1; //total distance
        for(int i=0;i<max;i++){
            for(int j=0;j<max;j++){
                int min = i < j ? i : j;
                min = min < max-i ? min : max-i-1;
                min = min < max-j-1 ? min : max-j-1;
                printf("%d ", n-min);
            }
            printf("\n");
        }
    return 0;
}
