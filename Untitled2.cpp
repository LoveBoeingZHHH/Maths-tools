#include <iostream>
#include<stdlib.h>
using namespace std;
void Show(int,int index[],int value[]);
bool judge(int,int ,int index[]);
void change(int ,int ,int index[],int value[]);
int main()
{
	int i,n,m;
	cout<<"������Ԫ�ظ���";
	cin>>n;
	cout<<"������ѡ����Ԫ��";
	cin>>m;
	ing index[n]={0},value[n];
	for(i=0;i<n;i++)
	{
		value[i]=i+1;
	}
	change(n,m,index,value);
	return 0;
}

void Show(int n,int index[],int value[])
{
	int i;
	for(i=0;i<n;i++)
	{
		if(index[i]) cout<<value[i]<<" ";
	
	}
	cout<<endl;
}

bool judge(int n,int m,int index[])
{
	int i;
	for(i=n-1;i>=n-m;i--)
	{
		if(!index[i] ) return false;
	}
	return ture;
}

void change(int n,int m,int index[],int value[])
{
	int i,j,num=0;
	for(i=0;i<m;i++)
	{
		index[i]=1;
	}
	Show(n,index,value);
	num +=1;
	while(!judge(n,m,index))
	{
		for(i=0;i<n-1,i++;
		{
			if(index[i]==1&&index[i+1]==0)
			{
				index[i]=0;
				index[i+1]=1;
				int count=0;
				for(j=0;j<i;j++)
				{
					if(index[i])
					{
						index[j]=0;
						index[count++]=1;
					}
				}
				Show(n,index,value);
				num+1;
				break;
			}
		}
	}
	cout<<"����"<<num<<"��"<<endl;
	system("pause");
	return 0;
}
