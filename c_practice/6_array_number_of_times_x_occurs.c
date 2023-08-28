#include<stdio.h>

void number_of_times(int arr[100],int n,int search)
{
	int count = 0;
	for(int i=0;i<n;i++)	{
		if (arr[i] == search)	{
			printf("%d is found at index %d\n",search,i);
			count ++;
		}
	}

	printf("\nnumber of times %d was in the array is %d\n",search,count);
}

int main()
{
	int arr[100],n,search;
	printf("how many terms do you want in the array: ");
	scanf("%d",&n);

	printf("enter %d terms for the array:\n",n);
	
	for (int i=0;i<n;i++)	{
		scanf("%d",&arr[i]);
	}

	printf("enter element to search: ");
	scanf("%d",&search);

	number_of_times(arr,n,search);

	return 0;
}
