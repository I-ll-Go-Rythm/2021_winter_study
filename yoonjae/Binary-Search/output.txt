#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long ll;

int N, C;
vector<ll> v;


int main() {
	cin >> N >> C;
	ll input, mn=0, mx=0;
	for(int i=0; i<N; i++) {
		cin >> input;
		v.push_back(input);
		mn = min(mn, input);
		mx = max(mx, input);
	}

	sort(v.begin(), v.end());

	ll lo = 1, hi = ((mx-mn)/(C-1)) + 1;
	while(lo < hi) {
//		cout << "lo is " << lo << ", hi is " << hi << endl;
		ll mid = (lo+hi+1)/2;
		ll orgC = v[0];
		int cnt = 1;
		for(int i=1; i<N; i++) {
			if(v[i] - orgC >= mid) {
				++cnt;
				orgC = v[i];
			}
		}
		if(cnt >= C) lo = mid;
		else hi = mid-1;
	}
	cout << lo << endl;

	return 0;
}




