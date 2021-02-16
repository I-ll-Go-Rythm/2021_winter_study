/*
keep a counter variable
for every for loop, count the number of dotori and update counter variable.
    do it!
*/

#include <iostream>
#include <climits>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;
typedef long long ll;

int main(void) {
    ll N, K, D, cnt = 0;
    int t1, t2, t3;
    cin >> N >> K >> D;
    int dmin = INT_MAX, dmax = -1;
    int **arr = new int*[K];
    for(int i = 0; i < K; ++i) {
        arr[i] = new int[3];
        cin >> arr[i][0] >> arr[i][1] >> arr[i][2];
        dmin = arr[i][0] > dmin ? dmin : arr[i][0];
        dmax = dmax > arr[i][1] ? dmax : arr[i][1];
    }
    int mid;
    while(dmin + 1 < dmax) {
        mid = (dmax + dmin) / 2;
        cnt = 0;
        for(int i = 0; i < K; ++i) {
            if(arr[i][0] > mid) continue;
            else if(mid == arr[i][0]) ++cnt;
            else if(mid > arr[i][1]) cnt += (arr[i][1] - arr[i][0]) / arr[i][2] +1;
            else cnt += (mid - arr[i][0]) / arr[i][2] +1;
            /* this part will cause a run time error
            for(int j = arr[i][0]; j <= mid && j <= arr[i][1]; j += arr[i][2]) {
                ++cnt;
                if(cnt >= D) break;
            }
            if(cnt >= D) break;
            */
        }
        
        if(cnt >= D) dmax = mid;
        else dmin = mid;
    }
    
    cout << dmax << '\n';
    
    for(int i = 0; i < K; i++)
        delete arr[i];
    delete arr;
    
    return 0;  
    
    
    /*
    map<int, int> mmp;
    
    for(int i = 0; i < K; ++i) {
        cin >> t1 >> t2 >> t3;
        for(int j = t1; j <= t2; j += t3) {
            if(mmp.find(j) == mmp.end()) mmp[j] = 1;
            else mmp[j] +=1;
            //++cnt;
        }
    }
    
    map<int, int>::iterator iter;
    
    for(iter = mmp.begin(); iter != mmp.end(); ++iter){
        D -= iter->second;
        if(D <= 0) {cnt = iter->first; break;}
    }
    
    cout << cnt << '\n';
    */
    /*
    vector<int> vec;
    vec.reserve(30000000); // 128mb can hold 32000000 integers
    for(int i = 0; i < K; ++i) {
        cin >> t1 >> t2 >> t3;
        for(int j = t1; j <= t2; j += t3) {
            vec.push_back(j);
            ++cnt;
        }
    }
    */
    
    /*
    int **arr = new int*[K];
    
    for(int i = 0; i < K; ++i) {
        arr[i] = new int[3];
        cin >> arr[i][0] >> arr[i][1] >> arr[i][2];
        for(int j = arr[i][0]; j <= arr[i][1]; j += arr[i][2]) {
            vec.push_back(j);
            ++cnt;
        }
    }
    
    sort(vec.begin(), vec.begin() + cnt);
    
    cout << vec[D-1] << '\n';
    */
    
    // no need to do this!
    // put possible boxes into a vector
    // sort the vector
    // increment the counter and if cnt == dotori then stop
    // print cnt
    
    
    /*
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
    */
    /*
    for(int i = 0; i < K; i++)
        delete arr[i];
    delete arr;
    */   
}

