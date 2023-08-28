#include <iostream>
using namespace std;

void input(int& x)  {
    try {
        cout<<"enter num greater than 0: ";
        cin>>x;
        if (x<1)    {
            throw(x);
        }
    }   catch(int x)    {
        cout<<"Inside Function"<<endl;
        throw;
    }
}

int main()
{
    int a;
    try {
        input(a);
        cout<<"num = "<<a<<endl;
    }   catch(int)   {
        cout<<"Inside Main()"<<endl;
    }
    return 0;
}