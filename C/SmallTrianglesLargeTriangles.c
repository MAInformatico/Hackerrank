#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;

int area(triangle t){
    int p=(t.a+t.b+t.c)/2;
    int area=sqrt(p*(p-t.a)*(p-t.b)*(p-t.c));
    return area;
}

void swap(triangle* a,triangle* b){
    triangle temp=*a;
    *a=*b;
    *b=temp;
}

void sort_by_area(triangle* tr, int n) {
    for(int i=0;i<n;i++){
        int swapped=0;
        for(int j=0;j<n-i-1;j++)
        {
            if(area(tr[j])>area(tr[j+1]))
             swap(&tr[j],&tr[j+1]);
            swapped=1;
        }
        if(swapped==0)
            break;
    }
}

int main(){
	int n;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}
