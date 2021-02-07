#include <iostream>
#include <vector>

using namespace std;

int N, K, Count = 0;
vector<int> v;

int main() {
	cin >> N >> K;
	for(int i=0; i<N; i++) {
		int input;
		cin >> input;
		v.push_back(input);
	}

	for(int i=v.size()-1; i>=0; i--) {
		if(v[i] > K)
			continue;
		else {
			do {
				K -= v[i];
				++Count;
			} while(v[i] <= K);
		}
	}

	cout << Count << endl;

	return 0;
}
			
		
	
