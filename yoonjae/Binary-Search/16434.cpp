#include <iostream>
#include <vector>
#include <climits>

using namespace std;
typedef long long ll;

typedef struct dungeon {
	ll t;
	ll a;
	ll h;

	dungeon(ll _t, ll _a, ll _h) {
		t = _t; a = _a; h = _h;
	}
} dg;

int N;
ll atk;
vector<dg> v;

int main() {
	cin >> N;
	cin >> atk;

	ll t, a, h;
	for(int i=0; i<N; i++) {
		cin >> t >> a >> h;
		v.push_back(dg(t,a,h));
	}

	ll lo = 1, hi = 1e18;
	while(lo < hi) {
//				cout << "lo is " << lo << ", hi is " << hi << endl;
		bool surv = true;
		ll mid = (lo+hi)/2, u_hp = mid, u_atk = atk;
//				cout << "mid is " << mid << endl;

		for(int i=0; i<N; i++) {
			ll _t = v[i].t; ll _a = v[i].a; ll _h = v[i].h;
//			cout << "t is " << t << endl;
//			cout << "a is " << a << endl;
//			cout << "monster hp is " << h << endl;
			//monster
			if(_t == 1) {
//				cout << "in Dungeon" << endl;
//				cout << "attak stat is " << atk << endl;
//				cout << "monster hp is " << h << endl;
				ll qM, qU;
				if(_h%u_atk == 0) qM = _h/u_atk;
				else qM = (_h/u_atk ) + 1;
				if(u_hp%_a == 0) qU = u_hp/_a;
				else qU = (u_hp/_a) + 1;
				if(qM <= qU) {// 몬스터 약해
					u_hp = u_hp - (qM-1)*_a;
				}
				else { // 몬스터 쎄
					surv = false;
					break;
				}
				/*
				while(true) {
					_h -= u_atk;
					if(_h <= 0) break;
					u_hp -= _a;
//					cout << " <- " << a << ", u_hp is " << u_hp << endl;
					if(u_hp <= 0) {
//						cout << "\t!!DEAD" << endl;
						surv = false;
						break;
					}
				}
				*/
			}

			//medicine
			else if(_t == 2) {
//				cout << "recovery" << endl;
				u_hp += _h;
				if(u_hp > mid) u_hp = mid;
				u_atk += _a;
			}

			if(!surv) break;
		}

		if(surv) hi = mid;
		else if(!surv) lo = mid+1;
	}

	cout << lo << endl;

	return 0;
}

