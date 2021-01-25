#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;

int main() {
	cin >> N;
	int sum[N];
	for(int i=0; i<N; i++) {
		cin >> sum[i];
	}

	int answer = 0; int end_index = (sizeof(sum)/sizeof(sum[0])) - 1;
	for(int i=1; i<N; i++) {
		sum[end_index-i] = max(sum[end_index-i], sum[end_index-i]+sum[end_index-i+1]);				
	}

	cout << *max_element(sum, sum+N) << endl;

	return 0;
}

