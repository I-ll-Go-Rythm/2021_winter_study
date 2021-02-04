#include <iostream>
#include <string>

using namespace std;

string S;
int N;
int max_diff;

int main() {
	cin >> S;
	N = stoi(S);

	max_diff = 9 * S.size();

	int sum = 0; string tempS;
	for(int i=N-max_diff; i<N; i++) {
		tempS = to_string(i);
		for(int i=0; i<tempS.size(); i++) {
			sum += tempS[i] - 48;
		}
		sum += i;
		if(sum == N) {
			cout << i << endl;
			break;
		}
		else sum = 0;
	}
	
	if(sum == 0) cout << 0 << endl;
	return 0;
}


