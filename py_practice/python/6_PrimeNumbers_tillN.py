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

n = int(input("Find Prime Numbers till N\nEnter N: "))
prime_list = check_prime(n)
for number in prime_list:
    print(f"{number}\t",end='')
print('')