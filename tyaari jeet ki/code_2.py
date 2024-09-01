'''
asteroids + right and - left representing direction
asteroids going in opposite direction destroy each other
smaller one gets destroyed if their directions are not equal
both get destroyed if their values are equal but opposite direction

input = [-5, 5, 15, -15, 5, 10]
output = [-5, 5, 5, 10]

input = [5, 10, -5]
output = [5, 10]
'''

def solve(arr):
    left_ones = []
    stack = []
    
    for asteroid in arr:
        # going left
        if asteroid < 0:
            while stack:
                prev = stack.pop()
                # same - so destroyed
                if prev == abs(asteroid):
                    break
                # if prev was bigger
                elif prev > abs(asteroid):
                    stack.append(prev)
                    break
                # if prev was smaller - previous breaks
                else:
                    continue
            else:
                left_ones.append(asteroid)  # going left endlessly without collision

        # going right 
        else:
            stack.append(asteroid)
    
    return left_ones + stack


arr = [5, 10, -5]
print(solve(arr))