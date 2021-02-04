#include <iostream>
using namespace std;

int main (void) {
    bool tmp, arr[51][51];
    char t;
    int M, N, cnt, cnt2;
    int p = 64;
    cin >> M >> N;
    
    for(int i = 0; i < M; i++) {
        for(int j = 0; j <N; j++) {
            cin >> t;
            if(t == 'W') arr[i][j] = 1;
            else arr[i][j] = 0;
        }
    }
    for(int i = 0; i < M-7; i++) {
        for(int j = 0; j < N-7; j++) {
            tmp = arr[i][j];
            cnt = 0;
            cnt2 = 0;
            for(int n = 0; n < 8; n++) {
                for(int m = 0; m < 8; m++) {
                    if(((n^m)&1)^tmp != arr[i+n][j+m]) cnt++;
                    else cnt2++; // if don't need to change in one side, need to change for the other side
                    //if(arr[i+n][j+m] == arr[i+n][j+m+1]) cnt ++;
                }
            }
            cnt = (cnt > cnt2 ? cnt2 : cnt);
            p = (p > cnt ? cnt : p);
        }
    }
    cout << p << endl;
    return 0;
}
