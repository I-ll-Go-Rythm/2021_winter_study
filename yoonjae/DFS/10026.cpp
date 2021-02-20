#include <iostream>
#include <cstring>

using namespace std;

const int MAX = 101;
char arr1[MAX][MAX];
char arr2[MAX][MAX];
bool visited1[MAX][MAX], visited2[MAX][MAX];
int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};
int cnt1 = 0, cnt2 = 0;
int N;

void DFS(int x, int y, int state) {
  if(state == 1) visited1[x][y] = true;
  else if(state == 2) visited2[x][y] = true;
  
  for(int i=0; i<4; i++) {
    int tempx = x, tempy = y;
    tempx += dx[i]; tempy += dy[i];
    if(tempx<0 || tempx>N-1 || tempy<0 || tempy>N-1) continue;
    if(state==1 && !visited1[tempx][tempy] && arr1[tempx][tempy]==arr1[x][y]) DFS(tempx, tempy, 1);
    if(state==2 && !visited2[tempx][tempy] && arr2[tempx][tempy]==arr2[x][y]) DFS(tempx, tempy, 2);
  }

  return;
}

int main() {
  cin >> N;
  memset(visited1, false, sizeof(visited1));
  memset(visited2, false, sizeof(visited2));
  string input;
  for(int i=0; i<N; i++) {
    cin >> input;
    for(int j=0; j<N; j++) {
      arr1[i][j] = input[j];
      if(input[j] == 'G') arr2[i][j] = 'R';
      else arr2[i][j] = input[j];
    }
  }

  for(int i=0; i<N; i++) {
    for(int j=0; j<N; j++) {
      if(!visited1[i][j]) {
        DFS(i, j, 1);
        ++cnt1;
      }
      if(!visited2[i][j]) {
        DFS(i, j, 2);
        ++cnt2;
      }
    }
  }

  cout << cnt1 << " " << cnt2;

  return 0;
}
