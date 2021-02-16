//// http://wookje.dance/2017/02/20/boj-1300-K번째-수/
#include <stdio.h>
#include <algorithm>

int main() {
	int N, K;
	scanf("%d %d", &N, &K);

	int left = 1, right = K, ans;
	while (left <= right) {
		long long cnt = 0;
		int mid = (left + right) / 2;
		for (int i = 1; i <= N; i++) cnt += std::min(mid / i, N);
		if (cnt < K) left = mid + 1;
		else ans = mid, right = mid - 1;
	}
	printf("%d", ans);

	return 0;
}
