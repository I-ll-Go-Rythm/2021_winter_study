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
		v[input].push(i); // vector index�� ���� ����, �ش� index�� pq�� ������ �����ϴ� ������ push
		list.push_back(input);
	}
	
	int count = 0; int ans = 0; // count�� ���� ��Ƽ�ǿ� �����ִ� ��ġ ����, ans �� ��Ƽ�ǿ��� ��ġ  ���� Ƚ�� 
	for(int i=0; i<K; i++) {
		v[list[i]].pop();
		if(check[list[i]] == true) continue; // ��Ƽ�ǿ� �����ִ� ��� 
		else { //�Ȳ����ִ� ��� 
			if(count < N) ++count; // ��Ƽ�ǿ� �� �ڸ� �ִ� ���  
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
			
					
			
		
	
	
		
		
	
