#include <stdio.h>
#include <string.h>

int main()
{
	char password[100];
	printf("enter your password: ");
	gets(password);
	strcat(password,"abc");
	printf("pass is %s\n",password);
	return 0;
}
