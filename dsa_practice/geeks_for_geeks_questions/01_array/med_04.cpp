// Search an element in a sorted and rotated array

#include <iostream>
using namespace std;

int find_pivot(int arr[],int n)
{
    for (int i=0;i<n;i++)   {
        if (arr[i+1]<arr[i])    {
            return i;
        }
    }
    return -1;
}

void binary_search(int arr[],int n,int key,int low, int high)
{
    int found = 0,mid;
    while (low!=high)    {
        mid = (low+high)/2;
        if (arr[mid]==key)  {
            cout<<key<<" found at index "<<mid;
            found = 1;
            break;
        }
        else if (key<arr[mid])  {
            high = mid-1;
        }
        else    {
            low = mid+1;
        }
    }
    if (found == 0) {
        cout<<key<<" not found in array";
    }
}

int main()
{
    int arr[] = {5,6,7,8,9,10,1,2,3,4};
    int n = sizeof(arr)/sizeof(int);
    int key = 3,low,high;

    int pivot_index = find_pivot(arr,n);
    if (pivot_index == -1)  {
        low = 0;
        high = n-1;
    }
    else if (arr[0] <= key) {
        binary_search(arr,n,key,0,pivot_index);
    }
    else    {
        binary_search(arr,n,key,pivot_index+1,n-1);
    }

    cout<<endl;

    return 0;
}