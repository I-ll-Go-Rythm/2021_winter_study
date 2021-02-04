#include <iostream>
#include <vector>
using namespace std;
int tot, S, cnt;

void rec(vector<int> ar, int idx, int cur) {
    int sum = 0;
    if(idx < tot) {
        rec(ar, idx+1, cur);
        ar[idx] = 100001; // out of bound
        rec(ar, idx+1, cur-1);
    } // idx == tot
    else {
        if(cur == 0) return; // empty subgroup
        for(int i = 0; i < tot; i++)
            if(ar[i] != 100001) sum += ar[i];
        if(sum == S) cnt++;
    }
}

int main(void) {
    int tmp;
    vector<int> arr;
    cin >> tot >> S;
    
    for(int i = 0; i < tot; i++){
        cin >> tmp;
        arr.push_back(tmp);
    }
    
    rec(arr, 0, tot);
    cout << cnt << endl;
    
    return 0;
}
