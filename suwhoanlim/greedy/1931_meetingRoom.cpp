#include <iostream>
#include <algorithm>
using namespace std;
bool cmp(int *a, int *b) {
    if(a[1] == b[1]) return a[0] < b[0]; // need this line. Think about why we would need this!
    else return a[1] < b[1]; // sort increasing order of end time
}

int main(void) {
    int N, curr = 0, cnt = 0;
    cin >> N;
    int **arr = new int*[N];
    for(int i = 0; i < N; i++) {
        arr[i] = new int[2];
        cin >> arr[i][0] >> arr[i][1];
    }
    sort(arr, arr + N, cmp);
    
    for(int i = 0; i < N; i++) {
        if(arr[i][0] < curr) continue;
        curr = arr[i][1];
        cnt++;
    }
    
    cout << cnt << endl;
    
    for(int i = 0; i < N; i++)
        delete arr[i];
    delete arr;
    return 0;
}
