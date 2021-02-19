#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;
typedef long long ll;

int main(void) {
    int N, M;
    cin >> N >> M;
    int *arr = new int[N];
    for(int i = 0; i < N; i++) 
        cin >> arr[i];
    
    int hi = INT_MAX, lo = 0, mid, sum, cnt;
    
    while(lo + 1 < hi) {
        mid = (hi+lo)/2;
        sum = 0; cnt = 1;
        for(int i = 0; i < N; i++) {
            sum += arr[i];
            if(sum > mid) {
                if(arr[i] > mid) {cnt = M+1; break;}
                //Above line accounts for the case where 
                //the length of the lesson is larger than the mid value
                sum = 0;
                i--;
                cnt++;
            }
        }
        if(cnt > M) lo = mid;
        else hi = mid;
        //printf("%d %d %d %d %d\n", lo, mid, hi, sum, cnt);
    }
    
    cout << hi << '\n';
    delete arr;
    return 0;
}
