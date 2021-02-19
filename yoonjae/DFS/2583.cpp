#include <iostream>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX = 101;
int M, N, K, cnt = 0;
bool visited[MAX][MAX];
vector<int> ans;
int xmove[4] = {0, 0, 1, -1};
int ymove[4] = {1, -1, 0, 0};


void DFS(int x, int y) {
//  cout << "DFS, x is " << x << ", y is " << y << endl;
  ++cnt;
  visited[x][y] = true;
  for(int i=0; i<4; i++) {
    int tempx = x+xmove[i];
    int tempy = y+ymove[i];
    if(!visited[tempx][tempy] && 0 <= tempx && tempx < N && 0 <= tempy && tempy < M) {
      DFS(tempx, tempy);
    }
  }
}

// left top is the signature of square
int main() {
  cin >> M >> N >> K;
  memset(visited, false, sizeof(visited));

  int x1, y1, x2, y2;
  for(int i=0; i<K; i++) {
    cin >> x1 >> y1 >> x2 >> y2;

    for(int i=x1; i<x2; i++) {
      for(int j=y1; j<y2; j++) {
        visited[i][j] = true;
      }
    }
  }
/*
  for(int i=0; i<M; i++) {
    for(int j=0; j<N; j++) {
      if(!visited[j][i]) cout << "f ";
      else cout << "* ";
    }
    cout << endl;
  }
*/

  for(int i=0;i<M; i++) {// M is y(row)
    for(int j=0; j<N; j++) {
      if(!visited[j][i]) {
        DFS(j, i);
//        cout << "i is " << i << ", j is " << j << ", cnt is " << cnt << endl;
        ans.push_back(cnt);
        cnt = 0;
      }
    }
  }

  sort(ans.begin(), ans.end());
  cout << ans.size() << endl;
  for(int i=0; i<ans.size(); i++) {
    cout << ans[i] << " ";
  }
  
}
