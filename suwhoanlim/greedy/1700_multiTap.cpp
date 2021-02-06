// https://jaimemin.tistory.com/759
#include <iostream>
#include <algorithm>
using namespace std;

const int MAX = 100 + 1;
int N, K;
int schedule[MAX], plug[MAX];

int main(void){
        //ios_base::sync_with_stdio(0);
        //cin.tie(0); //cin 실행속도 향상
        cin >> N >> K;

        for (int i = 0; i < K; i++)
            cin >> schedule[i];
        int result = 0;

        for (int i = 0; i < K; i++) {
                 bool pluggedIn = false;
                 for (int j = 0; j < N; j++)
                         if (plug[j] == schedule[i]) {
                                 pluggedIn = true;
                                 break;
                         }

                 if (pluggedIn)
                         continue;
                 for (int j = 0; j < N; j++)
                         if (!plug[j]){
                                 plug[j] = schedule[i];
                                 pluggedIn = true;
                                 break;
                         }
                 if (pluggedIn)
                         continue;

                 int idx, deviceIdx = -1;
                 for (int j = 0; j < N; j++){
                         int lastIdx= 0;
                         for (int k = i + 1; k < K; k++){
                                 if (plug[j] == schedule[k])
                                         break;
                                 lastIdx++;
                         }

                         if (lastIdx > deviceIdx){
                                 idx = j;
                                 deviceIdx = lastIdx;
                         }
                 }
                 result++;
                 plug[idx] = schedule[i];
        }
        cout << result << "\n";
        return 0;
}
