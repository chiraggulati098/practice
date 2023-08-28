def check_prime(n):
    prime = []
    for num in range(2,n+1):
        prime_indicator = 1
        for x in range(2,num):
            if num/x == num//x:
                prime_indicator = 0
        if prime_indicator == 1:
            prime.append(num)
    return prime

n = int(input("Find Prime Factors of Number\nEnter Number: "))
prime_list = check_prime(n)
prime_factors = []

for prime_no in prime_list:
    if n%prime_no == 0:
        prime_factors.append(prime_no)

for factors in prime_factors:
    print(f"{factors}\t",end='')
print('')