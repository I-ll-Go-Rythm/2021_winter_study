// https://yeeybook.tistory.com/96
#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

int main() {
	long long L, N, Bessie, John;
	cin >> L >> N >> John >> Bessie;
    vector <pair<int, int>> v(N);
	for (int i = 0; i < N; n++) {
		cin >> v[i].first >> v[i].second;
        //cin >> x >> c;
		//v.push_back(make_pair(c, x));
	}
    
	sort(v.begin(), v.end(), greater<>());
	long long current = 0, res = 0;
	for (int i = 0; i < v.size(); i++) {
		if (current < v[i].second) {
			res += (John - Bessie) * (v[i].second - current) * v[i].first; // how long time * how high * how tasty
			current = v[i].second;
		}
	}
	cout << res;
	return 0;
}
