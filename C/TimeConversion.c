#include <string.h>
#include <stdio.h>

int main() {
    int h, m, s ;
    char time[3];
    scanf("%d:%d:%d%s", &h, &m, &s, time) ;
        
    if (strcmp(time,"PM")==0 && h!=12) h += 12 ;
    if (strcmp(time,"AM")==0 && h==12) h = 0 ;
        
    printf("%02d:%02d:%02d", h, m, s) ;
    return 0;
}
