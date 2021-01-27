//There are three fatal errors in this problem
//Find them to prove you are worthy!

#include <iostream>
#include <stdio.h>
using namespace std;

int main(void) {
    int row, a, b, c, aa, bb, cc, str, ba, ss, bbaa;
    cin >> row;
    bool arr[1000];
    
    for(int i = 123 ; i <1000; i++) { // 메모리 효율성 그닥, 근데 보기는 편하잖아? mem eff < comp cost
        arr[i] = 0;
    }
    
    while(row) {
        cin >> aa >> str >> ba;
        bb = (aa/10)%10; cc = aa/10; aa = aa/100;
        for(int i = 123; i < 1000; i++) {
            if(arr[i] == -1) continue;
            ss = 0; bbaa = 0;
            a = i/100; b = (i/10)%10; c = i%10;
            if(aa == a) ss++;
            else if(aa == b || aa == c) bbaa++;
            if(bb == b) ss++;
            else if(bb == a || bb == c) bbaa++;
            if(cc == c) ss++;
            else if(cc == a || cc == b) bbaa++;
            
            if(bbaa == ba && ss == str) arr[i] = 1;
            else arr[i] = -1;
        }
        row--;
    }
    
    aa = 0;
    for(int i = 123; i < 1000; i++) {
	if(arr[i] == 1) aa++;     
    }
    cout << aa << endl;
    
    return 0;
}
