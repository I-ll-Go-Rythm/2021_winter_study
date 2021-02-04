#include <iostream>
#include <vector>

using namespace std;

const int MAX_N = 20;
int arr[MAX_N+1];
int visited[MAX_N+1];
int N, S, count = 0, temp = 0;
vector<int> v;

void back_tracking(int n) {
	if(n != 0) {
		v.push_back(n);
		cout << "add " << arr[n] << endl;
		visited[n] = 1;
		temp += arr[n];
		cout << "\t\t\t***** Sum of ";
		for(int i=0; i<v.size(); i++) {
			cout << arr[v[i]] << " ";
		}
		cout << "is >>>> " << temp << " *****" <<  endl;
	}
	if(temp == S && n != 0) {
		++count;
		cout << "*IT IS THE CASE*" << endl;
	}
	for(int i=n+1; i<N+1; i++) {
		if(visited[i] != 1) {
			back_tracking(i);
			cout << "\tdelete " << arr[i] << endl;
			visited[i] = 0;
			temp -= arr[i];
			v.pop_back();
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

