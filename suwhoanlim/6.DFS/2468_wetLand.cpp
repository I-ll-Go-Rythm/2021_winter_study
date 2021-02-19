// dynamic mem alloc
// max size, man init
// max size, global var
// i believe ther will be a difference in efficiency
// but i'm too lazy to test them out XD

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int N, maxland;
int arr[101][101];
int vis[101][101];

void dfs(int x, int y, int i) {
    if(x > N || y > N || x < 0 || y < 0) return; // Out of bound
    if(vis[y][x] == 1) return;
    if(arr[y][x] <= i) return;
    vis[y][x] = 1;
    dfs(x+1, y, i);
    dfs(x, y+1, i);
    dfs(x-1, y, i);
    dfs(x, y-1, i);
    
    return;
}

void dfsAll(int h) {
    int component = 0;
    for(int i = 0; i < N; ++i){
        for(int j = 0; j < N; ++j) {
            if(vis[i][j] == 0 && arr[i][j] > h) {
                ++component;
                dfs(j, i, h);
            }
        }
    }
    cout << maxland << ' '<<component << endl;
    maxland = maxland > component ? maxland : component;
    return;
}

int main(void) {
    int max = 0;
    cin >> N;

    for(int i = 0; i < N; ++i)
        for(int j = 0; j < N; ++j) {
            cin >> arr[i][j];
            max = max > arr[i][j] ? max : arr[i][j];
        }
    for(int i = 0; i < max; ++i) {
        dfsAll(i);
        for(int j = 0; j < N; ++j)
            for(int k = 0; k < N; ++k)
                vis[j][k] = 0;
    }
    
    cout << maxland << '\n';
    
        
    
    /* dynamic memory allocation
    for(int i = 0; i < N; ++i)
        delete arr[i];
    delete arr;
    */
    return 0;
}
