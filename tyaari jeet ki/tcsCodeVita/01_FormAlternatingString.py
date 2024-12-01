binString = input("")
n = len(binString)
arr = list(map(int, input("").split()))

toRemove = 0

prevArrMaxVal = arr[0]
for r in range(1, n):
    if binString[r] != binString[r - 1]:
        prevArrMaxVal = arr[r]
    else:
        toRemove += min(prevArrMaxVal, arr[r])
        prevArrMaxVal = max(prevArrMaxVal, arr[r])

print(toRemove, end="")