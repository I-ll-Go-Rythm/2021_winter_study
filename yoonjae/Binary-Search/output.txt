#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

typedef struct rule {
	int a;
	int b;
	int c;
	rule(int _a, int _b, int _c) {
		a = _a; b = _b; c = _c;
	}
} rl;

const int MAX = 1000000;
int N, K, D;
vector<rl> v;

int main() {
	cin >> N >> K >> D;

	int i1, i2, i3;
	for(int i=0; i<K; i++) {
		cin >> i1 >> i2 >> i3;
		v.push_back(rl(i1,i2,i3));
	}

	int lo = 1, hi = MAX;
	while(lo < hi) {
		int mid = (lo+hi)/2;

		int cnt = 0; bool check = true;
		for(int i=0; i<K; i++) {
			if(v[i].a > mid) continue;
			else if(v[i].b >= mid) cnt += ((mid-v[i].a)/v[i].c) + 1;
			else if(v[i].b < mid) cnt += ((v[i].b-v[i].a)/v[i].c) + 1;

			if(cnt >= D) {
				check = true;
				break;
			}
		}
		if(cnt < D) check = false;

		if(check) hi = mid;
		else lo = mid+1;
	}

	cout << lo << endl;
	return 0;
}


//		if(cnt > D) // 140 true
//		else if(cnt == D) //125 126 127 true
//		else if(cnt < D) // 110 false

