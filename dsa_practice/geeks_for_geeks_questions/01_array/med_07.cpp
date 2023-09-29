//Find the smallest missing number

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

int find_max(int arr[],int n)
{
    int max = arr[0];
    for (int i=0;i<n;i++)   {
        if (max<arr[i]) {
            max=arr[i];
        }
    }
    return max;
}

int main()
{
    int n = input_size(),arr[10000],found,m;
    input_array(arr,n);
    m = find_max(arr,n);
    for (int num=0;num<m;num++)   {
        found = 0;
        for (int i=0;i<n;i++)   {
            if (arr[i] == num)  {
                found = 1;
            }
        }
        if (found == 0) {
            cout<<"Min Number not in Array is: "<<num<<endl;
            break;
        }
    }

    return 0;
}