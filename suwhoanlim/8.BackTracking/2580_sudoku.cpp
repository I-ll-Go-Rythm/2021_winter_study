#include <iostream>
#include <vector>
#include <utility>
using namespace std;
int arr[9][9], neg;
vector<pair<int, int>> vec(81);

void dfs(int cnt, int x, int y) {
    if(arr[y][x] != 0) return;
    for(int i = 1; i < 10; ++i){ // row
        arr[y][x] = i;
        for(int j = 0; j < 9; ++j){
            if(arr[y][j] == i && j != x) {neg = -1; break;}
            else if(arr[y][j] == 0) {dfs(cnt-1, j, y);}
        }
        if(neg == -1) {neg = 0; continue;}
        
        for(int j = 0; j < 9; ++j){ // column
            if(arr[j][x] == i && j != y) {neg = -1; break;}
            else if(arr[j][x] == 0) {dfs(cnt-1, x, j);}
        }
        if(neg == -1) {neg = 0; continue;}
        
        int tmp1 = (y/3)*3, tmp2 = (x/3)*3;
        for(int j = 0; j < 3; ++j){ //s1
            if(arr[tmp1][tmp2 + j] == i && (tmp1 != y || tmp2 + j != x)) {neg = -1; break;}
            else if(arr[tmp1][tmp2 + j] == 0) {dfs(cnt-1, tmp2 + j, tmp1);}
        }
        if(neg == -1) {neg = 0; continue;}
        for(int j = 0; j < 3; ++j){ //s2
            if(arr[tmp1+1][tmp2 + j] == i && (tmp1+1 != y || tmp2 + j != x)) {neg = -1; break;}
            else if(arr[tmp1+1][tmp2 + j] == 0) {dfs(cnt-1, tmp2 + j, tmp1+1);}
        }
        if(neg == -1) {neg = 0; continue;}
        for(int j = 0; j < 3; ++j){ //s3
            if(arr[tmp1+2][tmp2 + j] == i && (tmp1+2 != y || tmp2 + j != x)) {neg = -1; break;}
            else if(arr[tmp1+2][tmp2 + j] == 0) {dfs(cnt-1, tmp2 + j, tmp1+2);}
        }
        if(neg == -1) {neg = 0; continue;}   
        else break;
    }
}


int main(void) {
    int cnt = 0, i = 0;
    int x = 0, y = 0;
    pair<int, int> p;
    for(int i = 0; i < 9; ++i) 
        for(int j = 0; j < 9; ++j) {
            cin >> arr[i][j];
            if(arr[i][j] == 0) {
                ++cnt;
                p.first = j; p.second = i;
                vec.push_back(p);
            }
        }
    
    while(++i <= cnt) {
	    cout << cnt<< ' '<< i <<' ' << vec[i-1].first << ' ' << vec[i-1].second << ' ';
	    cout << arr[vec[i-1].first][vec[i-1].second] << ' ';
	    dfs(cnt, vec[i-1].first, vec[i-1].second);
	    cout << arr[vec[i-1].first][vec[i-1].second] << endl;
    }

    for(int i = 0; i < 9; ++i) {
        for(int j = 0; j < 9; ++j) {
            cout << arr[i][j];
        }
        cout << endl;
    }
    return 0;
}
