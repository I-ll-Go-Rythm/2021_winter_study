// I hate knapsack
// dp is the key
// sol. from https://blog.naver.com/angs91/220930702887
//https://suuntree.tistory.com/49
//https://untouchable.tistory.com/77


#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
 
struct NODE
{
    int next;
    int cycle = 0;
    int cycleCnt = 0;
    int varCnt = 0;
};
 
int N, K, list_size;
int dp[1001][1001];
bool visited[1001];
bool chked[1001];
NODE node[1001];
queue<int> q;
vector<pair<int, int> > list;
 
int dfs(int x)
{
    visited[x] = true;
    int next = node[x].next;
    int cycle = 0;
    if (!chked[next])
    {
        if (visited[next])
        {
            int cnt = 1;
            node[x].cycle = x;
            while (next != x)
            {
                cnt++;
                node[next].cycle = x;
                next = node[next].next;
            }
            node[x].cycleCnt = cnt;
            node[x].varCnt = -cnt;
            q.push(x);
            cycle = x;
        }
        else cycle = dfs(next);
    }
    else
    {
        cycle = node[next].cycle;
    }
    chked[x] = true;
    node[x].cycle = cycle;
    node[cycle].varCnt++;
    return cycle;
}
 
int main()
{
    scanf("%d%d", &N, &K);
    for (int i = 1; i <= N; i++)
    {
        scanf("%d", &node[i].next);
    }
    for (int i = 1; i <= N; i++)
    {
        if (!chked[i]) dfs(i);
    }
 
    int c = 0;
    while (!q.empty())
    {
        c = q.front();
        q.pop();
        if (node[c].cycleCnt > K) continue;
        list.push_back(make_pair(node[c].cycleCnt, node[c].varCnt));
    }
 
    list.push_back(make_pair(0,0));
    sort(list.begin(), list.end());
    list_size = list.size();
 
    memset(dp, -1, sizeof(dp));
    
    int w, v;
    for (int i = 1; i < list_size; i++)
    {
        w = list[i].first;
        v = list[i].second;
        dp[i][w] = v;
        for (int j = 1; j <= K; j++)
        {
            if (j > w)
            {
                if (dp[i - 1][j - w] >= 0)
                {
                    dp[i][j] = max(dp[i-1][j-w] + v, dp[i - 1][j]);
                }
                else
                {
                    dp[i][j] = max(dp[i][j], dp[i - 1][j]);
                }
            }
            else
            {
                dp[i][j] = max(dp[i][j],dp[i - 1][j]);
            }
        }
    }
 
    int ans = 0;
    for (int i = 1; i <= K; i++)
    {
        if (dp[list_size-1][i] >= 0)
        {
            ans = max(ans, i + dp[list_size-1][i]);
        }
    }
    if (ans > K) printf("%d\n", K);
    else printf("%d\n", ans);
    return 0;
}
