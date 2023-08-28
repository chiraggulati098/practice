#include<stdio.h>

int main()
{
	int arr[100],n,condition,number = 0;
	printf("how many terms do you want in the array: ");
	scanf("%d",&n);
	printf("enter %d terms for the array:\n",n);
	for (int i=0;i<n;i++)	{
		scanf("%d",&arr[i]);
	}
	loop:
	printf("\nthe array is: \n");
	for (int i=0;i<n+number;i++)	{
		printf("%d\t",arr[i]);
	}
	not_valid_entry:
	condition = 0;
	printf("\npress 1 and enter if you want to put another term in the end of the array and press 2 if you just want to exit: ");
	scanf("%d",&condition);
	if (condition==1)	{
		printf("enter the term you want to put in the array: ");
		scanf("%d",&arr[n+number]);
		number++;
		goto loop;
	}
	else if (condition==2)	{
		return 0;
	}
	else	{
		printf("enter a valid choice\n");
		goto not_valid_entry;
	}
}
