#include <iostream>
#include <math.h>
using namespace std;

int main(void) {
	long long  sum = 0;
	for(int i = 8; i > 0; i--) {
		sum += i * pow(9,i+1);
		cout << sum << endl;
	}
	cout << sum << endl;
	return 0;
}
