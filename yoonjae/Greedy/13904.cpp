#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int N;

struct hw {
	int d;
	int s;
	
	hw(int _d, int _s) {
		d = _d;
		s = _s;
	}
};

struct comp1 {
	bool operator()(hw& a, hw& b) {
		if(a.d == b.d) return a.s < b.s;
		else return a.d < b.d;
	}
};

struct comp2 {
	bool operator()(hw& a, hw& b) {
		if(a.s == b.s) return a.d < b.d;
		else return a.s < b.s;
	}
};


int main() {
	cin >> N;
	vector<int> score(N+1);
	priority_queue<hw, vector<hw>, comp1> q;
	priority_queue<hw, vector<hw>, comp2> r;
	
	
	int input1, input2;
	for(int i=0; i<N; i++) {
		cin >> input1 >> input2;		
		q.push(hw(input1, input2));
	}
	/*
	while(!q.empty()) {
		cout << "(" << q.top().d << ", " << q.top().s << ")" << " ";
		q.pop();
	}
	*/
	
	int temp;
	for(int i=N; i>0; i--) {
//		cout << "in for, i is " << i << endl;
		while(!q.empty() && q.top().d >= i) {
//			cout << "in while";
//			cout << "(" << q.top().d << ", " << q.top().s << ")" << " " << endl;
			r.push(q.top());
			q.pop();
//			++count;
		}
		if(r.empty()) score[i] = 0;
		else {
			score[i] = r.top().s;
			r.pop();
		}
	}
	
	int sum = 0;
	for(int i=1; i<N+1; i++) {
		sum += score[i];
	}
	
	cout << sum << endl;
	
	return 0;
}
		
			
		
		
		
		
	
