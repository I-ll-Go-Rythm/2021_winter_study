#include <iostream>

using namespace std;

long long A, B, C;

long long mul(long long b) { // return 나머지
	if(b == 0) return 1%C;
	else if(b == 1) return A%C;

	if(b%2 == 1) return ((mul(b/2)*mul(b/2))%C*A)%C;
	else if(b%2 == 0) return (mul(b/2)*mul(b/2))%C; 

	return 0;

}

int main() {
	cin >> A >> B >> C;

	cout << mul(B) << endl;

	return 0;
}




