#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair<int, int>& a, pair<int, int>& b) {
	return a.first < b.first;
}

int main() {
	vector<pair<int, int> > v;
	for(int i=0; i<11; i++) {
		int f, s;
		cin >> f >> s;
		v.push_back(make_pair(f, s));
	}

	sort(v.begin(), v.end(), compare);

	int temp_D = 0, sum = 0;
	for(int i=0; i<11; i++) {
		temp_D += v[i].first;
		sum = sum + temp_D + 20*v[i].second;
	}

	cout << sum << endl;

	return 0;
}
	

