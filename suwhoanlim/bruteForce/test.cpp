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
	cout << "boolean test" << endl;
	cout << sizeof(bool ) << endl;
	bool ara[3];
	bool araa[5];
	cout << sizeof(ara ) << endl;
	cout << sizeof(araa ) << endl;
	int a, b, c, d, e;
	scanf("%d%d%d %d %d\n", &a, &b, &c, &d, &e);
	printf("%d %d %d %d %d\n", a, b, c, d, e);

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

