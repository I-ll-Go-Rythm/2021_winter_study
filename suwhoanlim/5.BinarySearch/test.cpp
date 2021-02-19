#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main (void) {
	vector<int> vec;
	
	for(int i = 10; i > 0; --i)
		vec.push_back(i);

	sort(vec.begin(), vec.begin() + 9);

	for(int i = 0; i < 10; ++i)
		cout << vec[i] << endl;

	return 0; 
}
