#include <stdio.h>
#include <string>
#include <cstring>
#include <vector>
#include <iostream>

using namespace std;

int main()
{
	int n;
	scanf("%d",&n);
	char num[n][3];
	int strike[n],ball[n];
	for(int i=0;i<n;i++)
	{
		scanf("%s %d %d",num[i],&strike[i],&ball[i]);
	}
	
	vector<string> answers;
	int x,y,z;
	for(int i=123;i<988;i++)
	{
		string k = to_string(i);
		if(k.find('0')==-1)
		{
			if((k[0]!=k[1])&&(k[0]!=k[2])&&(k[1]!=k[2]))
			{
				answers.push_back(k);
			}
		}
	}
	
	//ans:324, 123
	int count=0;
	int fakestrike=0;
	int fakeball=0;
	for(int j=0;j<n;j++)
	{
		for(int i=0;i<answers.size();i++)
		{
			for(int k=0;k<3;k++)
			{
				if(strchr(num[j],answers[i][k])!=NULL)// 324에서 123이 있는가? 1일때 없으므로 스킵, 2일때 있는데 if문에서 걸려서 fakestrike++, 3일때 fakeball++
				{
					if((answers[i][k])==(num[j][k]))
					{
						fakestrike++;
					}
					else
					{
						fakeball++;
					}
				}
			}//여기서 123 입력값일때 1S 1B
			if((fakestrike==strike[j])&&(fakeball==ball[j]))
			{
				count++;
				fakestrike=0;
				fakeball=0;
			}
			fakestrike=0;
			fakeball=0;
			
		}
	}
	
	cout<<count<<endl;
	return 0;
}
