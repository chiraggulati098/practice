#include <iostream>
using namespace std;

class Vector
{
    private:
        int x,y;
    public:
        Vector(int a,int b) {
            x = a;
            y = b;
        }
        
        Vector operator + (Vector &o2)  {
            return Vector(x+o2.x,y+o2.y);
        }

        void print_vector() {
            cout<<x<<"x + "<<y<<"y"<<endl;
        }
};

int main()  {
    Vector v1(1,2);
    Vector v2(3,4);
    Vector v3 = v1+v2;

    v3.print_vector();

    return 0;
}