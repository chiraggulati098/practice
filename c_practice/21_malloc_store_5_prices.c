#include<stdio.h>
#include<stdlib.h>

int main()
{
	float *ptr;
	ptr = (float *) malloc(5* sizeof(float));

	ptr[0] = 214;
	ptr[1] = 234;
	ptr[2] = 624;
	ptr[3] = 452;
	ptr[4] = 234;

	for(int i = 0;i<5;i++)	
		printf("%f\n",ptr[i]);

	return 0;
}
