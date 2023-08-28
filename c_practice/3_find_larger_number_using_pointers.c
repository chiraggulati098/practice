#include<stdio.h>

void larger (int *a, int *b)
{
	if (*a>*b)	{
		printf("a is greater\n");
	}
	else	{
		printf("b is greater\n");
	}
}

int main()
{
	int a = 4, b = 7;
	larger (&a,&b);
	return 0;
}
