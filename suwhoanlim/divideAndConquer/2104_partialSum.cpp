// https://yangorithm.tistory.com/51
// https://devbelly.tistory.com/61
// https://t-anb.tistory.com/15

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;

ll solve(int start, int end, vector<int> const &arr) {
    if(start == end) return (ll) arr[start] * arr[start];
    
    int mid = (start+end)/2; // use lower one
    ll maxval = max(solve(start, mid, arr), solve(mid+1, end, arr));
    
    int left = mid, right = mid+1;
    int minval = min(arr[left], arr[right]);
    ll interSum = arr[left] + arr[right];
    maxval = max(maxval, interSum * minval);
    
    while(start < left || right < end) {
        if(right < end && (start == left || arr[left - 1] < arr[right + 1])) {
	    // why would we need (arr[left - 1] < arr[right + 1])?
            // might be a good challenge to think about
            // hint: thie while loop won't check every single possible combination of the subsets
            interSum += arr[++right];
            minval = min(minval, arr[right]);
        }
        else {
            interSum += arr[--left];
            minval = min(minval, arr[left]);
        }
        maxval = max(maxval, interSum*minval);
    }
    
    return maxval;
}


int main(void) {
    int N;
    ll sol;
    cin >> N;
    vector<int> arr(N);
    for(int i = 0; i < N; i ++)
        cin >> arr[i];
    
    sol = solve(0, N - 1, arr);
    
    cout << sol << '\n';
    
    return 0;    
}
