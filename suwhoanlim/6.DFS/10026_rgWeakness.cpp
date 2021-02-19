// dynamic mem alloc
// max size, man init
// max size, global var
// i believe ther will be a difference in efficiency
// but i'm too lazy to test them out XD

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int N;
int arr[101][101];

void dfs(int x, int y, int z, int c) {
    if(x > N || y > N || x < 1 || y < 1) return; // Out of bound
    if(arr[y][x] != z) return;
    arr[y][x] = (z == 3*c ? -3*c : -1*c);
    dfs(x+1, y, z, c);
    dfs(x, y+1, z, c);
    dfs(x-1, y, z, c);
    dfs(x, y-1, z, c);
    
    return;
}

int dfsAll(int c) {
    int component = 0;
    for(int i = 1; i < N+1; ++i){
        for(int j = 1; j < N+1; ++j) {
            if(arr[i][j] * c > 0) {
                ++component;
                dfs(j, i, arr[i][j], c);
            }
        }
    }
    return component;
}

int main(void) {
    
    cin >> N;
    //int arr[101][101]; // int arr[101][101] = {0} // which is faster? manual init or automatic init?
    /* dynamic memory allocation
    int **arr = new int*[N+1];
    for(int i = 1; i < N+1; ++i)
        arr[i] = new int[M+1];
    */
    // 134973
    // 82 71 66 RBG ascii
    // R G B == 1 2 3 respectivly
    char T; // need to check 형변환
    for(int i = 1; i <= N; ++i)
        for(int j = 1; j <= N; ++j) {
            cin >> T;
            arr[i][j] = 134973 % (int)T;
        }

    int K;
    
    for(int i = 1; i <=N; i++) {
	    for(int j = 1; j <=N; j++)
		    cout << arr[i][j];
	    cout << endl;
    }
    
    K = dfsAll(1);
    cout << K << ' ';
    for(int i = 1; i <=N; i++) {
	    for(int j = 1; j <=N; j++)
		    cout << arr[i][j];
	    cout << endl;
    }
    K = dfsAll(-1);
    for(int i = 1; i <=N; i++) {
	    for(int j = 1; j <=N; j++)
		    cout << arr[i][j];
	    cout << endl;
    }
    cout << K << '\n';
    
        
    
    /* dynamic memory allocation
    for(int i = 0; i < N; ++i)
        delete arr[i];
    delete arr;
    */
    return 0;
}
