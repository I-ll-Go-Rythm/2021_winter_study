#include <iostream>

using namespace std;

int L, P, V;

int main() {

	int i = 1;
	cin >> L >> P >> V;

	do {
		int R = V % P;
		if(L < R) 
			cout << "Case " << i << ": " << L * (V/P) + L << endl;
		else
			cout << "Case " << i << ": " << L * (V/P) + R << endl;

		cin >> L >> P >> V;
		++i;
	} while(V != 0);

	return 0;
}


