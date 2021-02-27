#include <stdio.h>
#include <iostream>
using namespace std;

int main(void) {
	int x = 0;
	long long y = 0;
	for(int i = 50; i >= 10; i--) {
		x += i; y += i;
		x *=100; y *= 100;
	}

	cout <<x<<endl;
	cout <<y<<endl;
	char c;
	for(int i = 0 ; i<10; i++) {

	cin >> c;
	cout << c;
	}
	return 0;


}
