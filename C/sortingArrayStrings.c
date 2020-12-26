#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define ALPHACHARS   26
int distinct_chars(const char *a)
{
    int dist = 0;
    int chars[ALPHACHARS] = {0};

    while (*a != '\0') {
        int chr = (*a++) - 'a';
        if (chr < ALPHACHARS)
            chars[chr]++;
    }
    
    for (int i = 0; i < ALPHACHARS; i++)
        if (chars[i])
            dist++;

    return dist;
}

int lexicographic_sort(const char* a, const char* b) {
    return strcmp(a, b);
}

int lexicographic_sort_reverse(const char* a, const char* b) {
    return strcmp(b, a);
}

int sort_by_number_of_distinct_characters(const char* a, const char* b) {
    int result = distinct_chars(a) - distinct_chars(b);
    return (result) ? result : lexicographic_sort(a, b);
}

int sort_by_length(const char* a, const char* b) {
    int result = strlen(a) - strlen(b);
    return (result) ? result : lexicographic_sort(a, b);
}

void string_sort(char** arr,const int len,int (*cmp_func)(const char* a, const char* b)){
    int sorted = 0;
    int num = len - 1;
    while (!sorted) {
        sorted = 1;
        for (int i = 0; i < num; i++) {
            if (cmp_func(arr[i], arr[i + 1]) > 0) {
                char *aux = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = aux;
                sorted = 0;
            }
        }
        num--;
    }
}


int main() 
{
    int n;
    scanf("%d", &n);
  
    char** arr;
	arr = (char**)malloc(n * sizeof(char*));
  
    for(int i = 0; i < n; i++){
        *(arr + i) = malloc(1024 * sizeof(char));
        scanf("%s", *(arr + i));
        *(arr + i) = realloc(*(arr + i), strlen(*(arr + i)) + 1);
    }
  
    string_sort(arr, n, lexicographic_sort);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);
    printf("\n");

    string_sort(arr, n, lexicographic_sort_reverse);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");

    string_sort(arr, n, sort_by_length);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);    
    printf("\n");

    string_sort(arr, n, sort_by_number_of_distinct_characters);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");
}
