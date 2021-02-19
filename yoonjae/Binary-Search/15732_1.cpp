#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>

using namespace std;
/*
struct cmp {
	bool operator()(int a, int b) {
		return a < b;
	}
};
*/

int N, K, D;

int main() {
	cin >> N >> K >> D;

//	priority_queue<int, vector<int>, cmp> pq;
	vector<int> v;

	int i1, i2, i3;
	for(int i=0; i<K; i++) {
		cin >> i1 >> i2 >> i3;
		for(int j=i1; j<=i2; j+=i3) {
			v.push_back(j);
		}
	}

//	cout << "vsize is " << v.size() << endl;

	sort(v.begin(), v.end());
	v.erase(v.begin()+D, v.end());
//	cout << "vsize is " << v.size() << endl;

	cout << v.back() << endl;

	return 0;
}



