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

	char arr[4][4];

	for(int i = 0; i < 4; i++) {
		for(int j = 0; j < 4; j++) {
			scanf("%c", &arr[i][j]);
		}
	}

	for(int i = 0; i < 4; i++) {
		for(int j = 0; j < 4; j++) {
			printf("%c",arr[i][j]);
		}
	}

	return 0;
}

