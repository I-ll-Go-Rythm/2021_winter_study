//https://gsmesie692.tistory.com/113
// https://namnamseo.tistory.com/entry/냅색-알고리즘
//The first one is better reference

#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
    int N, K;
    cin >> N >> K;
    int **arr = new int* [N+1];
    int **bag = new int* [N+1];
    for(int i = 0; i < N+1; i++) {
        arr[i] = new int [2];
        bag[i] = new int [K+1];
        bag[i][0] = 0;
        cin >> arr[i][0] >> arr[i][1];
    }
    
    for(int i = 0; i < K+1; i++)
        bag[0][i] = 0;
    
    for(int i = 0; i < N+1; i++) { // item no
        for (int j = 0; j < K+1; j++) { // weight
            if (i == 0 || j == 0) continue; //bag[i][j] = 0;
            else if (arr[i-1][0] <= j) // Always be aware of the index
                bag[i][j] = max(arr[i-1][1] + bag[i-1][j-arr[i-1][0]], bag[i-1][j]);
            else    
                bag[i][j] = bag[i-1][j];
        }
    }
    //important to understatnd how this works, how knapsack works
    //one item per iteration
                  
    cout << bag[N][K] << '\n';
        
    for(int i = 0; i < N+1; i++) {
        delete bag[i];
        delete arr[i];
    }
    delete arr;
    delete bag;
    
    return 0;
}
