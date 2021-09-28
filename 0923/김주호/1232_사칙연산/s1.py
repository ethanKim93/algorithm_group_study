op = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y
}


def math(idx=1):
    val = tree[idx][0]

    if val in op:
        left = int(tree[idx][1])
        right = int(tree[idx][2])

        return op[val](math(left), math(right))

    else:
        return int(val)


for case in range(10):
    N = int(input())
    tree = [0] * (N + 1)

    for _ in range(N):
        st = input().split()

        tree[int(st[0])] = st[1:]

    print("#{} {}".format(case + 1, int(math())))
