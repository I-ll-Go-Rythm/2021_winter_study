// divide n conqure
// greedy / brute force << belongs
// need to learn more about string STL

// https://sooooooyn.tistory.com/12
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main(void) {
    int N;
    string S;
    cin >> S;
    cin >> N;
    string A[101];
    //string *A = new string[N];
    for(int i = 0; i < N; i++)
        cin >> A[i];
    bool *dp = new bool[S.size()+1];
    dp[S.size()] = 1;
    
    for(int i = S.size() -1; i >= 0; i--) {
        for(int j = 0; j < N; j++) {
            //check from the back of the string
            if(S.find(A[j], i) == i && dp[i + A[j].size()] == 1) {dp[i] = 1; break;}
            //if(S.compare(i, A[j].length(), A[j]) == 0 && dp[i + A[j].size()] == 1) dp[i] = 1;
            else dp[i] = 0;
        }
    }
    
    cout << dp[0] <<'\n';
    delete dp;
    //delete A; // why munmap_chunk(): invalid pointer error??
    return 0;
}
