def dec_to_bin(n):
    return bin(n).replace('0b','')

def bin_to_dec(n):
    return int(n,2)

print("PRESS 1 TO CONVERT DECIMAL INTO BINARY")
print("PRESS 2 TO CONVERT BINARY INTO DECIMAL")

choice = 0
while (choice != 1 and choice != 2):
    choice = input('Enter Choice: ')
    if choice == '1' or choice == '2':
        choice = int(choice)
        break
    else:
        print("Please enter either 1 or 2!")

if choice == 1:
    print(dec_to_bin(int(input("Enter Decimal Number: "))))
elif choice == 2:
    print(bin_to_dec(input("Enter Binary Number: ")))