#include <stdio.h>
#include <math.h>
#include <vector>
using namespace std;

void sc(vector<int> &arr, int num, int jari) {
    int a = num / pow(10, jari-1);
    int val = (a-1) * pow(10, jari) + a;
    for(int i = jari-1; i>0;i--) {
        val += 9*pow(10,i) + 9;
    }
    if(val > num) {
        arr.push_back(--a);
        if(jari == 1) return;
        num = num - a*pow(10,jari) - a;
        sc(arr, num, --jari);
    }
    else{
        arr.push_back(a);
        if(jari == 1) return;
        num = num - a*pow(10, jari) - a;
        sc(arr, num, --jari);
    }
}

int main(void) {
    vector<int> vec;
    int no;
    int p = 1;
    int sum = 0;
    scanf("%d", &no);
    
    while(no/pow(10, p) != 0) { // get no's # of digits
        p++;
    }
    sc(vec, no, p);
    
    for(int i = 0; i<vec.size(); i++) {
        sum += vec[i] * pow(10, p-i-1); 
    }
    return sum;
}
