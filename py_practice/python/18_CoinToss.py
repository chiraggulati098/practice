import random

toss = {'1':'Heads','2':'Tails'}
head = 0
tail = 0

def flip():
    global head
    global tail
    flip = random.randint(1,2)
    print(toss[str(flip)])
    if flip == 1:
        head+=1
    else:
        tail+=1
    print(f'Heads: {head}\nTails: {tail}')

print("----- WELCOME TO COIN TOSS SIMULATOR -----")

while True:
    choice = input("\nPress enter to Toss or N to Exit: ")
    if choice == '':
        flip()
    else:
        break