<<<<<<< HEAD
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
=======
#include <iostream>
#include <algorithm>
#include <utility>
using namespace std;

int main(void) {
	int arr[10] = {5,2,7,1,4,6,3,9,8,0};

	cout << sizeof(pair<int, int>) << endl;
	cout << arr << endl;
	cout << arr << endl;
	
	
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
>>>>>>> 0d317a691d9eb22032e11e6ff1579e3070b7e217
