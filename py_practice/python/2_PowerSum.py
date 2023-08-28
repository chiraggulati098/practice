x = int(input("Enter x: ")) 
y = int(input("Enter y: ")) 
sum = 0
i = 1

while i <= y:   
    sum += x**i
    i += 1

print(sum) 