#include <iostream>
#include <algorithm>
using namespace std;

typedef long long ll;

int main(void) {
    int l, w, h, n, ans = 0;
    ll cnt = 0;
    int arr[20] = {0};
    cin >> l >> w >> h >> n;
    for(int i = 0, tmp; i < n; i++) {
        cin >> tmp;
        cin >> arr[tmp];
    }
    for (int i = 19; i >= 0; i--) {
		cnt <<= 3;
		ll tmp = min((ll)arr[i], (ll)(l>>i)*(w>>i)*(h>>i)-cnt);
		cnt += tmp, ans += tmp;
	}

    cout << (cnt == (ll)l*w*h ? ans : -1) << '\n';
    
	return 0;
}
