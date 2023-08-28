#include <stdio.h>
#include <string.h>

typedef struct student	{
	int roll;
	float cgpa;
	char name[100];
}st;

int main()
{
	st s[100];
	s[0].roll = 2197;
	s[0].cgpa = 7.76;
	strcpy(s[0].name,"Chirag Gulati");
	printf("student info:\nname - %s\nroll no. - %d\ncgpa - %.2f\n",s[0].name,s[0].roll,s[0].cgpa);
	st s1 = {2198,7.45,"Arjun Singh"};
	st *ptr = &s1;
	printf("student info:\nname - %s\nroll no. - %d\ncgpa - %.2f\n",(*ptr).name,ptr->roll,s1.cgpa);
	return 0;
}
