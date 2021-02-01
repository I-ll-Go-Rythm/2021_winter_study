#include <iostream>
#include <algorithm>

using namespace std;

int main(void) {
	int arr[10] = {5,2,7,1,4,6,3,9,8,0};

	cout << arr << endl;
	cout << arr + 9 <<endl;
	cout << arr + 10 <<endl;
	
	cout << *arr << endl;
	cout << *(arr + 9) <<endl;
	cout << *(arr + 10) <<endl;

	sort(arr, arr+10);

	cout << *arr << endl;
	cout << *(arr + 9) <<endl;
	cout << *(arr + 10) <<endl;
	return 0;
}
