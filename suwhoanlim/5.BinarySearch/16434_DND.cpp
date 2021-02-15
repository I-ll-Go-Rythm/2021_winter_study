#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;
typedef long long ll;

int main(void) {
    int N, atk;
    cin >> N >> atk;
    
    int **arr = new int*[N];
    for(int i = 0; i < N; i++) {
        arr[i] = new int[3];
        cin >> arr[i][0] >> arr[i][1] >> arr[i][2];
    }
    
    //ll lo = 32, hi = 62, mid, curr = 0, aa, cnt;
    ll lo = 0, hi = LLONG_MAX, mid, curr = 0, aa, cnt;
    
    while(lo <= hi) {
    //while(lo+1 < hi) {
        mid = (hi+lo)/2;
        curr = mid;
        aa = atk;
        for(int i = 0; i < N; i++) {
            if(arr[i][0] == 1) {
                cnt = arr[i][2] / aa; // hero attack count
                curr -= cnt * arr[i][1]; // monster attack dmg
                //cout << curr << ' ';
                if(curr <= 0) break;
            }
            else {
                aa += arr[i][1];
                curr += arr[i][2];
            }
        }
        //printf("%lld %lld %lld %lld %lld %lld\n", lo, hi, mid, curr, atk, aa);
        if(curr > 0) {hi = mid - 1;}
        else {lo = mid + 1;}
        //if(curr > 0) {hi = mid;}
        //else {lo = mid;}
    }
    
    cout << lo << '\n';
    
    for(int i = 0; i < N; i++)
        delete arr[i];
    delete arr;
    return 0;   
}
