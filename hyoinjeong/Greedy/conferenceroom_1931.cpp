#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int N;
	cin>>N;
	vector<pair<int,int>> conferences;
	int start,end;
	for(int i=0;i<N;i++)
	{
		cin>>start>>end;
		conferences.push_back(make_pair(start,end));
	}
	sort(conferences.begin(),conferences.end());
	int count = 1;
	int temp = 0;
	int maximum = 1;
	for(int i=0;i<conferences.size()-1;i++)
	{
		
		if(temp<=conferences[i].first)
		{
			count++;
			temp = conferences[i].second;	
		}
		
		
		for(int j=i+1;j<conferences.size();j++)
		{
			if(temp<=conferences[j].first)
			{
				count++;
				temp = conferences[j].second;
			}
		}
		maximum = max(maximum,count);
		count = 1;
	}
	cout<<maximum<<endl;
}