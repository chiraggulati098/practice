# passed

def robinHood(arr, k):
    gold = 0
    ans = 0
    
    for val in arr:
        if val == 0:
            ans += 1 if gold > 0 else 0
            gold -= 1 if gold > 0 else 0
        elif val >= k:
            gold += val
    return ans

testCases = []
numTestCases = int(input())
for _ in range(numTestCases):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    testCases.append([k, arr])

for k, arr in testCases:
    print(robinHood(arr, k))