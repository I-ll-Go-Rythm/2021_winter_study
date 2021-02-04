#include <iostream>
#include <vector>

using namespace std;

const int MAX_N = 20;
int arr[MAX_N+1];
int visited[MAX_N+1];
int N, S, count = 0, temp = 0;

void back_tracking(int n) {
	if(n != 0) {
		v.push_back(n);
		visited[n] = 1;
		temp += arr[n];
	if(temp == S && n != 0)
		++count;
	for(int i=n+1; i<N+1; i++) {
		if(visited[i] != 1) {
			back_tracking(i);
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
	fill_n(visited, MAX_N+1, 0);

	back_tracking(0);

	cout << count << endl;

	return 0;
}

