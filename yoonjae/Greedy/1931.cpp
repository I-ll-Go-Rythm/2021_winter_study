#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
vector<pair<int, int> > v;

bool compare(pair<int, int>& a, pair<int, int>& b) {
	if(a.second == b.second) return a.first < b.first;
	else return a.second < b.second;
}

int main() {
	cin >> N;
	int input1, input2;
	for(int i=0; i<N; i++) {
		cin >> input1 >> input2;
		v.push_back(make_pair(input1, input2));
	}

	sort(v.begin(), v.end(), compare);

	int count = 1;
	int first = v[0].first, second = v[0].second;
	for(int i=1; i<N; i++) {
		if(v[i].first >= second) {
			first = v[i].first;
			second = v[i].second;
			++count;
		}
	}

	cout << count << endl;

	return 0;
}





	
