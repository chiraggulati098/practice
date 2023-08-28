#include<stdio.h>
#include<string.h>

int main()
{
    int pos = 0;
    char input_string[1000], output_string[30] = "";
    printf("enter string: ");
    fgets(input_string,1000,stdin);

    for (int i=0;input_string[i]!='\0';i++) {
        for (int j=0;j>=0;j++)    {
            if (output_string[j] == input_string[i])
                break;
            if (output_string[j] == '\0')   {
                output_string[pos] = input_string[i];
                output_string[pos+1] = '\0';
                pos++;
                break;
            }
        }
    }
    printf("new string: %s\n",output_string);

    return 0;
}
