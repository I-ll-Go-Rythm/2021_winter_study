#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;

int N;
vector<ll> v;

ll get_surf(int s, int e) {
//	cout << "Start index, " << s << " | End index, " << e << endl;
	if(e-s == 1) {
//		cout << "Done, " << s << " , " << e << endl;
		return v[s];
	}

	int mid = (s+e-1)/2;

	ll L_sur = get_surf(s, mid+1);
//	cout << "L surface is " << L_sur << endl;
	ll R_sur = get_surf(mid+1, e);
//	cout << "R surface is " << R_sur << endl;
	ll res = max(L_sur, R_sur);

	int l = mid, r = mid;
	ll w = 2, h = v[mid], M_sur = 0;
	while(w <= e-s) {
		if(s<l && r<e-1) {
			if(v[l-1] > v[r+1]) {
				h = min(h, v[--l]);
				M_sur = max(M_sur, (ll) h*w);
			}
			else {
				h = min(h, v[++r]);
				M_sur = max(M_sur, (ll) h*w);
			}
		}
		else if(s==l && r<e-1) {
			h = min(h, v[++r]);
			M_sur = max(M_sur, (ll) h*w);
		}
		else if(s<l && r==e-1) {
			h = min(h, v[--l]);
			M_sur = max(M_sur, (ll) h*w);
		}
		++w;
	}
//	cout << "M surface is " << M_sur << endl;

//	cout << "Done, " << s << " , " << e << endl;
	return max(res, M_sur);
}


int main() {
	cin >> N;

	ll input;
	for(int i=0; i<N; i++) {
		cin >> input;
		v.push_back(input);
	}

	cout << get_surf(0, N) << endl;
}




