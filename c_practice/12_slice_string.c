#include <stdio.h>
#include <string.h>

void slicestr(char sin[],char slice[],int n,int m)
{
	int j = 0;
	for (int i=n;i<=m;i++)	{
		slice[j] = sin[i];
		j++;
	}
	slice[j] = '\0';
}

int main()
{
	char sin[100];
	char slice[100];
	int n,m;
	printf("enter string: ");
	gets(sin);
	printf("enter n and m:\n");
	scanf("%d%d",&n,&m);
	slicestr(sin,slice,n,m);
	printf("sliced string is %s\n",slice);
	return 0;
}
