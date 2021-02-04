#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, K;
int main() {
	cin >> N >> K;
	if(N == 1) {
		cout << 0 << endl;
		return 0;
	}
	vector<int> v;
	
	int input;
	for(int i=0; i<N; i++) {
		cin >> input;
		v.push_back(input);
	}
	sort(v.begin(), v.end());
	
	vector<int> distance;
	int diff;
	for(int i=0; i<N-1; i++) {
		diff = v[i+1] - v[i];
		distance.push_back(diff);
	}
	sort(distance.begin(), distance.end(), greater<int>());
	
//	cout << "size is " << distance.size() << endl;
	
	distance.erase(distance.begin(), distance.begin()+K-1);
	
//	cout << "size is " << distance.size() << endl;
	
	int ans = 0;
	for(int i=0; i<distance.size(); i++) {
		ans += distance[i];
	}
	
	cout << ans << endl;
	
	return 0;
}
		
		
	
