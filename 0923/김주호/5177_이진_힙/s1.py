def leaf(n, index):
    if tree[index // 2] < n:
        tree[index] = n
    else:
        tree[index // 2], tree[index] = n, tree[index // 2]
        leaf(n, index // 2)
    return


for case in range(int(input())):
    N = int(input())
    tree = [0] * (N + 1)

    nums = list(map(int, input().split()))
    idx = 0
    for num in nums:
        idx += 1
        leaf(num, idx)

    total = 0
    while N:
        N //= 2
        total += tree[N]

    print("#{} {}".format(case + 1, total))
