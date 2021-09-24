def leaf(num=0):
    if num >= N:
        return

    global value
    leaf(num*2 + 1)
    tree[num] = value
    value += 1
    leaf(num*2 + 2)

    return


for case in range(int(input())):
    N = int(input())
    tree = [0] * N
    value = 1

    leaf()

    print("#{} {} {}".format(case+1, tree[0], tree[N//2-1]))
