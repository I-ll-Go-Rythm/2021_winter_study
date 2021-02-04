#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, L, Count = 0;
vector<double> water;

int main() {
	cin >> N >> L;
	for(int i=0; i<N; i++) {
		int input;
		cin >> input;
		water.push_back(input);
	}

	sort(water.begin(), water.end());
	
	double start = 0;
	for(int i=0; i<N; i++) {
		if(start >= water[i] + 0.5)
			continue;
		else {
			start = max(water[i] - 0.5, start) + L;
			++Count;
//			cout << "Count is " << Count << ", start is " << start << endl;
		}
	}

	cout << Count << endl;

	return 0;
}

