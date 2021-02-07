#include <iostream>
#include <algorithm>
#include <utility>
#include <queue>
#include <stdlib.h>
#include <vector>
using namespace std;

int main(void) {
	
	cout << sizeof(int) << sizeof(long) << sizeof(long long) << endl;

	int arr[10] = {5,2,7,1,4,6,3,9,8,0};
	priority_queue<int, vector<int>, greater<int> > pq;
	int a;
	for(int i = 0; i < 10; i++) {
		a = rand() % 10;
		pq.push(a);
		cout << a << ' ';
	}
	cout << '\n';
	for(int i = 0; i < 10; i++) {
		cout << pq.top() << ' ';
		pq.pop();
	}

	cout << '\n';
	cout << '\n';

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
