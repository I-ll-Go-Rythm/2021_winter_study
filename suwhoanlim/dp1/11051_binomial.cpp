#include <iostream>
using namespace std;
typedef long long ll;

int solve(int N, int K, int** arr) {
    if(K == 0 || N == K) return 1;
    else if (K == 1 || K == N-1) return N;
    
    if(arr[N][K] != -1) return arr[N][K];
    
    arr[N][K] = (solve(N-1, K, arr) + solve(N-1, K-1, arr)) % 10007;
    //    arr[N][K] = solve(N-1, K, arr) % 10007 + solve(N-1, K-1, arr) % 10007;
    // The line above will give a false output. try test_11051.cpp in /suwhoanlim
    
    return arr[N][K];
}

int main(void) {
    int N, K;
    cin >> N >> K;
    int **arr = new int*[N+1];
    for(int i = 0; i < N+1; i++) {
        arr[i] = new int[N+1];
        for(int j = 0; j < N+1 ; j++)
            arr[i][j] = -1;
    }
    
    cout << solve(N, K, arr) << '\n';    
    
    for(int i = 0; i < N+1; i++)
        delete arr[i];
    delete arr;
    
    return 0;
}
