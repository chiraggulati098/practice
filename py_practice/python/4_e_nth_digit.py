from decimal import *
from math import e

def get_e_till_n(n):
    getcontext().prec = n+1
    e_n = e
    print(Decimal(e_n)/Decimal(1))

n = int(input("Enter n (from 0 to 51): "))
get_e_till_n(n)
