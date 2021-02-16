#include <iostream>

using namespace std;
typedef long long ll;

int N;
ll u_atk;

int main() {
	cin >> N;
	cin >> u_atk;

	int t, a, h;
	ll lo = 0, hi = LLONG_MAX;
	while(lo < hi) {
		bool surv = true;
		ll mid = (lo+hi+1)/2, u_hp = mid;

		for(int i=0; i<N; i++) {
			cin >> t >> a >> h;
			if(t == 1) {
				while(true) {			
					h -= u_atk;
					if(h <= 0) break;
					u_hp -= a;
					if(u_hp <= 0) {
						surv = false;
						break;
					}
				}
			}
			else if(t == 2) {
				u_hp += h;
				u_atk += a;
			}

			if(surv) lo = mid;
			else if(!surv) hi = mid-1;
		}
	}

	cout << lo << endl;

	return 0;
}

