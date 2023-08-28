#include<stdio.h>
#include<math.h>

int power(int x, int y)
{
    int result = 1;
    for (int i = 0;i<y;i++) {
        result *= x;
    }
    return result;
}

int num_of_digits(int num)
{
    int count = 0;
    while (num != 0)    {
        count++;
        num /= 10;
    }
    return count;
}

int armstrong_num(int num)
{
    int sum = 0, temp_num = num, digits;
    digits = num_of_digits(num);

    while (temp_num != 0)   {
        sum += power(temp_num%10,digits);
        temp_num /= 10;
    }

    if (sum == num)
        return 1;
    else
        return 0;
}

int main()
{
    int range1, range2;
    printf("enter start of range:");
    scanf("%d",&range1);
    printf("enter end of range:");
    scanf("%d",&range2);
    printf("\n");

    for (int i = range1; i<=range2; i++)    {
        if (armstrong_num(i) == 1)  {
            printf("%d\n",i);
        }
    }
    printf("\n");
    return 0;
}
