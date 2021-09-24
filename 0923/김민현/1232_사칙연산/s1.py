import sys
sys.stdin = open("sample_input.txt")


def cal(n):
    if left[n]:
        if tree[n] == '*':
            return cal(left[n]) * cal(right[n])
        elif tree[n] == '/':
            return cal(left[n]) / cal(right[n])
        elif tree[n] == '+':
            return cal(left[n]) + cal(right[n])
        elif tree[n] == '-':
            return cal(left[n]) - cal(right[n])
    else:
        return tree[n]


for tc in range(1,11):
    N = int(input())
    tree = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for i in range(N):
        data = list(input().split())
        try:
            tree[int(data[0])] = int(data[1])
        except:
            tree[int(data[0])] = data[1]
        if len(data) >2:
            left[int(data[0])] = int(data[2])
            right[int(data[0])] = int(data[3])

    print('#{} {}'.format(tc, int(cal(1))))



