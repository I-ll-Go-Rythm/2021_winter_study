#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

bool cmp (pair<int, int> a, pair<int, int> b) {
    if(a.second == b.second) return a.first > b.first;
    return a.second > b.second;
}

int main(void) {
    int N, newday, result = 0, maxday = 0, maxp = 0, j = 1;
    cin >> N;
    
    vector<pair<int, int>> hw(N);
    for(int i = 0; i < N; i++) {
        cin >> hw[i].first >> hw[i].second;
        maxday = maxday < hw[i].first ? hw[i].first : maxday;
    }
    int *arr = new int[N+1];
    for(int i = 0; i < N+1; i++) arr[i] = 0;
    
    sort(hw.begin(), hw.end(), cmp);
    
    for(int i = 0; i < N; i++) {
        for(int k = hw[i].first; k>0; k--) 
            if(arr[k] == 0) {
                result += hw[i].second;
                maxp++;
                arr[k] = 1;
                break;
            }    
            if(maxp == maxday) break;
    }
    
    cout << result << '\n';
    
    return 0;
}
