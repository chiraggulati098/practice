#include<stdio.h>

int Count(int num)
{
    int count = 0;
    while (num>0)   {
        count++;
        num /= 10;
    }
    return count;
}

int main()
{
    int count, num, temp_num, times10 = 1;
    printf("enter the number: ");
    scanf("%d",&num);
    temp_num = num;

    count = Count(num);
    for (int i = 0;i<count;i++) {
        if (temp_num % 10 == 0) {
            num += (times10*1);
        }
            temp_num /= 10;
            times10 *= 10;
    }

    printf("\nnew number = %d\n",num);

    return 0;
}
