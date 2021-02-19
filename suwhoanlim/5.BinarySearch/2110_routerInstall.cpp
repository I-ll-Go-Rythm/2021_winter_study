// https://mygumi.tistory.com/301
// I hate working with indices..
// I don't think this code should work
// how come mid = (lo+hi)/2 can be exactly the distance between two routers?
// what if no house exists on that particular coordinate?

#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;
typedef long long ll;
int main(void) {
    int N, C;
    cin >> N >> C;
    int *arr = new int[N];
    for(int i = 0; i < N; i++) 
        cin >> arr[i];
    sort(arr, arr + N);
    
    int hi = arr[N-1] - arr[0], lo = 0, mid, sum, cnt, idx, ans = 0; //min_dist = INT_MAX;
    
    while(lo <= hi) {
        mid = (hi+lo)/2;
        sum = 0; cnt = 1; idx = 0;
        for(int i = 1; i < N; i++) {
            sum += arr[i] - arr[i-1];
            if(sum >= mid) {
                sum = 0;
                cnt++;
                //min_dist = min_dist < arr[i] - arr[idx] ? min_dist : arr[i] - arr[idx];
                idx = i;
            }
        }
        
        if (cnt >= C) {
            // 공유기의 수를 줄이자 => 간격 넓히기
            ans = mid;
            lo = mid + 1;
        } else {
            // 공유기가 더 설치되어야한다. => 간격 좁히기
            hi = mid - 1;
        }
    /*
        if(cnt >= C) lo = mid;
        else hi = mid;
        //printf("%d %d %d %d %d\n", lo, mid, hi, sum, cnt);
    }
    */
    }
    cout << ans << '\n';
    delete arr;
    return 0;
}
