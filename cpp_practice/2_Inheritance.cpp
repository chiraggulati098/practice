#include <iostream>
using namespace std;

class Grandparent
{
    public:
        Grandparent()   {
            cout<<"This is the Grandparent Class\n";
        }    
};

class Parent : public Grandparent
{   
    public:
        Parent()    {
            cout<<"This is Parent Class\n";
        }
};

class Child : public Parent
{
    public:
        Child() {
            cout<<"This is Child Class\n";
        }
};

int main()
{
    Child c;
    return 0;
}