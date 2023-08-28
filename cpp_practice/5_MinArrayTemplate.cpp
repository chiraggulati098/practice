#include <iostream>
using namespace std;

template <typename T>
T min(T e[],int n)  {
    T small = e[0];
    for (int i = 1;i<n;i++) {
        if (e[i]<small) {
            small = e[i];
        }
    }
    return small;
}

int main() 
{
    int a[5] = {3,4,34,5,2};
    float b[5] = {2.3,23,234,24,1.3};

    cout<<min(a,5)<<endl;
    cout<<min(b,5)<<endl;

    return 0;
}