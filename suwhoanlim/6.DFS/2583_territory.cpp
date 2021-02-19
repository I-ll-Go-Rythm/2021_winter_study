// dynamic mem alloc
// max size, man init
// max size, global var
// i believe ther will be a difference in efficiency
// but i'm too lazy to test them out XD

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int N, M;
vector<int> vec;
int arr[101][101];

int dfs(int x, int y) {
    if(x > M || y > N || x < 1 || y < 1) return 0; // Out of bound
    if(arr[y][x] != 0) return 0;
    int node = 1;
    arr[y][x] = -1;
    node += dfs(x+1, y);
    node += dfs(x, y+1);
    node += dfs(x-1, y);
    node += dfs(x, y-1);
    
    return node;
}

int dfsAll() {
    int component = 0;
    for(int i = 1; i < N+1; ++i){
        for(int j = 1; j < M+1; ++j) {
            if(arr[i][j] == 0) {
                ++component;
                int k = dfs(j, i);
                vec.push_back(k);
            }
        }
    }
    return component;
}

int main(void) {
    int K, t1, t2, t3, t4;
    cin >> N >> M >> K;
    //int arr[101][101]; // int arr[101][101] = {0} // which is faster? manual init or automatic init?
    /* dynamic memory allocation
    int **arr = new int*[N+1];
    for(int i = 1; i < N+1; ++i)
        arr[i] = new int[M+1];
    */
    
    for(int i = 0; i < K; ++i) {
        cin >> t1 >> t2 >> t3 >> t4;
        for(int k = t2+1; k <= t4; ++k)
            for(int j = t1+1; j <= t3; ++j)
                arr[k][j] = 1;
    }
    
    K = dfsAll();
    sort(vec.begin(), vec.end());
    cout <<vec.size() << '\n';
    for(int i = 0; i < vec.size(); ++i)
        cout << vec[i] << ' ';
    cout << '\n';
        
    
    /* dynamic memory allocation
    for(int i = 0; i < N; ++i)
        delete arr[i];
    delete arr;
    */
    return 0;
}
