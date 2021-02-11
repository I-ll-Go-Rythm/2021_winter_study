#include <iostream>
using namespace std;
// need to initialize a and b every time use, olse the valus will accumulate
typedef long long ll;
ll a[10];
ll b[10];

int main(void) {
    int N, n;
    ll sum = 0;
    cin >> N;
    n = N;
    if(N==1) {cout << 10 << '\n'; return 0;}
        
    for(int i = 0; i < 10; i++)
        a[i]++;
    b[9] = 1;
    for(int i = 0; i < N - 1; i ++) {
        if(i % 2 == 0) { // N %2 == 0
            for(int k = 0; k < 9; k++){ 
                b[k] = 0;
                for(int j = k; j < 10; j++)
                    b[k] = (b[k] + a[j]) % 10007;
            }
        }
        else { // N % 2 == 1
            for(int k = 0; k < 9; k++) {
                a[k] = 0;
                for(int j = k; j < 10; j++)
                    a[k] = (a[k] + b[j]) % 10007;
            }
        }
    }
    
    if((n%2) == 0)
        for(int i = 0; i < 10; i++)
            sum += b[i];
    else
        for(int i = 0; i < 10; i++)
            sum += a[i];
    cout << sum  % 10007 << '\n';    
    
    return 0;
}
