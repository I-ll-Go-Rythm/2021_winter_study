// dynamic mem alloc
// max size, man init
// max size, global var
// i believe ther will be a difference in efficiency
// but i'm too lazy to test them out XD

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int T, N, maxn, c, tot;
int arr[100001];
int vis[100001];
int fin[100001];


void dfs(int next) {
    if(vis[next] == c && fin[next] == c) {
        do {
            fin[next] = -c;
            ++maxn;
            next = arr[next];
        } while(fin[next] != -c);
        return;
    }
    else if(vis[next] != 0) return; // already visited
        
    vis[next] = c;
    fin[next] = c;
    dfs(arr[next]);
}

void dfsAll() {
    for(int i = 1; i <= N; ++i){
        if(vis[i] == 0) {
            ++c;
            dfs(i);
            tot += maxn;
            maxn = 0;
        }
    }
    return;
}

int main(void) {
    cin >> T;
    while(T--) {
        int sum = 0;
        cin >> N;
        for(int i = 1; i <= N; ++i){ 
            cin >> arr[i];
            vis[i] = 0; fin[i] = 0;
        }
        dfsAll();
        cout << N - tot << '\n';
        tot = 0;
    }

    return 0;
}
