// not having arr[300][300] will cause an memory & time overflow
// if you put arr[p.first][p.second] = T, then it will not pass the test
// this is because the arr will be initialized as 0 at the beginning of the program
// Thus we have it T+1

// is there any way to efficiently save the next coordinate to the queue?

#include <iostream>
#include <queue>
#include <algorithm>
#include <utility>
using namespace std;
int L, n1, n2, w1, w2, howmany, T, arr[300][300];
/*
void clear(queue<pair<int, int>> &someQueue)
{
    queue<pair<int,int>> empty;
    swap(someQueue, empty);
}
*/

void bfs() {
    queue<pair<int,int>> q;
    pair<int, int> p, pp;
    p.first = n1; p.second = n2;
    q.push(p);
    
    while(!q.empty()) {
        int qsize = q.size();
        for(int i = 0; i < qsize; ++i ) {
            p = q.front();
            q.pop();
            if(p.first == w1 && p.second == w2){return;}
            if(p.first < 0 || p.second < 0 || p.first >= L || p.second >= L) continue;
            if(arr[p.first][p.second] == T+1) continue;
            arr[p.first][p.second] = T+1;

            pp.first = p.first - 2;
            pp.second = p.second + 1;
            q.push(pp);
            pp.second = p.second - 1;           
            q.push(pp);
            ++pp.first;
            pp.second = p.second - 2;           
            q.push(pp);
            pp.second = p.second + 2;           
            q.push(pp);
            pp.first = p.first + 1;
            pp.second = p.second + 2;            
            q.push(pp);
            pp.second = p.second - 2;            
            q.push(pp);
            pp.first = p.first + 2;
            pp.second = p.second + 1;            
            q.push(pp);
            pp.second = p.second - 1;
            q.push(pp);
        }
        ++howmany;
        //cout << howmany << ' '<< "one rap" << endl;
    }
}


int main(void) {
    cin >> T;
        
    while(T--) {
        cin >> L;
        cin >> n1 >> n2;
        cin >> w1 >> w2;
        //printf("%d %d %d %d %d\n", L, n1, n2, w1, w2);
        bfs();
        cout << howmany << endl;
        howmany = 0;
        //clear(q)
    }
}
