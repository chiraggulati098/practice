start = 2

def check_prime(s):
    global start
    for num in range(s,100000000000):
        prime_indicator = 1
        for x in range(2,num):
            if num%x == 0:
                prime_indicator = 0
        if prime_indicator == 1:
            print(num)
            start = num+1
            break

print("PRIME NUMBER GENERATOR")
enter = input("PRESS ENTER TO START")

if enter == '':
    check_prime(start)

continuing = True

while continuing == True:
    enter = input("Press Enter for Generating another Prime Number\nPress 1 to stop ")
    if enter == '':
        check_prime(start)
    elif enter == '1':
        continuing = False
    else:
        print("Please press either Enter or 1")