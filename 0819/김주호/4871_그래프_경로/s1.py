import sys
sys.stdin = open("sample_input.txt")

for case in range(int(input())):
    V, E = map(int, input().split())
    stack = []
    place = [0] * V
    li = [[0] * V for _ in range(V)]

    for _ in range(E):
        LS, LE = map(int, input().split())
        li[LS - 1][LE - 1] = 1

    S, G = map(int, input().split())
    place[S - 1] = 1
    stack.append(S - 1)

    ans = 0
    while len(stack):
        for EP in range(V):
            if li[stack[-1]][EP] and not place[EP]:
                place[EP] = 1
                stack.append(EP)
                if EP == G - 1:
                    ans = 1
                break
        else:
            stack.pop()

        if ans:
            break

    print("#{} {}".format(case + 1, ans))
