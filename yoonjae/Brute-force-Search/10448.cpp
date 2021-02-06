#include <iostream>
#include <vector>

using namespace std;

int N;
vector<int> tri_num;

int is_three(int n) {
	int max = n/3 + 1;
	for(int i=0; i<max; i++) {
		for(int j=0; j<max; j++) {
			for(int k=0; k<max; k++) {
				if(tri_num[i] + tri_num[j] + tri_num[k] == n)
					return 1;
			}
		}
	}
	return 0;
}


int main() {
	cin >> N;
	int temp = 1, i = 2;
	while(temp <= 1000) {
		tri_num.push_back(temp);
		temp += i; ++i;
	}

	for(int i=0; i<N; i++) {
		int n;
		cin >> n;
		cout << is_three(n) << endl;
	}

	return 0;
}

	



