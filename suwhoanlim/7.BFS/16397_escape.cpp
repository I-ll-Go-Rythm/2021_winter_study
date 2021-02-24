//version with predefined array

#include <iostream>
#include <queue>
#include <algorithm>
#include <utility>
#include <unordered_map>
using namespace std;
int N, T, G, c, howmany;
bool arr[100000];
/*
void clear(queue<pair<int, int>> &someQueue)
{
    queue<pair<int,int>> empty;
    swap(someQueue, empty);
}
*/

void bfs() {
    queue<int> q;
    q.push(N);
    int p, tmp, tmp1, k;
    
    while(!q.empty()) {
        int qsize = q.size();
        for(int i = 0; i < qsize; ++i ) {
            if(howmany > T) return;
            p = q.front();
            q.pop();
            if(p == G) {c = -1; return;}
            if(p > 99999 || 0 > p || arr[p] == 1) continue;
            // will there be any smarter way to determine when to stop?
            arr[p] = 1;
            q.push(p+1);
            tmp = p * 2;
            if(tmp > 99999 ||tmp == 0) continue; 
            for(k = 1; k < 10000; k*=10) {
                tmp1 = tmp / 10;
                if(tmp1 == 0) break;
                tmp = tmp1;
            }
            tmp = p*2-k <= 0 ? 0 : p*2-k;
            q.push(tmp);
        }
        ++howmany;
        //cout << howmany << ' '<< "one rap" << endl;
    }
}


int main(void) {
    cin >> N>>T>>G;
    bfs();
    if(c == -1) cout << howmany << endl;
    else cout << "ANG" << endl;
    
    return 0;
}
