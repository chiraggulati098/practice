#include<stdio.h>

float fact(int i)
{
	if (i == 1)
		return i;
	else	{
		return i*fact(i-1);
	}
}

int main()
{
	float sum=0;
	int num;
	printf("enter num: ");
	scanf("%d",&num);
	for (int i=1;i<=num;i++)	{
		sum = sum + (1/fact(i));
	}
	printf("answer is %f\n",sum);
}
