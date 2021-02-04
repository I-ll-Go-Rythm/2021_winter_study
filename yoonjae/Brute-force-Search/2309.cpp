#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	vector<int> v(9);
	int sum = 0, diff = 0;
	for(int i=0; i<9; i++) {
		cin >> v[i];
		sum += v[i];
	}
	diff = sum - 100;

	for(int i=0; i<9; i++) {
		for(int j=i+1; j<9; j++) {
			if(v[i]+v[j] == diff) {
				v.erase(v.begin() + max(i, j));
				v.erase(v.begin() + min(i, j));
			}
		}
	}

	sort(v.begin(), v.end());
	for(int i=0; i<v.size(); i++) {
		cout << v[i] << endl;
	}

	return 0;
}
