#include <stdio.h>
#include <math.h>

void update(int *a,int *b) {
    int aux;
    aux=*a-*b;
    *a=*a+*b;
    *b=abs(aux);
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
