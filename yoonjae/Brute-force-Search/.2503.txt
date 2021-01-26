#include <iostream>
#include <string>
#include <vector>

using namespace std;

int N;

int main() {
	cin >> N;
	vector<int> v_cand;
	vector<string> v_hint; vector<int> v_strike; vector<int> v_ball;

	for(int i=0; i<N; i++) {
		string num; int str; int ball;
		cin >> num;
		cin >> str >> ball;
		v_hint.push_back(num); v_strike.push_back(str); v_ball.push_back(ball);
	}

	for(int i=111; i<1000; i++) {
		string ans = to_string(i);
		if(ans[1] == '0'|| ans[2] == '0') continue;
		else if(ans[0] == ans[1]) continue;
		else if(ans[0] == ans[2]) continue;
		else if(ans[1] == ans[2]) continue;
		cout << "0: " <<  ans[0] << " 1: " << ans[1] << " 2: " << ans[2] << endl;

		int is_correct = 1;
		for(int j=0; j<N; j++) {
			int str = 0; int ball = 0;
			for(int k=0; k<3; k++) {
				if(ans[k] == v_hint[j][k]) ++str;
			}
			for(int k=0; k<3; k++) {
				for(int l=0; l<3; l++) {
					if(ans[k] == v_hint[j][l]) ++ball;
				}
			}
			ball -= str;

			if(v_strike[j] != str || v_ball[j] != ball) {
				is_correct = 0;
				break;
			}
		}

		if(is_correct == 1) {
//			cout << i << endl;
			v_cand.push_back(i);
		}
	}


	cout << v_cand.size() << endl;

	return 0;
}
