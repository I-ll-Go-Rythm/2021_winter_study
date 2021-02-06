#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;

int main(void) {
    int tmp;
    int sum = 0; // Not initializing this part caused an error on the consequitive tests!
    vector<int> nan;
    for(int i = 0; i < 9; i++) {
 	printf("%dth trial: ", i);
        scanf("%d", &tmp); // scanf("%d\n", &nan[i]);, scanf("%d\n", &tmp) caused an error
        //scanf("%d\n", &tmp); // why does this line doesn't work?

        nan.push_back(tmp);
        sum += tmp;
    }

	for (auto tmp = nan.begin(); tmp != nan.end(); tmp++)
	    printf("%d\n", *tmp);


    sort(nan.begin(), nan.end());
    tmp = 0;
    int i, j;
    bool k = 0;
    for(i = 0; i <8; i++) {
        for(j = i+1; j<9; j++){
            tmp = sum - nan[i] - nan[j];
            if(tmp == 100) {k = 1; break;}
        }
        if(k == 1) break;
    }
    
    for(int m = 0; m < 9; m++) {
        if(m == i || m == j) continue;
        printf("%d\n", nan[m]);
    }
    
    return 0;
}
