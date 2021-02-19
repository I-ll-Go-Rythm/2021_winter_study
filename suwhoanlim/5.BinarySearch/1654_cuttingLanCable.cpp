#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;
typedef long long ll;
//mid = current length
int main(void) {
    int N, K;
    cin >> K >> N;
    ll *arr = new ll[K];
    //int min = -1, max = INT_MAX;
    for(int i = 0; i < K; i++) {
        cin >> arr[i];
        //min = min > arr[i] ? arr[i] : min;
        //max = max > arr[i] ? max : arr[i];
    }
    /*
    if(K == N) {
        if(min >= (max/2)) {cout << min << '\n'; return 0;}
        else {cout << max/2 << '\n'; return 0;}
    }
    */
    // case of K < N
    // ERROR FOUND! hi = INT_MAX will cause a failure
    // >> a given lan cable may be longer than INT_MAX
    // I assume there are some test cases where a given lan cable length == INT_MAX
    ll hi = LLONG_MAX, lo = 0, mid, cnt;
    //mid = curr length
    while(lo + 1 < hi) {
        mid = (hi+lo)/2;
        cnt = 0;
        for(int i = 0; i < K; i++)
            cnt += arr[i] / mid;

        if(cnt < N) hi = mid;
        else lo = mid;
        //printf("%d %d %d %d\n", lo, mid, hi, cnt);
    }
    
    cout << lo << '\n';
    delete arr;
    return 0;
}
