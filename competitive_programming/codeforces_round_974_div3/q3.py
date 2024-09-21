# failed 2nd test case

def func(arr, n):
    if n <= 2:
        return -1
    
    arr.sort()

    curAvg = (sum(arr) / n) 
    ans = int (((2 * arr[n // 2]) - curAvg) * n) + 1
    
    return ans if ans >= 0 else 0

testCases = []
numTestCases = int(input())
for _ in range(numTestCases):
    n = int(input())
    # n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    testCases.append([arr, n])

for arr, n in testCases:
    print(func(arr, n))