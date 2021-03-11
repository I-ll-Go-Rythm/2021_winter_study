#include <iostream>
#include <queue>
#include <algorithm>
#include <utility>
#include <unordered_map>
using namespace std;
int N, M, howmany, c;
char arr[51][51];
/*
void clear(queue<pair<int, int>> &someQueue)
{
    queue<pair<int,int>> empty;
    swap(someQueue, empty);
}
*/

void bfs(int a, int aa, int aaa) {
    queue<int> q;
    q.push(a); q.push(aa); q.push(aaa);
    int tmp1, k;
    char tmp;
    while(1) {
        if(q.size() == 0) {howmany = -1; return;}
        int qsize = q.size();
        for(int i = 0; i < qsize; i+=3) {
            a = q.front();
            q.pop();
            aa = q.front();
            q.pop();
            aaa = q.front();
            q.pop();
            if(a > N || 1 > a || aa > M || 1 > aa) continue;
            tmp = arr[a][aa];
            if(tmp == '1') {cout << a<<' '<<aa<<endl; return;}
            else if(tmp == '#') continue;
            else if ('A' <= tmp && tmp <= 'F') {
                tmp = tmp - 65;
                int b = 0;
                b = 1 << tmp;
                if((aaa & b) == 0) {cout<<'f'<<aaa<<' '<<b; continue;}
            }
	    else if (tmp != '.' && tmp != '0') {
                aaa |= (1 << (tmp - 97));
                aaa &= 63; q.push(a+1); q.push(aa); q.push(aaa);
                aaa |= 64; q.push(a-1); q.push(aa); q.push(aaa);
                aaa |= 128; q.push(a); q.push(aa-1); q.push(aaa);
                aaa &= 63; aaa |= 128; q.push(a); q.push(aa+1); q.push(aaa);
            	cout << aaa << endl;
		//cout<<'0';
		continue;
	    }
            int t = 0;
            t = aaa & 448;
            t = t >> 6;
            
            if(t != 1) {
                aaa &= 63; q.push(a+1); q.push(aa); q.push(aaa);    
            }
            if(t != 0) {
         aa &= 63; aaa |= 64; q.push(a-1); q.push(aa); q.push(aaa);
            }
            if(t != 2) {
                aaa &= 63; aaa |= 192; q.push(a); q.push(aa-1); q.push(aaa);
            }
            if(t != 3) {
                aaa &= 63; aaa |= 128; q.push(a); q.push(aa+1); q.push(aaa);
            }
	    //cout<<1;
        }
        ++howmany;
	cout << howmany<<endl;
	cout << q.size()<<endl;
        //cout << howmany << ' '<< "one rap" << endl;
    }
}


int main(void) {
    int x, y;
    cin >> N >> M;
    
    for(int i = 1; i <= N; i++) {
        for(int j = 1; j <= M; j++) {
            cin >> arr[i][j];  cout<< arr[i][j];
            if(arr[i][j] == '0') {y = i; x = j;}
        }
    cout << endl;
}
   cout << x << y << endl; 
    bfs(y, x, 256);
    cout << howmany << '\n';
    
    return 0;
}
