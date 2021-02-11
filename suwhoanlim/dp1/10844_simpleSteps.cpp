#include <iostream>
using namespace std;
//If you use something else rather than ll, it will cause an overflow error
typedef long long ll;
ll a[10];
ll b[10];

int main(void) {
    int N, n;
    ll sum = 0;
    cin >> N;
    n = N;
    if(N==1) {cout << 9 << '\n'; return 0;}
    else if (N==2) {cout << 17 << '\n'; return 0;}
        
    for(int i = 0; i < 10; i++)
        a[i]++;
    for(int i = 0; i < N - 1; i ++) {
        if(i % 2 == 0) { // N %2 == 0
            for(int i = 1; i < 9; i++)
                b[i] = (a[i-1] + a[i+1]) % 1000000000;
            b[9] = a[8]; b[0] = a[1]; 
        }
        else { // N % 2 == 1
            for(int i = 1; i < 9; i++)
                a[i] = (b[i-1] + b[i+1]) % 1000000000;
            a[9] = b[8]; a[0] = b[1];     
        }
    }
    
    if((n%2) == 0)
        for(int i = 1; i < 10; i++)
            sum += b[i];
    else
        for(int i = 1; i < 10; i++)
            sum += a[i];
    cout << sum  % 1000000000 << '\n';    
    
    return 0;
}
