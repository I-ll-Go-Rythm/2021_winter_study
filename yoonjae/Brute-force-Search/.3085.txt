#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX = 51;
char arr[MAX][MAX];
int N;

int count() {
	int ans = 1;

	for(int i=0; i<N; i++) {
		int temp = 1;
		for(int j=0; j<N-1; j++) {
			if(arr[i][j] == arr[i][j+1]) ++temp;
			else {
				ans = max(ans, temp);
				temp = 1;
			}
		}
		ans = max(ans, temp);
	}
	for(int j=0; j<N; j++) {
		int temp = 1;
		for(int i=0; i<N-1; i++) {
			if(arr[i][j] == arr[i+1][j]) ++temp;
			else {
				ans = max(ans, temp);
				temp = 1;
			}
		}
		ans = max(ans, temp);
	}

	return ans;
}

int main() {
	cin >> N;
	for(int i=0; i<N; i++) {
		for(int j=0; j<N; j++) {
			cin >> arr[i][j];
		}
	}

	int ans = 1;
	for(int i=0; i<N; i++) {
		for(int j=0; j<N-1; j++) {
			char temp = arr[i][j];
			arr[i][j] = arr[i][j+1];
			arr[i][j+1] = temp;
			ans = max(count(), ans);
			temp = arr[i][j];
			arr[i][j] = arr[i][j+1];
			arr[i][j+1] = temp;
		}
	}
	for(int j=0; j<N; j++) {
		for(int i=0; i<N-1; i++) {
			char temp = arr[i][j];
			arr[i][j] = arr[i+1][j];
			arr[i+1][j] = temp;
			ans = max(count(), ans);
			temp = arr[i][j];
			arr[i][j] = arr[i+1][j];
			arr[i+1][j] = temp;
		}
	}

	cout << ans << endl;
}







	
