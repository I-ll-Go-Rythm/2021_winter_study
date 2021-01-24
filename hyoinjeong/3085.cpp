#include <iostream>
#include <algorithm>
using namespace std;


int count(char** board,int n)
{
	//c,p,z,y
	int arr1[3]={0};
	int arr2[3]={0};
	for(int i=1;*(board[i])!=0;i++)
	{
		switch(board[i][n])
		{
			case 'C':
				arr1[0]++;
				break;
			case 'P':
				arr1[1]++;
				break;
			case 'Z':
				arr1[2]++;
				break;
			case 'Y':
				arr1[3]++;
				break;
		}
	}
	for(int i=1;(board[n][i])!=0;i++)
	{
		switch(board[n][i])
		{
			case 'C':
				arr2[0]++;
				break;
			case 'P':
				arr2[1]++;
				break;
			case 'Z':
				arr2[2]++;
				break;
			case 'Y':
				arr2[3]++;
				break;
		}
	}
	
	return (*max_element(arr1,arr1+3)>*max_element(arr2,arr2+3)? *max_element(arr1,arr1+3):*max_element(arr2,arr2+3));
}

int main()
{
	int n;
	char color;
	cin>>n;
	char** board;
	for(int i=1;i<=n;i++)
	{
		for(int j=1;j<=n;j++)
		{
			cin>>color;
			board[i][j]=color;
		}
	}
	cout<<count(board,2);
	
}