def down(num):
    global count
    for leaf in tree[num]:
        down(leaf)
        count += 1
    return count


for case in range(int(input())):
    E, N = map(int, input().split())
    tree = [[] for _ in range(E+1)]

    st = list(map(int, input().split()))

    for i in range(0, len(st), 2):
        tree[st[i]-1].append(st[i+1]-1)

    count = 1
    print("#{} {}".format(case + 1, down(N-1)))
