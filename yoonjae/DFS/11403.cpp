#include <iostream>
#include <cstring>
#include <vector>
using namespace std;

const int MAX = 101;
int N;
int adj[MAX][MAX];
int ans[MAX][MAX];
bool visited[MAX];
vector<int> st;

int cnt = 0;

void DFS(int n) {
  ++cnt;
  cout << "@@@" << cnt << " th DFS started" << endl;
  visited[n] = true;
  st.push_back(n);
  
  for(int i=0; i<N; i++) {
    if(adj[n][i] == 1) {
      for(int j=0; j<st.size(); j++) {
        cout << st[j] << " ";
        ans[st[j]][i] = 1;
      }
      cout << " are connected to " << i << endl;
      if(!visited[i]) {
        DFS(i);
        visited[i] = false;
      }
    }
  }
  st.pop_back();
  cout << "POP! size of stack is now " << st.size() << endl;
  return;
}

int main() {
  cin >> N;
  memset(adj, 0, sizeof(adj));
  memset(ans, 0, sizeof(ans));
  memset(visited, false, sizeof(visited));

  for(int i=0; i<N; i++) {
    for(int j=0; j<N; j++) {
      cin >> adj[i][j];
    }
  }

  for(int i=0; i<N; i++) {
    //cout << "@@@in main@@@ " << "Checking " << i << "th number" << endl;
    if(!visited[i]) {
      DFS(i);
      visited[i] = false;
    }
  }

  for(int i=0; i<N; i++) {
    for(int j=0; j<N; j++) {
      cout << ans[i][j] << " ";
    }
    cout << endl;
  }
}

  


