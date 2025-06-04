def find_duplicate_integer(integers):
    n = len(integers)
    expected_sum = n * (n - 1) // 2
    actual_sum = sum(integers)

    return actual_sum - expected_sum

print(find_duplicate_integer([1, 3, 4, 2, 2])) 