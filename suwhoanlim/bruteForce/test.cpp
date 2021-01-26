#include <stdio.h>
#include <iostream>
using namespace std;

int main(void) {
	cout << sizeof(int) <<endl;
	cout << sizeof(int * ) << endl;
	cout << sizeof(char * ) << endl;
	cout << sizeof(char) << endl;
	cout << sizeof(float* ) << endl;
	cout << sizeof(float ) << endl;

	if('a' == 97) 
		cout << "yo its right" << endl;


	return 0;
}

