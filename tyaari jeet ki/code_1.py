'''
Given an Array A with n elements. Return the maximum sum you can achieve by choosing K elements, but none of the elements should be adjacent to each other i.e. if element A[i] is chosen, then next element must not be A[i+1] where 0 <= i < n. 

Example 
A = [5, 3, 10, 11, 8, -1, -3, 4] 
K = 3

Solution:
You can choose 5, 10, 8 to give you sum = 23 which is the maximum
'''


# This is not the best approach (but something I figured out)
# We should try the take / not take approach here


def func(A, K):
    n = len(A)

    if n < 2 * K:
        return -1

    A_sorted = sorted(A, reverse=True)
    res = float("-inf")

    for i in range(n):
        if K > n - i:
            return res
        picked = set()
        local = 0
        j = i

        for _ in range(K):
            while j < n:
                idx = A.index(A_sorted[j])
                if idx + 1 not in picked and idx - 1 not in picked:
                    local += A_sorted[j]
                    picked.add(idx)
                    j += 1
                    break
                j += 1
        
        res = max(res, local)

A = [5, 3, 10, 11]
#A = [5,5,5,5,5,5,5,5]
#A = [-1,-1,-1,-1]
K = 2

print(func(A, K))