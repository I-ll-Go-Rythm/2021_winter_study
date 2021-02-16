#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;

int N;
vector<int> v;
vector<ll> sum(100002, 0);
//int COUNT = 0;

ll solution(int s, int e) {
//	++COUNT;
//	cout << "Entering " << COUNT << " Solution, ";
//	cout << "start index is " << s << ", end index is " << e << endl;

	if(e-s == 1) {
//		cout << "\t\t\t\t\t\t\t\tBase Case, return " <<  v[s]*(sum[s] - sum[s-1]) << endl;
		return (ll) v[s]*(sum[s] - sum[s-1]);
	}

	int mid = (s+e-1)/2;

	ll L_res = solution(s, mid+1);
//	cout << "\t\t\t\t\t\tL_res solution Done" << endl;
//	cout << "Again Entering, "  << "start index is " << s << ", end index is " << e << endl;

	ll R_res = solution(mid+1, e);
//	cout << "\t\t\t\t\t\tR_res solution Done" << endl;
//	cout << "Again Entering, "  << "start index is " << s << ", end index is " << e << endl;

	ll res = max(L_res, R_res);

	ll sum_e = sum[mid] - sum[mid-1];
	int min_e = v[mid];

	ll M_res = sum_e * min_e;
	int l = mid, r = mid;
	ll L_min, R_min;
	while(s<=l && r<=e-1) {
		if(s<l && r<e-1) {
			L_min = min(min_e, v[l-1]);
			L_min *= (sum_e + v[l-1]); // 36
			R_min = min(min_e, v[r+1]);
			R_min *= (sum_e + v[r+1]); // 
		}
		else if(s==l && r<e-1) {
			L_min = 0;
			R_min = min(min_e, v[r+1]);
			R_min *= (sum_e + v[r+1]); // 
		}
		else if(s<l && r==e-1) {
			R_min = 0;
			L_min = min(min_e, v[l-1]);
			L_min *= (sum_e + v[l-1]); // 36
		}


		if(L_min < R_min) {
			M_res = max(M_res, R_min);
			min_e = min(min_e, v[r+1]);
			sum_e += v[++r];
		}
		else {
			M_res = max(M_res, L_min);
			min_e = min(min_e, v[l-1]);
			sum_e += v[--l];
		}
	}

//	cout << "\t\t\t\t\t\tM_res is " << M_res << endl;
	res = max(res, M_res);
//	cout << "\t\t\t\t\t\tNot Base Case, return " << res << endl;
	return res;
}

int main() {
	cin >> N;
	v.resize(N+1); sum.resize(N+1);

	int input, temp = 0;
	for(int i=0; i<N; i++) {
		cin >> input;
		v[i+1] = input;
		temp += input;
		sum[i+1] = temp; // i to j(involved) -> sum[j] - sum[i-1]
	}
	/*
	for(int i=0; i<sum.size(); i++) {
		cout << sum[i] << endl;
	}
	*/
	cout << solution(1, N+1) << endl;

	return 0;
}

	

