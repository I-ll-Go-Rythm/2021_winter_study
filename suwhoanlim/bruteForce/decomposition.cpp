#include <stdio.h>
#include <math.h>
#include <vector>
using namespace std;
int N;

int main(void) {
    int jari = 0;
    scanf("%d", &N);
    int cp = N;
    do {
        jari ++;
        cp = cp / 10;
    }while (cp);
    
    int con = N - 9 * jari;
    if(con <= 0) con = 1;
    cp = con;
    int conn = con;
    
    while(1) {
        while(conn){
            cp = cp + (conn % 10);
            conn = conn / 10;
        }
        if (cp == N || con == N) break;
        else {con++; cp = con; conn = con;} 
    }
    
    if(cp == N) printf("%d\n", con);
    else printf("0\n");
    
    return 0;
}
