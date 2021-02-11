
// I was kinda afriad to see this q
// but turns out it was simpler than i thought
// https://chanhuiseok.github.io/posts/baek-10/ << better solution

#include <iostream>
#include <algorithm>
#include <math.h>
#include <climits>
using namespace std;

int solve(int N, int *dp) {
    if(N == 1) return 1;
    else if(N == 0) return 0;
    else if(dp[N] != INT_MAX) return dp[N];
    
    for(int i = 1; i*i <= N; i++) {
        dp[N] = min(solve(N-i*i, dp) + 1, dp[N]);
    }
    return dp[N];
}

int main(void) {
    int N;
    cin >> N;
    int *dp = new int[N+1];
    for(int i = 0; i < N+1; i++)
        dp[i] = INT_MAX;
    
    int max = solve(N,dp);
    
    cout << max << '\n';
    
    delete dp;
    return 0;
}
