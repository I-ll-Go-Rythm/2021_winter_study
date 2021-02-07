#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main(void) {
    int row;
    char tmp;
    char candy[] = {'C', 'P', 'Z', 'Y'};
    char *col;
    scanf("%d", &row);
    char **arr;
    arr = (char**)malloc(sizeof(char*) * row);
    for(int j = 0; j < row; j++) {
        for(int i = 0; i < row; i++) {
            col = (char*)malloc(sizeof(char) * row);
            scanf("%c", &col[i]);
        }
        arr[j] = col;
    } // formation of the map
    
    for(int j = 0; j < row; j++) {
        for(int i = 0; i < row; i ++) {
            printf("%c ", arr[j][i]);    
        }
        printf("\n");
            
        }
    
    return 0;
    
}
