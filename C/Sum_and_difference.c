#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
	int a,b,r,r2;
    float c,d,v,v2;
    scanf("%d %d", &a, &b);
    scanf("%f %f", &c, &d);
    r=a+b;
    r2=a-b;
    printf("%d %d\n",r,r2);
    v=c+d;
    v2=c-d;
    printf("%2.1f %2.1f\n",v,v2);
    return 0;
}
