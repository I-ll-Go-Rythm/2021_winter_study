#include <bits/stdc++.h>

using namespace std;

int main()
{
	int n;
	int dp[1001];
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		cin>>dp[i];
	}
	for(int i=2;i<=n;i++)
	{
		for(int j=1;j<=(i/2);j++)
		{
			dp[i]=max(dp[i],dp[i-j]+dp[j]);	
		}
	}
	cout<<dp[n];
}