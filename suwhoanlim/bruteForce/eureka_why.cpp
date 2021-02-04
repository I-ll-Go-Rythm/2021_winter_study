#include <iostream>
using namespace std;


int sam(int a, int* ar) {
    for(int i = 0; i < 44; i++) {
        for(int j = i; j < 44; j++) {
            for(int k = j; k <44; k++) {
                if(a == (ar[i] + ar[j] + ar[k])) return 1;
                else if(ar[k] > a) break;
            }
            if(ar[j] > a) break;
        }
        if(ar[i] >= (a/3)) return 0;
    }
    return 0;
}

int main(void) {
    int row, cp;
    int val;
    int arr[44];
    cin >> row;
    cp = row;
    
    int *ans = new int[row+1];
    for(int i = 0 ; i < 44; i++)
        arr[i] = (i+1) * (i+2) / 2; // get sam-gak-su, arr[0] ~ arr[43]
    while(row) {
        cin >> val;
        ans[row] = sam(val, arr);
        row--;
    }
    while(cp) {
        cout << ans[cp] << endl;
        cp--;
    }
    
    delete ans;
    return 0;
}
