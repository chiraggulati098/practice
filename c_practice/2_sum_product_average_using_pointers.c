#include<stdio.h>

void dowork (int a, int b,int *sum,int *multi,int *avg)	{
	*sum = a + b;
	*multi = a*b;
	*avg = (a+b)/2;
}

int main()
{
	int a = 3, b = 5;
	int sum, multi, avg;
	dowork(a,b,&sum,&multi,&avg);
	printf("sum is %d\nproduct is %d\naverage is %d\n",sum,multi,avg);
	return 0;
}
