import sys
sys.stdin = open("input.txt")

for case in range(10):
    li = [[] for _ in range(99)]
    N, Ways = map(int, input().split())

    Nodes = list(map(int, input().split()))

    for i in range(0, Ways * 2, 2):
        li[Nodes[i]].append(Nodes[i + 1])

    stack = [0]
    val = 0

    while len(stack) > 0:
        try:
            place = stack[-1]
            if place == 99:
                val = 1
                break
            else:
                stack.append(li[place][0])
                del[li[place][0]]
        except:
            stack.pop()

    print("#{} {}".format(case + 1, val))