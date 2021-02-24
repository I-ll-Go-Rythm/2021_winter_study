//version with predefined array

#include <iostream>
#include <queue>
#include <algorithm>
#include <utility>
#include <unordered_map>
using namespace std;
int N, K, howmany;
bool arr[100001];
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
    int p;
    
    while(!q.empty()) {
        int qsize = q.size();
        for(int i = 0; i < qsize; ++i ) {
            p = q.front();
            q.pop();
            if(p == K) {return;}
            if(p < 0 || p > 100000) continue; // any better ways to set the maximum value?
            if(arr[p-1] == 1) continue;
            arr[p-1] = 1;
            q.push(p+1);
            q.push(p-1);
            q.push(p*2);
        }
        ++howmany;
        //cout << howmany << ' '<< "one rap" << endl;
    }
}


int main(void) {
    cin >> N>>K;
    bfs();
    cout << howmany << endl;
    
    return 0;
}
