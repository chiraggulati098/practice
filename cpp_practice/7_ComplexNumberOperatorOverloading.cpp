#include <iostream>
using namespace std;

class Complex
{
    public:
        int real, img;

        Complex()   {
            real = 0;
            img = 0;
        }

        Complex(int r,int i)    {
            real = r;
            img = i;
        }

        void display()  {
            cout<<real<<" + "<<img<<"i"<<endl;
        }

        Complex operator + (Complex& a)    {
            Complex c;
            c.real = real + a.real;
            c.img = img + a.img;
            return c;
        }
};

int main()
{
    Complex a(2,3), b(2,3), c;
    c = a+b;
    c.display();
    return 0;
}