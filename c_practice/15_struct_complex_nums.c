#include<stdio.h>
#include<string.h>

struct com	{
	int r;
	int img;
};

int main()
{	
	struct com n1 = {5,8};
	struct com *p = &n1;
	printf("number is %d + %di\n",p->r,p->img);
	return 0;
}
