#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
    int N, maxi = 0;
    cin >> N;
    int *arr = new int[N];
    int *ans = new int[N];
    for(int i = 0; i < N; i++) {
        cin >> arr[i];
        ans[i] = arr[i];
    }
    for(int i = N-1; i >= 0; i--) {
        int tmp = arr[i];
        for(int j = i+1; j < N; j++) {
            if(tmp < arr[j]) {
                ans[i] = max(ans[i], tmp + ans[j]);
            }
        }
        maxi = max(maxi, ans[i]);
    }
    cout << maxi << '\n';
    //cout << ans[0] << '\m';
    //above may not be always the answer
    delete arr;
    delete ans;
    return 0;
}
