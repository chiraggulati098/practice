#include <stdio.h>
#include <string.h>

typedef struct vector	{
	int x;
	int y;
}vec;

void sumv(vec v1, vec v2, vec sum)	
{
	sum.x = v1.x+v2.x;
	sum.y = v1.y+v2.y;
	printf("sum of vectors is %di + %dj\n",sum.x,sum.y);
}

int main()
{
	vec v1 = {5, 10};
	vec v2 = {3, 10};
	vec sum = {0};	
	sumv(v1,v2,sum);
	return 0;
}
