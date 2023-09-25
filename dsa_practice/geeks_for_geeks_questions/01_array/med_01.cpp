#include <iostream>
using namespace std;

void print_array(int arr[],int n)   // function to print array taking in array and size as argument
{
    cout<<"\narray:\t";
    for (int i=0;i<n;i++)   {
        cout<<arr[i]<<"\t";
    }
}  

int main()  
{
    int n,initial_arr[1000],final_arr[1000];
    cout<<"enter num of elements: ";
    cin>>n;

    cout<<"enter "<<n<<" elements:\n";
    for (int i=0;i<n;i++)   {
        cin>>initial_arr[i];
    }

    print_array(initial_arr,n);

    for (int i = 0;i<n;i++) {
        int temp = 1;
        for (int j=0;j<n;j++)   {
            if (i==initial_arr[j])  {
                final_arr[i] = i;
                temp = 0;
            }
        }
        if (temp == 1)   {
            final_arr[i] = -1;
        }
    }

    print_array(final_arr,n);
    cout<<endl;
    return 0;
}