//K-th largest sum contiguous subarray

#include <iostream>
using namespace std;

int input_size()
{
    int n;
    cout<<"enter size of array: ";
    cin>>n;
    return n;
}

void input_array(int arr[],int n)
{
    cout<<"enter "<<n<<" elements:\n";
    for (int i=0;i<n;i++)   {
        cin>>arr[i];
    }
}

int num_sum (int n) 
{
    if (n==0)   {
        return 0;
    }   
    else if (n==1)  {
        return 1;
    }   else    {
        return n+num_sum(n-1);
    }
}

void array_sort(int arr[],int n)    
{
    int min,temp;
    for (int i = 0;i<n;i++) {
        min = arr[i];
        for (int j=i+1;j<n;j++)   {
            if (arr[j]<min) {
                min = arr[j];
                temp = arr[i];
                arr[i] = min;
                arr[j] = temp;
            }
        }
    }
}

void result_print(int arr[],int n,int result_arr[],int key) 
{
    int sum,index = 0;
    for (int i = 0;i<n;i++) {
        sum = 0;
        for (int j = i;j<n;j++) {
            sum += arr[j];
            result_arr[index] = sum;
            index+=1;
        }
    }   

    array_sort(result_arr,num_sum(n));

    cout<<result_arr[num_sum(n)-key]<<endl;
}

int main()
{
    int arr[100],n = input_size(),result_arr[10000],key;
    input_array(arr,n);
    cout<<"enter key: ";
    cin>>key;
    result_print(arr,n,result_arr,key);

    return 0;
}