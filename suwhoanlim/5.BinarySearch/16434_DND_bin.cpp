#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;
typedef long long ll;
// DND solved using binary search
int main(void) {
    int N, atk;
    cin >> N >> atk;
    
    int **arr = new int*[N];
    for(int i = 0; i < N; i++) {
        arr[i] = new int[3];
        cin >> arr[i][0] >> arr[i][1] >> arr[i][2];
    }
    
    ll lo = 0, hi = LLONG_MAX, mid, curr = 0, aa, cnt;

    while(lo + 1 < hi) {
        mid = (hi+lo)/2;
        curr = mid;
        aa = atk;
        for(int i = 0; i < N; i++) { // mind the max_h >= curr health, despite potion!
            if(arr[i][0] == 1) {
                if(arr[i][2] %aa == 0) cnt = arr[i][2] / aa - 1; // hero attack count
                else cnt = arr[i][2] / aa;
                curr -= cnt * arr[i][1]; // monster attack dmg
                if(curr <= 0) break;
            }
            else {
                aa += arr[i][1];
                if(mid <= curr + arr[i][2]) curr = mid;
                else curr += arr[i][2];
            }
        }
        if(curr > 0) hi = mid;
        else lo = mid;
    }
    
    cout << hi << '\n';

    for(int i = 0; i < N; i++)
        delete arr[i];
    delete arr;
    return 0;   
}
