#include <iostream>
using namespace std;

int main()
{
    int a;
    cout<<"enter num between 1 to 10:";
    cin>>a;
    try {
        if(a<0)    {
            throw out_of_range("Number is less than 0!");
        }   
        else if(a>10)   {
            throw ('x');
        }   else    {
            cout<<"number = "<<a<<endl;
        }
    }   catch(const out_of_range& x)    {
        cout<<x.what()<<endl;
    }   catch(char x)   {
        cout<<"Number greater than 10!"<<endl;
    }
    return 0;
}