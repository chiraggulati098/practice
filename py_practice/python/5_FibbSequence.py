t1 = 0
t2 = 1
n = int(input("Enter n: "))
if n <= 0:
    print("enter a positive number")
elif n == 1:
    print("0")
elif n == 2:
    print("0\t1")
else:
    print("0\t1",end='')
    for _ in range(3,n+1):
        t3 = t1+t2
        print(f'\t{t3}',end='')
        t1 = t2
        t2 = t3
print('\tEND')