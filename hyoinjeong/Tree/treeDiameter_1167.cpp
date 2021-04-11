#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;
class Graph{
    int N;
    vector<vector<pair<int,int>>> adj;
    vector<bool> visited;
    int ret=0;
    int distance=0;
    public:
    Graph():N(0){}
    Graph(int n):N(n){
        adj.resize(N);
        visited.resize(N,false);
    }
    void addEdge(int x, int y, int r){
        adj[x].push_back({y,r});
    }
    void dfs(int x){
        visited[x]=true;
        for(pair<int,int> next:adj[x]){
            if(!visited[next.first]){
                visited[next.first]=true;
                ret+=next.second;
                distance=max(distance,ret);
                dfs(next.first);
                ret-=next.second;
            }
        }
    }
    void reset(){
        fill(visited.begin(),visited.end(),false);
        ret=0;
        distance=0;
    }
    int getDistance(){
        return distance;
    }
};

int main(){
    int v,x,y,r,dist=0;
    scanf("%d",&v);
    Graph G(v+1);
    for(int i=0;i<v;i++){
        scanf("%d",&x);
        while(1){
            scanf("%d",&y);
            if(y==-1) break;
            scanf("%d",&r);
            G.addEdge(x,y,r);
        }
    }
    for(int i=1;i<=v;i++){
        G.dfs(i);
        dist=max(dist,G.getDistance());
        G.reset();
    }
    printf("%d",dist);
}