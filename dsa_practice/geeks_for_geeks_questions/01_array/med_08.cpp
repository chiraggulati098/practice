// Difference Array | Range Update Query

#include <iostream>
using namespace std;

int input_size()   
{
    int n;
    cout<<"enter num of elements: ";
    cin>>n;
    return n;
}

void input_array(int arr[],int n)  
{
    cout<<"enter "<<n<<" terms:\n";
    for (int i=0;i<n;i++)   {
        cin>>arr[i];
    }
}

void print_array(int arr[],int n)   // function to print array taking in array and size as argument
{
    cout<<"\narray:\t";
    for (int i=0;i<n;i++)   {
        cout<<arr[i]<<"  ";
    }
    cout<<endl;
}   

void update_array(int arr[],int n)
{
    int value,start,stop;
    cout<<"enter value to add: ";
    cin>>value;
    cout<<"enter starting and stoping index:\n";
    cin>>start>>stop;

    for (int i=start;i<=stop;i++)   {
        arr[i]+=value;
    }
}

int main()
{
    int n = input_size(),arr[10000];
    input_array(arr,n);
    
    update_array(arr,n);
    print_array(arr,n);

    return 0;
}