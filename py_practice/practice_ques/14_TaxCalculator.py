def calculate_tax(amount, percent):
    return amount*percent/100

while True:
    try:
        income = float(input("Enter your Annual Income (in INR): "))
    except:
        print("Please enter a numeric value")
    else:
        if income < 0:
            print("Please enter a positive value")
            continue
        break

if income > 0 and income <= 250000:
    print("Tax: INR 0")
elif income <= 500000:
    print(f'Tax: INR {calculate_tax(income,5)}')
elif income <= 750000:
    print(f'Tax: INR {calculate_tax(income,10)+12500}')
elif income <= 1000000:
    print(f'Tax: INR {calculate_tax(income,15)+37500}')
elif income <= 1250000:
    print(f'Tax: INR {calculate_tax(income,20)+75000}')
elif income <= 1500000:
    print(f'Tax: INR {calculate_tax(income,25)+125000}')
elif income > 1500000:
    print(f'Tax: INR {calculate_tax(income,30)+187500}')
else:
    print("Please enter a valid Income")