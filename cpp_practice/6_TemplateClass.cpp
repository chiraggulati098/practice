#include <iostream>
using namespace std;

template<class T1,class T2>
class Sample
{
    T1 a;
    T2 b;
    public:
        Sample(T1 x,T2 y)   {
            a = x;
            b = y;
            cout<<"a = "<<a<<"\tb = "<<b<<endl;
        }
};

int main() 
{
    Sample a(1,2);
    Sample b('a',4.5);
    Sample c(2.2323,"string");
    return 0;
}