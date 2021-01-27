#include <iostream>

using namespace std;

int func(int* arr,int s,int i,bool ox)//1-2,-1,0,0/1
{
	int size=sizeof(arr)/sizeof(arr[0]);//2
	if(i==size)//2
	{
		return 0;
	}
	int pandog[2];
	if(ox)//0/1
	{
		pandog[0]=func(arr,s,i+1,0);//1-2,-1,0,0->1-2,-1,1,0
		pandog[1]=func(arr,s,i+1,1);//1-2,-1,0,0->1-2,-1,1,1
	}
	else
	{
		pandog[0]=arr[i]+func(arr,s,i+1,0);//1-2,-1,0,0->1+(1-2,-1,1,0)
		pandog[1]=arr[i]+func(arr,s,i+1,1);//1-2,-1,0,0->1+(1-2,-1,1,1)
	}
	for(int j=0;j<2;j++)
	{
		if(pandog[j]==s)
		{
			return 1;
		}
		else
		{
			return 0;
		}
	}
	return pandog[0]+pandog[1];
}

int main()
{
	int N,S;
	cin>>N;//3
	cin>>S;//3
	int numbers[N];
	for(int i=0;i<N;i++)
	{
		cin>>numbers[i];//1,2,3
	}
	int count1 = func(numbers,S,0,0);//1-2,-1,0,0
	int count2 = func(numbers,S,0,1);//1-2,-1,0,1
	cout<<count1+count2-1<<endl;
}