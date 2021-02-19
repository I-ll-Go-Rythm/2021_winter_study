// need to be more mindful about cnt = -1 clause
// we don't neccessarily have to go back to P for checking

#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <utility> 
using namespace std;
int N, M, P, cnt, init;
unordered_map<int, int> m; // hate, love

void dfs(int hate) {
    unordered_map<int, int>::iterator iter = m.find(hate);
    if(iter == m.end()) return;
    else if(iter->second == -1) {cnt = -1; return;}
    ++cnt;
    int k = iter->second;
    iter->second = -1;
    dfs(k);
    
    return;
}

int main(void) {
    pair<int, int> t;
    cin >> N >> M >> P;
    for(int i = 0; i < N; ++i){
        cin >> t.second >> t.first; // t1 = love, t0 = hate
        if(m.find(t.first) == m.end()) {
            m.insert(t);
        }
    }

    dfs(P);
    cout << cnt << '\n';  
    

    return 0;
}
