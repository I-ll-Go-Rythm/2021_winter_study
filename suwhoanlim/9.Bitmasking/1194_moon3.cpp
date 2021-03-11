nt t = 0;
            t = aaa & 448;
            t = t >> 6;
            
            if(t != 1) {
                aaa &= 63; q.push(a+1); q.push(aa); q.push(aaa);    
            }
            if(t != 0) {
                aaa &= 63; aaa |= 64; q.push(a-1); q.push(aa); q.push(aaa);
            }
            if(t != 2) {
                aaa &= 63; aaa |= 192; q.push(a); q.push(aa-1); q.push(aaa);
            }
            if(t != 3) {
                aaa &= 63; aaa |= 128; q.push(a); q.push(aa+1); q.push(aaa);
            }
        }
        ++howmany;
    }
}


int main(void) {
    int x, y;
    cin >> N >> M;
    
    for(int i = 1; i <= N; i++)
        for(int j = 1; j <= M; j++) {
            cin >> arr[i][j];
            if(arr[i][j] == '0') {y = i; x = j;}
        }
    
    bfs(y, x, 256);
    cout << howmany << '\n';
    
    return 0;
}
