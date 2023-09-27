// Rearrange positive and negative numbers alternatively in array

#include <iostream>
using namespace std;

#include <iostream>
using namespace std;

void print_array(int arr[],int n)   
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

void sort_array(int arr[],int n) 
{
    int temp,found;
    for (int i = 0;i<n;i++) {
        found = 0;
        if (i%2 == 0)   {
            if (arr[i] >= 0)    {
                found = 1;
                continue;
            }
            else    {
                for (int j=i+1;j<n;j++) {
                    if (arr[j]>=0)  {
                        temp = arr[i];
                        arr[i] = arr[j];
                        arr[j] = temp;
                        found = 1;
                    }
                }
            }
        }
        else    {
            if (arr[i] < 0)    {
                found = 1;
                continue;
            }
            else    {
                for (int j=i+1;j<n;j++) {
                    if (arr[j]<0)  {
                        temp = arr[i];
                        arr[i] = arr[j];
                        arr[j] = temp;
                        found = 1;
                    }
                }
            }
        }
        if (found == 0) {
            break;
        }
    }
}

int main()  
{
    int n,arr[1000];
    cout<<"enter number of terms in array: ";
    cin>>n;

    enter_elements(arr,n);
    sort_array(arr,n);
    print_array(arr,n);

    cout<<endl;
    return 0;
}