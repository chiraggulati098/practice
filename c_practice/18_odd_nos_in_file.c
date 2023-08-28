#include<stdio.h>

int main()
{
	FILE *f;
	f = fopen("18_file_oddnos.txt","w");
	int n;
	printf("enter n: ");
	scanf("%d",&n);

	for (int i = 1;i <= n;i++)	{
		if (i % 2 == 0)
			continue;
		else	{
			fprintf(f,"%d\t",i);
		}
	}
	fprintf(f,"\n");
	fclose(f);

	return 0;
}
