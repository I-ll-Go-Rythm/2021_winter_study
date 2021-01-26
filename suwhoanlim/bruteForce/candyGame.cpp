#include <stdio.h>
#include <iostream>
using namespace std;
int maximum;
int row;

void search(char DD, char**arr) {
    int cnt = 0;
    for(int i = 0; i < row; i++) {
        for(int j = 0; j < row; j++) {
            if(arr[i][j] == DD) cnt++;
            else {
                maximum = cnt > maximum ? cnt : maximum;
                cnt = 0;
            }
        }
        maximum = cnt > maximum ? cnt : maximum;
        cnt = 0;
    }

    for(int i = 0; i < row; i++) {
        for(int j = 0; j < row; j++) {
            if(arr[j][i] == DD) cnt++;
            else {
                maximum = cnt > maximum ? cnt : maximum;
                cnt = 0;
            }
        }
        maximum = cnt > maximum ? cnt : maximum;
        cnt = 0;
    }
}

void swap(char CC, char** arr) {
    for(int i = 0; i < row; i++) {
        for(int j = 0; j < row-1; j++) {
            if(arr[i][j] != arr[i][j+1]) {
                char tmp = arr[i][j+1];
                arr[i][j+1] = arr[i][j];
                arr[i][j] = tmp;
                search(CC, arr);
            }   
            else
                continue;
            char tmp = arr[i][j+1];
            arr[i][j+1] = arr[i][j];
            arr[i][j] = tmp;    
        }   
    }   
    
    for(int j = 0; j < row; j++) {
        for(int i = 0; i < row-1; i++) {
            if(arr[i][j] != arr[i+1][j]) {
                char tmp = arr[i+1][j];
                arr[i+1][j] = arr[i][j];
                arr[i][j] = tmp;
                search(CC, arr);
            }   
            else
                continue;
            char tmp = arr[i+1][j];
            arr[i+1][j] = arr[i][j];
            arr[i][j] = tmp;
        }   
    }   
}

int main(void) {
    char **arr;
    scanf("%d", &row);
    
    arr = new char*[row];
    for(int i = 0; i < row; i ++)
        arr[i] = new char[row];
    
    
    for(int i = 0; i < row; i++)
        for(int j = 0; j < row; j++)
            cin >> arr[i][j];
            //scanf("%c", &arr[i][j]);
    
    for(int i = 0; i < 4; i++) {
        switch (i) {
            case 0: swap('Y', arr); break;
            case 1: swap('C', arr); break;
            case 2: swap('Z', arr); break;
            case 3: swap('P', arr); break;    
        }
    }
    
    printf("%d\n", maximum);
    
    return 0;
    
}   
