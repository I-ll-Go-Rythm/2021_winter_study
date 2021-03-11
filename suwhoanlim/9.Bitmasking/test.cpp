#include <stdio.h>
#include <iostream>
using namespace std;

int main(void) {
	cout << sizeof(char)<<endl;;
	int a = 1;
	a << 1;
	cout << a << endl;
	a<<1;
	cout << (a << 'A'-64)<<endl;
	return 0;
}
