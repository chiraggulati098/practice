// Find the rotation Count in a Rotated Sorted Array

#include <iostream>
using namespace std;

int count_rotations(int arr[],int n)
{
    int min = arr[0],min_index=0;
    for (int i=0;i<n;i++)   {
        if (arr[i]<min) {
            min = arr[i];
            min_index = i;
        }
    }
    return min_index;
}

int main()
{
    int arr[] = {15,18,19,2,3,6,12};
    int n = sizeof(arr)/sizeof(int);
    cout<<"the array was rotated "<<count_rotations(arr,n)<<" times"<<endl;
    return 0;
}