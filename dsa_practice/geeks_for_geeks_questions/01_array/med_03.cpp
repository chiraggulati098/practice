// Rearrange an array according to given indexes

#include <iostream>
using namespace std;

void print_array(int arr[],int n)   // function to print array taking in array and size as argument
{
    cout<<"\narray:\t";
    for (int i=0;i<n;i++)   {
        cout<<arr[i]<<"\t";
    }
}   

void enter_elements(int arr[],int n)    // function to input elements of array
{
    cout<<"enter "<<n<<" terms: \n";
    for (int i=0;i<n;i++)   {
        cin>>arr[i];
    }
}

int enter_size()    // function to input size of array from user
{
    int n;
    cout<<"enter size of array: ";
    cin>>n;
    return n;
}

void remap_array(int arr[],int index[],int n)
{
    int temp[n];
    for (int i = 0;i<n;i++) {
        temp[index[i]] = arr[i]; 
    }

    for (int i = 0;i<n;i++) {
        arr[i] = temp[i]; 
    }
}

int main()  
{
    int n = enter_size(),arr[1000],index[1000];
    enter_elements(arr,n);

    cout<<"enter "<<n<<" indexes: \n";
    for (int i=0;i<n;i++)   {
        cin>>index[i];
    }
    remap_array(arr,index,n);
    print_array(arr,n);
    cout<<endl;

    return 0;
}