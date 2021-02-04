#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

int N, K;
using namespace std;

int main() {
	cin >> N >> K;
	vector<priority_queue<int, vector<int>, greater<int> > > v(K+1);
	vector<bool> check(K+1, false);
	vector<int> list;
	
	
	int input;
	for(int i=0; i<K; i++) {
		cin >> input;
		v[input].push(i); // vector index는 본인 숫자, 해당 index의 pq에 본인이 등장하는 순서를 push
		list.push_back(input);
	}
	
	int count = 0; int ans = 0; // count는 현재 멀티탭에 꽂혀있는 장치 개수, ans 는 멀티탭에서 장치  빼는 횟수 
	for(int i=0; i<K; i++) {
		v[list[i]].pop();
		if(check[list[i]] == true) continue; // 멀티탭에 꽂혀있는 경우 
		else { //안꽂혀있는 경우 
			if(count < N) ++count; // 멀티탭에 빈 자리 있는 경우  
			else {
				int temp = 0; int adios = 0;
				for(int j=1; j<K+1; j++) {
					if(check[j] == true) {
						if(v[j].empty()) {
							adios = j;
							break;
						}
						else if(v[j].top() > temp) {
							adios = j;
							temp = v[j].top();
						}
					}
				}
				check[adios] = false;
				++ans;
			}			
			check[list[i]] = true;
		}
	}
	
	cout << ans << endl;
	
	return 0;
}
			
					
			
		
	
	
		
		
	
