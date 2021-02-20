#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

const int MAX = 100;
int N;
int ans = 1;
int arr[MAX][MAX];
bool visited[MAX][MAX];
int dr[4] = {0, 0, 1, -1};
int dc[4] = {1, -1, 0, 0};

void DFS(int r, int c) {
  visited[r][c] = true;
  for(int i=0; i<4; i++) {
    int tempr = r+dr[i], tempc = c+dc[i];
    if(tempr<0 || tempr>N-1 || tempc<0 || tempc>N-1) continue;
    if(!visited[tempr][tempc]) DFS(tempr, tempc);
  }
  return;
}

int main() {
  cin >> N;
  int max_height = 0;
  for(int r=0; r<N; r++) {
    for(int c=0; c<N; c++) {
    cin >> arr[r][c];
    max_height = max(max_height, arr[r][c]);
    }
  }
  for(int i=1; i<=max_height; i++) {
    memset(visited, false, sizeof(visited));
    int cnt = 0;
    for(int r=0; r<N; r++) {
      for(int c=0; c<N; c++) {
        if(arr[r][c] <= i) visited[r][c] = true;
      }
    }
    for(int r=0; r<N; r++) {
      for(int c=0; c<N; c++) {
        if(!visited[r][c]) {
          DFS(r, c);
          ++cnt;
        }
      }
    }
    ans = max(ans, cnt);
  }
  cout << ans << endl;
  return 0;
}

