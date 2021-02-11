#include <bits/stdc++.h>

using namespace std;



int main()
{
	int n;
	int p[1001];
	int dp[1001];
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		cin>>p[i];
		dp[i]=p[i];
	}
	for(int i=2;i<=n;i++)
	{
		for(int j=1;j<=(i/2);j++)
		{
			//cout<<"p[i]: "<<p[i]<<"  dp[i-j]+dp[j]:  "<<dp[i-j]+dp[j]<<endl;
			dp[i]=max(dp[i],dp[i-j]+dp[j]);	
			//cout<<"i : "<<i<<" j : "<<j<<"dp[i] : "<<dp[i]<<endl;
		}
	}
	cout<<dp[n];
}