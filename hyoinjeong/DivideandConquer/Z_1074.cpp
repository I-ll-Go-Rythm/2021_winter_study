#include <bits/stdc++.h>

using namespace std;

vector<vector<int>> arr(pow(2,15));
int cnt;

void z(int i, int j ,int n)
{
	if(n==1)
	{
		arr[i][j]=cnt;
		cnt++;
		return;
	}
	int div=n/2;
	for(int x=0;x<2;x++)
	{
		for(int y=0;y<2;y++)
		{
			z(i+(x*div),j+(y*div),div);
		}
	}
}

int main()
{
	int N,r,c;
	cin>>N>>r>>c;
	vector<int> row((int)pow(2,15));
	for(int i=0;i<(int)pow(2,N);i++)
	{
		arr.push_back(row);
	}
	z(0,0,(int)pow(2,N));
	cout<<arr[r][c];
	return 0;
}