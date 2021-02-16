#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;

ll solve(int start, int end, vector<int> const &arr) {
    if(start == end) {
		cout << "base case" << endl;
		return arr[start];
	}
    
    int mid = (start + end) / 2;
    ll maxval = (solve(start, mid, arr), solve(mid + 1, end, arr));
    
    int left = mid, right = mid + 1;
    ll cnt = 2;
    int minval = min(arr[left], arr[right]);
    maxval = max(maxval, minval * cnt);
    
    while(!(start == left && right == end)) { //start < left || right < end) {
		cout << "In While" << endl;
        if(right < end && (start == left || arr[left - 1] < arr[right + 1])) {
            ++right; ++cnt;
            minval = min(minval, arr[right]);
        }
        else {
            --left; ++cnt;
            minval = min(minval, arr[left]);
        }
		cout << "count is " << cnt << " min val " << minval << endl;
        maxval = max(maxval, minval * cnt);
		cout << "max val is " << maxval << endl;
    }
    return maxval;
}

int main(void) {
    int N;
    cin >> N;
    vector<int> arr(N);
    
    for(int i = 0; i < N; i++) 
        cin >> arr[i];
    
    cout << solve(0, N-1, arr) << '\n';
    
    return 0;
}
