#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
typedef long long ll;

int K, N;
vector<ll> v;

int main() {
	cin >> K >> N;

	ll input, mx = 0;
	for(int i=0; i<K; i++) {
		cin >> input;
		v.push_back(input);
		mx = max(mx, input);
	}

//	cout << mx << endl;
	
	ll lo = 1, hi = mx;
	while(lo < hi) {
		ll cnt = 0;
		int mid = (lo+hi+1)/2;
		for(int i=0; i<K; i++) {
			ll q = v[i] / mid;
			cnt += q;
			if(cnt >= N) break;
		}

//		cout << "lo is " << lo << ", hi is " << hi << ", cnt is " << cnt << endl;

		if(cnt < N) hi = mid-1;
		else lo = mid;
	}

	cout << lo << endl;

	return 0;
}




