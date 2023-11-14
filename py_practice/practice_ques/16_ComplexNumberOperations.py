class Complex:

    def __init__(self,real,img):
        self.real = real
        self.img = img

    def __str__(self):
        if self.img == 0:
            return f'{self.real}'
        elif self.real == 0:
            return f'{self.img}i'
        else:
            return f'{self.real} + {self.img}i'
    
    def add(self,other):
        real_sum = self.real + other.real
        img_sum = self.img + other.img
        return Complex(real_sum,img_sum)
    
    def sub(self,other):
        real_sum = self.real - other.real
        img_sum = self.img - other.img
        return Complex(real_sum,img_sum)
    
def try_except_else_block(string):
    while True:
        try:
            n = int(input(string))
        except:
            print("Please enter an Integer")
        else:
            return n
            break

def choice_func():
    print("\nEnter 1 for COMPLEX ADDITION")
    print("Enter 2 for COMPLEX SUBTRACTION")
    while True:
        try:
            choice = int(input("Enter your Choice: "))
        except:
            print("Please enter an Integer")
        else:
            if choice not in [1,2]:
                print("Please enter 1 or 2\n")
                continue
            return choice

print("--- COMPLEX NUMBER CALCULATOR ---")

while True:

    choice = choice_func()  

    r1 = try_except_else_block('Enter the Real value for 1st Complex Number: ')
    i1 = try_except_else_block('Enter the Imaginary value for 1st Complex Number: ')
    r2 = try_except_else_block('Enter the Real value for 2nd Complex Number: ')
    i2 = try_except_else_block('Enter the Imaginary value for 2nd Complex Number: ')

    c1 = Complex(r1,i1)
    c2 = Complex(r2,i2)

    if choice == 1:
        c3 = c1.add(c2)
        print(f'Sum = {c3}')
        print()
    else:
        c3 = c1.sub(c2)
        print(f'Sub = {c3}')
        print()

    print("Do you want to EXIT or GO AGAIN?")
    stopchoice = input("Enter Y to GO AGAIN or N to EXIT: ")

    if stopchoice.upper() == 'Y':
        continue
    else:
        break