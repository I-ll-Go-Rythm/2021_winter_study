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

	int count = 0, room = 0, first = 0, second = 0;
	vector<pair<int, int> >::iterator it = v.begin();
	do {
		while(it != v.end()) {
			if(it->first >= second) {
				first = it->first;
				second = it->second;
				v.erase(it);
			}
			else ++it;
		}
		first = 0; second = 0;
		it = v.begin();
		++room;		
	} while(v.size() > 0);

	cout << room << endl;

	return 0;
}





	
