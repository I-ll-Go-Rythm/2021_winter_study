#include <iostream>
#include <vector>

using namespace std;
typedef long long ll;

int N, M;
ll MAX;
vector<ll> v;

int main() {
	cin >> N >> M;
	ll input;
	for(int i=0; i<N; i++) {
		cin >> input;
		v.push_back(input);
		MAX += input;
	}

	ll mn = 0, mx = MAX;
	while(mn < mx) {
//		cout << "in while" << endl;
		ll mid = (mn+mx)/2;
		int cnt = 0;
		ll temp = 0;
		for(int i=0; i<N; i++) {
			if(v[i] > mid) {
				cnt = M;
				break;
			}
			temp += v[i];
			if(temp > mid) {
				++cnt;
				temp = v[i];
			}
			if(cnt >= M) break;
		}
		if(temp > mid) ++cnt;

		if(cnt < M) mx = mid;
		else mn = mid+1;
	}

	cout << mn << endl;

	return 0;
}




