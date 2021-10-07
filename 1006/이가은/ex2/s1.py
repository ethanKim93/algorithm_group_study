A = [i for i in range(1,11)]

def pwset(arr):
    n = len(arr)
    for i in range(2**n):
        subsum = 0
        subset = []
        for j in range(n):
            if i & 1<<j:
                subsum += arr[j]
                subset.append(arr[j])
        if subsum == 10:
            print(subset)

print(pwset(A))

#  Output
# [1, 2, 3, 4]
# [2, 3, 5]
# [1, 4, 5]
# [1, 3, 6]
# [4, 6]
# [1, 2, 7]
# [3, 7]
# [2, 8]
# [1, 9]
# [10]
