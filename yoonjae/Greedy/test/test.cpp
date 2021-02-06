#include <vector>
#include <iostream>


using namespace std;

int main() {
	vector<int> v;
	for(int i=0; i<6; i++) {
		v.push_back(i);
	}

	vector<int>::iterator it = v.begin();

	it += 3;

	cout << "Size is " << v.size() << endl;
	cout << "Pointing value is " <<	*it << endl;

	v.erase(it);
	cout << "ERASE DONE" << endl;


	cout << "Size is " << v.size() << endl;
	cout << "Pointing value is " <<	*it << endl;

	v.erase(it);
	cout << "ERASE DONE" << endl;


	cout << "Size is " << v.size() << endl;
	cout << "Pointing value is " <<	*it << endl;
}
