def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)
    
print("----- FACTORIAL FINDER -----")
    
while True:
    try:
        num = int(input("Enter Number: "))
    except:
        print("Please enter an Integer")
    else:
        if num<0:
            print("Please enter a positive Number")
            continue
        break

print(f'Factorial of {num} = {factorial(num)}')