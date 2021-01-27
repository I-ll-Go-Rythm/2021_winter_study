#include <iostream>
#include <algorithm>

using namespace std;

const int MAX = 51;
char arr[MAX][MAX];
int M, N;

typedef pair<int, int> coord;

int how_many(coord xy) {
	//W start is temp2, B start is temp1
	int temp1 = 0, temp2 = 0;
	for(int i=0; i<8; i++) {
		for(int j=0; j<8; j++) {
			if((i+j)%2 == 0) {
				if(arr[xy.first+i][xy.second+j] != 'B') ++temp1;
				if(arr[xy.first+i][xy.second+j] != 'W') ++temp2;
			}
			else {
				if(arr[xy.first+i][xy.second+j] != 'W') ++temp1;
				if(arr[xy.first+i][xy.second+j] != 'B') ++temp2;
			}
		}
	}

	return min(temp1, temp2);
}		



int main() {
	cin >> M >> N;
	for(int i=1; i<M+1; i++) {
		for(int j=1; j<N+1; j++) {
			cin >> arr[i][j];
		}
	}

	int ans = M*N;
	for(int i=1; i<M-6; i++) {
		for(int j=1; j<N-6; j++) {
			ans = min(ans, how_many(make_pair(i, j)));
//			cout << "i is " << i << ", j is " << j << ", ans is " << ans << endl;
		}
	}

	cout << ans << endl;
}


