cost = int(input("Enter the cost: "))
money = int(input("Enter money paid: "))
change = money-cost

print(f'Money to be paid back: {change}\n')
if change//2000>0:
    print(f'Number of Rs. 2000 Notes: {change//2000}')
    change = change - (change//2000 * 2000)
if change//500>0:
    print(f'Number of Rs. 500 Notes: {change//500}')
    change = change - (change//500 * 500)
if change//200>0:
    print(f'Number of Rs. 200 Notes: {change//200}')
    change = change - (change//200 * 200)
if change//100>0:
    print(f'Number of Rs. 100 Notes: {change//100}')
    change = change - (change//100 * 100)
if change//50>0:
    print(f'Number of Rs. 50 Notes: {change//50}')
    change = change - (change//50 * 50)
if change//20>0:
    print(f'Number of Rs. 20 Notes: {change//20}')
    change = change - (change//20 * 20)
if change//10>0:
    print(f'Number of Rs. 10 Notes: {change//10}')
    change = change - (change//10 * 10)
if change//5>0:
    print(f'Number of Rs. 5 Coins: {change//5}')
    change = change - (change//5 * 5)
if change//2>0:
    print(f'Number of Rs. 2 Coins: {change//2}')
    change = change - (change//2 * 2)
if change//1>0:
    print(f'Number of Rs. 1 Coins: {change}')