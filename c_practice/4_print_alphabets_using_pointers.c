#include<stdio.h>

int main()
{
	char alphabet = 'a';
	char* ptr = &alphabet;
	while (alphabet <= 'z')	{
		printf("%c\t",alphabet);
		(*ptr)++;
	}
	printf("\n");
	return 0;
}
