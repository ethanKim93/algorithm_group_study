import sys

sys.stdin = open('input.txt')
T = 10
def in_order(n):
    global visit
    if n:
        in_order(left[n])
        visit.append(n)
        in_order(right[n])

for tc in range(1, T + 1):
    V = int(input())
    left = [0] * (V + 1)
    right = [0] * (V + 1)
    tree = [0] * (V + 1)

    for i in range(V):
        V_list = list(map(str, input().split()))
        idx = int(V_list.pop(0))

        if V_list[0] in '+-*/':

            tmp = V_list.pop(0)
            tree[idx] = tmp
            if not left[idx]:
                tmp = V_list.pop(0)
                left[idx] = tmp
            if left[idx]:
                tmp = V_list.pop(0)
                right[idx] = tmp

        elif V_list[0].isnumeric():
            tmp = V_list.pop(0)
            tree[idx] = tmp

    left = list(map(int, left))
    right = list(map(int, right))
    visit = [0]
    in_order(1)

    result=[]
    for i in range(1,len(visit)):
        result.append(tree[visit[i]])

    print(result)
    #식으로 변환했으나.. ['88', '-', '65', '-', '10']을 어떻게 계산시켜야할지 모르겠다..;;