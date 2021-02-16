#include <iostream>
#include <vector>

using namespace std;
typedef long long ll;

int N, M;
ll MAX = 0;
vector<ll> v;

ll b_search(ll mn, ll mx) {
	if(mn == mx) return mn;
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
		if(cnt >= M) {
			break;
		}
	}
//	cout << "mid is " << mid << ", cnt is " << cnt << endl;
//	return 0;
	if(cnt < M) return b_search(mn, mid);
	else return b_search(mid+1, mx);
}

int main() {
	cin >> N >> M;
	ll input;
	for(int i=0; i<N; i++) {
		cin >> input;
		v.push_back(input);
		MAX += input;
	}

	cout << b_search(0, MAX) << endl;

	return 0;
}




