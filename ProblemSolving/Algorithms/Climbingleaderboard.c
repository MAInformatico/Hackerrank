#include <stdio.h>
int n, m, currentScore, top, stack[200002];
int main() {
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        scanf("%d", &stack[top+1]);
        if (stack[top+1] != stack[top]) ++top;
    }
    scanf("%d", &m);
    for (int j = 0; j < m; ++j) {
        scanf("%d", &currentScore);
        while (top && currentScore >= stack[top]) --top;
        printf("%d\n", top+1);
    }
    return 0;
}
