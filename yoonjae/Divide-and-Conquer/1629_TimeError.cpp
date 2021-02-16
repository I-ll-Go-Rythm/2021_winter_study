#include <iostream>

using namespace std;

int A, B, C;

int main() {
	cin >> A >> B >> C;
	int ans = 1;
	for(int i=0; i<B; i++) {
		ans *= A;
		ans %= C;
	}

	cout << ans << endl;

	return 0;
}




