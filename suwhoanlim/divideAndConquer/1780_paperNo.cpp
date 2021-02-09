#include <iostream>
#include <vector>
#include <array>
using namespace std;
int nzo[3] = {0, 0, 0}; //noz, non, noo; //no. zero, no. negative, no. one

void solve(int stx, int sty, int N, int **arr) {
    int out = 0;
    int init = arr[sty][stx];
    if(N == 1) {nzo[init + 1]++; return;}
    for(int i = sty; i < sty + N; i++) {
        for(int j = stx; j < stx + N; j++)
            if(init != arr[i][j]) {out = 1; break;}
        if(out == 1) break;
    }
    if(out == 0) {nzo[init + 1]++; return;}
    else{
        int trix = N / 3;
        for(int i = 0; i < 3; i++)
            for(int j = 0; j < 3; j++) 
                solve(stx + trix * j, sty + trix * i, trix, arr);
                //solve(stx * (1+stx/3*j), sty * (1+stx/3*i), endx * (1+endx/3*(j+1)), endy * (1+stx/3*(i+1)));
    }
    return;
    //if diff no exit, return slve
    // else count 0 or 1 or -1, increase the count, return null;
}

int main(void) {
    int N;
    cin >> N;
    int **arr = new int*[N];
    for(int i = 0; i < N; i++)
        arr[i] = new int[N];
    
    for(int i = 0; i < N; i++)
        for(int j = 0; j < N; j++) 
            cin >> arr[i][j];
    
    solve(0,0,N, arr);
    
    cout << nzo[0] << '\n' << nzo[1] << '\n' << nzo[2] << '\n';
    
    for(int i = 0; i < N; i++)
        delete arr[i];
    delete arr;
    return 0;
    
}
