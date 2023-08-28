#include <iostream>
using namespace std;

int main()
{
    int a,b;
    cout<<"enter 2 num:"<<endl;
    cin>>a>>b;
    try {
        if(b!=0)    {
            float result = a/float(b);
            cout<<"result = "<<result<<endl;
        }   else    {
            throw(b);
        }
    }   catch(int x)    {
        cout<<"Exception Caught: Divide by Zero"<<endl;
    }
    return 0;
}