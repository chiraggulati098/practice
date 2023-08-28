#include<stdio.h>

int max_in_array(int arr[100],int n)
{
	int max = arr[0];
	for (int i=0;i<n;i++)	{
		if (max < arr[i])	{
			max = arr[i];
		}	
	}
	return max;
}

int main()
{
	int arr[100],n;
	printf("how many terms do you want in the array: ");
	scanf("%d",&n);
	printf("enter %d terms for the array:\n",n);
	for (int i=0;i<n;i++)	{
		scanf("%d",&arr[i]);
	}
	printf("max in the array is %d\n",max_in_array(arr,n));
	return 0;
}
