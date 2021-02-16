// https://ghdic.github.io/ps/boj-15732/
#include <iostream>
#include <algorithm>
using namespace std;

struct rule {
	int a, b, c;
};
int n, k, d;
rule principle[10000];

bool isShort(int last) {
	long long int cnt = 0;

	for (int i = 0; i < k; ++i) {
		if (last < principle[i].a)continue;
		int a = principle[i].a, b = min(principle[i].b, last);
		cnt += (b - a) / principle[i].c + 1;
	}
	return cnt < d;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	int l = 1, r = 0;
	cin >> n >> k >> d;
	for (int i = 0; i < k; ++i) {
		cin >> principle[i].a >> principle[i].b >> principle[i].c;
		r = max(r, principle[i].b);
	}

	while (l <= r) {
		int mid = (l + r) / 2;
		if (isShort(mid)) {
			l = mid + 1;
		}
		else {
			r = mid - 1;
		}
	}

	cout << l << endl;
	return 0;
}
