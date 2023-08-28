#include<stdio.h>

int main()
{
	FILE *fptrw;
	FILE *fptr;
	fptrw = fopen("16_file.txt","w");
	char ch;
	printf("enter 5 char:\n");
	for(int i = 0;i<5;i++)	{
		scanf("%c",&ch);
		fprintf(fptrw,"%c",ch);
	}
	fclose(fptrw);

	fptr = fopen("16_file.txt","r");
	fscanf(fptr,"%c",&ch);
	printf("char = %c\n",ch);
	fscanf(fptr,"%c",&ch);
	printf("char = %c\n",ch);
	fscanf(fptr,"%c",&ch);
	printf("char = %c\n",ch);
	fscanf(fptr,"%c\n",&ch);
	printf("char = %c\n",ch);
	fscanf(fptr,"%c",&ch);
	printf("char = %c\n",ch);
	fclose(fptr);

	FILE *fptr2;
	fptr2 = fopen("demofile34523432.txt","r");
	if (fptr2 == NULL)
		printf("\nfile doesn't exist\n");
	else 
		fclose(fptr2);

	FILE *fptr3;
	fptr3 = fopen("16_new_file_create.txt","w");
	fputc('A',fptr3);
	fputc('B',fptr3);
	fputc('C',fptr3);
	fclose(fptr3);

	FILE *fptr4;
	fptr4 = fopen("16_new_file_create.txt","r");
	for (int i=1; i<=3;i++)	{
		printf("%c\n",fgetc(fptr3));
	}
	fclose(fptr4);

	return 0;
}
