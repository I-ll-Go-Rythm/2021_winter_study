// you need vis array to check whether the node was previously visited or not
// this code can be shortened but i am too lazy to do so
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int N;
vector<int> vec;
int arr[101][101];
int sol[101];
int vis[101];

void dfs(int from, int to) {
    if(arr[from][to] != 1 || vis[to] == 1) {return;}
    sol[to] = 1; vis[to] = 1;
    for(int z = 0; z < N; ++z) 
        if(arr[to][z] == 1 && vis[z] != 1) dfs(to, z);
    return;
}

int main(void) {
    cin >> N;
    
    for(int i = 0; i < N; ++i) {
        for(int k = 0; k < N; ++k)
            cin >> arr[i][k];
    }
    
    for(int i = 0; i < N; ++i){
        for(int j = 0; j < N; ++j) {
            if(arr[i][j] == 1) dfs(i, j);
        }
        for(int k = 0; k < N; ++k) {
            cout << sol[k] << ' ';
            sol[k] = 0;
            vis[k] = 0;
        }
        cout << '\n';
    }

    
    return 0;
}
