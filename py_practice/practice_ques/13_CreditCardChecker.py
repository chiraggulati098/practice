def checker(num, clen):
    sum = 0
    for x in range(clen):
        double = int(num[x])*2
        if x%2 == 0:
            if double > 9:
                sum+=add_double_digits(double)
            else:
                sum+=double
        else:
            sum+=int(num[x])
    return sum

def add_double_digits(n):
    total = 0
    while n>0:
        total += n%10
        n//=10
    return total

ccnum = input("Enter the CC Number: ").replace(' ','')
cclen = len(ccnum)

print(checker(ccnum,cclen))

if (checker(ccnum,cclen))%10 == 0:
    print("CREDIT CARD VALDATED")
else:
    print("WRONG CC NUMBER")