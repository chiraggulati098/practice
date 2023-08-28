#include<stdio.h>

void _swap(int *a,int *b)
{
	int t = *a;
	*a = *b;
	*b = t;
}

int main()
{
	int x = 3, y = 5;
	_swap(&x,&y);
	printf("x = %d\ny = %d\n",x,y);
	return 0;
}
