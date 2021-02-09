#include <bits/stdc++.h>

using namespace std;

long long sb(int n, bool k)
{
	if(n==1)
		return (long long)1;
	if(k==1)
    {
        return sb(n-1,0);
    }
    else if(k==0)
    {
        return sb(n-1,0)+sb(n-2,0);
    }
}

int main()
{
	int N;
	cin>>N;
	cout<<sb(N,1)<<endl;
	return 0;
}