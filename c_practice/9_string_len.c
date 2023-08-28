#include<stdio.h>
#include<string.h>

int main()
{
	char name[100];
	printf("enter name: ");
	fgets(name,100,stdin);
	int count = 0;
	for(int i=0;name[i]!='\0';i++)	{
		count++;
	}
	printf("count is %d\n",count-1);
	return 0;
}
