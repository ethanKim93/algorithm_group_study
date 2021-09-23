import sys
sys.stdin = open('input.txt')


def in_order(n):
    if n:
        in_order(left[n])
        result.append(alpha[n])
        in_order(right[n])


for tc in range(1, 11):
    V = int(input())
    E = V - 1
    alpha = [0] * (V+1)
    left = [0] * (V+1)
    right = [0] * (V+1)
    for _ in range(V):
        data = input().split()
        n = len(data)
        for i in range(n):
            if data[i].isdecimal():
                data[i] = int(data[i])

        alpha[data[0]] = data[1]
        if n == 4:
            left[data[0]] = data[2]
            right[data[0]] = data[3]
        elif n == 3:
            left[data[0]] = data[2]

    result = []
    in_order(1)
    print('#{} {}'.format(tc, ''.join(result)))
