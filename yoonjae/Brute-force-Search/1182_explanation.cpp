#include <iostream>
#include <algorithm>

using namespace std;

const int MAX_N = 20;
int arr[MAX_N+1];
int visited[MAX_N+1];
int N, S, Count = 0, temp = 0;
int backtracking_count = 0;

void back_tracking(int n) {
	++backtracking_count;
	visited[n] = 1;
	temp += arr[n];
//	cout << "back tracking for num " << arr[n] << ", sum is " << temp << endl;
	if(temp == S) ++Count;
	for(int i=n+1; i<N+1; i++) {
		if(temp > S && arr[N] >= S) continue;
		if(visited[i] != 1) {
//			cout << "in if, i is " << i << ", temp is " << temp << endl;
			back_tracking(i);
//			cout << ", and then cancel num " << arr[i] << endl;
			visited[i] = 0;
			temp -= arr[i];
		}
	}
}




int main() {
	cin >> N >> S;
	for(int i=1; i<N+1; i++) {
		cin >> arr[i];
	}
	arr[0] = 0;
	sort(arr+1, arr+N+1);
	fill_n(visited, MAX_N+1, 0);

	back_tracking(0);

	if(S == 0) cout << Count-1  << endl;
	else cout << Count << endl;

	cout << "BackTracking done, " << backtracking_count << endl;

	return 0;
}

