#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

typedef pair<int, int> pii;
int N;

struct node {
	int s;
	int t;
	
	node(int _s, int _t) {
		s = _s;
		t = _t;
	}
};

struct cmp {	
	bool operator()(node& a, node& b) {
		if(a.t == b.t) return a.s > b.s;
		else return a.t > b.t;
	}
};

bool compare(node& a, node& b) {
	if(a.s == b.s) return a.t < b.t;
	else return a.s < b.s;
}



int main() {
	cin >> N;
	vector<node> lecture;
	priority_queue<node, vector<node>, cmp> q;
	
	int input1, input2;
	for(int i=0; i<N; i++) {
		cin >> input1 >> input2;
		node temp(input1, input2);
		lecture.push_back(temp);
	}
	sort(lecture.begin(), lecture.end(), compare);
	
	/*
	for(int i=0; i<lecture.size(); i++) {
	//	cout <<  lecture[i].first << ", " << lecture[i].second << endl;
		q.push(lecture[i]);
	}
	
	q.push(make_pair(100,4));
	
	
    while (!q.empty()) {
        cout << q.top().first << ", " << q.top().second << endl;
        q.pop();
    }
	*/
	
	q.push(lecture[0]);
	int ans = 1;
	for(int i=1; i<N; i++) {
//		cout << "index " << i << ", top is " << q.top().first << ", " << q.top().second << endl;
		if(q.top().t > lecture[i].s) {
			++ans;
		}
		else {
			q.pop();
		}
		q.push(lecture[i]);
	}
//	cout << "top is " << q.top().first << ", " << q.top().second << endl;
	
	cout << ans << endl;
	
	return 0;
}
		
	
	
		
		
	
