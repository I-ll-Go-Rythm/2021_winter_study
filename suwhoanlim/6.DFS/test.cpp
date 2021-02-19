#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
	char T;

	cin >> T;
	while(T != 'q') {
		cout << T << endl;
		cout << (int)T << endl;
		cin >> T;
	}
	return 0;
}
