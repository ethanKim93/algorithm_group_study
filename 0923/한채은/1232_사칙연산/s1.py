import sys
sys.stdin = open('input.txt')


def result(operator):
    if operator == '+':
        ans = tree[int(inform[i][2])] + tree[int(inform[i][3])]
    elif operator == '-':
        ans = tree[int(inform[i][2])] - tree[int(inform[i][3])]
    elif operator == '*':
        ans = tree[int(inform[i][2])] * tree[int(inform[i][3])]
    else:
        ans = tree[int(inform[i][2])] // tree[int(inform[i][3])]
    return ans


# 연산자를 판별할 리스트
cal = ['+', '-', '*', '/']

for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)
    inform = [0] + [list(input().split()) for _ in range(N)]

    # 거꾸로 돌면서 연산자가 나오면 함수로 계산
    for i in range(N, 0, -1):
        if inform[i][1] in cal:
            tree[i] = result(inform[i][1])
        # 연산자가 아니면 트리에 값 집어 넣기
        else:
            tree[i] = int(inform[i][1])

    print('#{} {}'.format(tc, tree[1]))
