//#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;
int room, N;

bool cmp(int *a, int *b) {
    if(a[1] == b[1]) return a[0] < b[0];
    else return a[1] < b[1];
}

void solve(int **arr, int idx) {
    int curr = arr[idx][0];
    room++;
    for(int i = idx+1; i < N; i++) {
        if(arr[i][0]<curr) {solve(arr, i); continue;}
        curr = arr[i][1];
    }
}

int main(void) { // try solving this prob with vector
    scanf("%d", &N);
    //cin >> N;

    int **arr = new int*[N];
    for(int i = 0; i < N; i++) {
        arr[i] = new int[2];
        scanf("%d %d", &(arr[i][0]), &(arr[i][1]));
        //cin >> arr[i][0] >> arr[i][1];
    }

    sort(arr, arr+N, cmp);
    
    solve(arr, 0);
    
    for(int i = 0; i < N; i ++)
        delete arr[i];
    delete arr;

    printf("%d\n", room);
    //cout << room << endl;

    return 0;
}
