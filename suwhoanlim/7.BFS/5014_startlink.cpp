//version with predefined array

#include <iostream>
#include <queue>
#include <algorithm>
#include <utility>
#include <unordered_map>
using namespace std;
int F, S, G, U, D, c, howmany;
bool arr[1000000];
/*
void clear(queue<pair<int, int>> &someQueue)
{
    queue<pair<int,int>> empty;
    swap(someQueue, empty);
}
*/

void bfs() {
    queue<int> q;
    q.push(S);
    int p;
    unordered_map <int, int> map;
    
    while(!q.empty()) {
        int qsize = q.size();
        for(int i = 0; i < qsize; ++i ) {
            p = q.front();
            q.pop();
            if(p == G) {c = -1; return;}
            if(p < 1 || p > F) continue;
            if(arr[p-1] == 1) continue;
            arr[p-1] = 1;
            map.insert(make_pair(p,-1));
            q.push(p+U);
            q.push(p-D);
        }
        ++howmany;
        //cout << howmany << ' '<< "one rap" << endl;
    }
}


int main(void) {
    cin >> F>>S>>G>>U>>D;
    bfs();
    if(c == -1) cout << howmany << endl;
    else cout << "use the stairs" << endl;
    
    return 0;
}
