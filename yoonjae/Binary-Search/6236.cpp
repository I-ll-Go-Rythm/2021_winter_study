#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;
typedef long long ll;

int N, M;
vector<int> v;
const int MAX = 100001;

int main() {
	cin >> N >> M;
	ll input;
	ll mn = 0, mx = 0;
	for(int i=0; i<N; i++) {
		cin >> input;
		v.push_back(input);
		mn = min(mn, input);
		mx += input;
	}

	ll lo = mn, hi = mx;
	while(lo < hi) {
		ll mid = (lo+hi)/2, sum = 0;

		int cnt = 1;
		for(int i=0; i<N; i++) {
			if(v[i] > mid) {
				cnt = MAX;
				break;
			}

			sum += v[i];
			if(sum > mid) {
				sum = v[i];
				++cnt;
			}
			if(cnt > M) break;
		}

		if(cnt > M) lo = mid+1;
		else hi = mid; // case of (cnt <= M)
	}

	cout << lo << endl;

	return 0;
}




