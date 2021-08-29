def in_order(i=0):
    try:
        in_order(int(tree[i][2]) - 1)
    except:
        pass
    st.append(tree[i][1])
    try:
        in_order(int(tree[i][3]) - 1)
    except:
        pass
    return st


for case in range(10):
    N = int(input())

    tree = [input().split() for _ in range(N)]

    st = []

    print("#{} {}".format(case + 1, ''.join(in_order())))
