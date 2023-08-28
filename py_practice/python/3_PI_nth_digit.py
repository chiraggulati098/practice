from decimal import *

def get_pi_till_n(n):
    getcontext().prec = n+1
    pi = Decimal (22)/ Decimal(7)
    print(pi)

n = int(input("Enter n: "))
get_pi_till_n(n)