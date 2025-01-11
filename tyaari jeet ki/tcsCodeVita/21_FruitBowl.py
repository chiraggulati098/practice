# n = int(input(""))

# dots = []
# for _ in range(n):
#     dots.append(list(map(int, input('').split())))

n = 8
dots = [[3, 4], [5, 5], [2, 2], [2, 5], [6, 4], [4, 1], [1, 3], [4, 3]]

dots.sort()
basket_points = []
res = 0

def cross_product(a, b, p):
    return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])

for coord in dots:
    while len(basket_points) >= 2 and cross_product(basket_points[-2], basket_points[-1], coord) <= 0:
        basket_points.pop()
    basket_points.append(coord)

m = len(basket_points)
for i in range(m - 1):
    a, b = basket_points[i], basket_points[i + 1]
    res += (((b[0] - a[0]) ** 2) + ((b[1] - a[1]) ** 2)) ** 0.5

print(round(res), end = '')