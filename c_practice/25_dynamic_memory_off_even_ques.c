#include<stdio.h>
#include<stdlib.h>

int main()
{
	int *ptr;
	ptr = (int *) calloc(2,sizeof(int));
	ptr[0] = 1;
	ptr[1] = 3;
	printf("odd nos: ");
	for (int i=0;i<2;i++)
		printf("%d ",ptr[i]);
	
	ptr = realloc(ptr,3);
	ptr[0] = 2;
	ptr[1] = 4;
	ptr[2] = 6;
	printf("\neven nos: ");
	for (int i=0;i<3;i++)
		printf("%d ",ptr[i]);
	printf("\n");
	free(ptr);

	return 0;
}
