# TLE

def func(n, k):
    # arr = [(x ** x) for x in range(n - k + 1, n + 1)]
    # print('---',sum(range(n - k + 1, n + 1)))
    # total = sum(arr)
    return "NO" if (sum(range(n - k + 1, n + 1))) % 2 != 0 else "YES"

testCases = []
numTestCases = int(input())
for _ in range(numTestCases):
    n, k = map(int, input().split())
    # arr = list(map(int, input().split()))
    testCases.append([n, k])

for n, k in testCases:
    print(func(n, k))