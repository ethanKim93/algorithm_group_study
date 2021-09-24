import sys
sys.stdin = open('input.txt')

def a_b(x):
    global n
    for i in range(N):
        if calculate[i][0] == calculate[n][x]:
            return calculate[i][1]

for tc in range(1, 11):
    N = int(input())
    calculate = []
    for n in range(N):
        node = list(input().split())
        calculate.append(node)

    for n in range(len(calculate)-1, -1, -1):
        if not calculate[n][1].isdigit():
            if calculate[n][1] == '+':
                calculate[n][1] = int(a_b(2)) + int(a_b(3))
            elif calculate[n][1] == '-':
                calculate[n][1] = int(a_b(2)) - int(a_b(3))
            elif calculate[n][1] == '*':
                calculate[n][1] = int(a_b(2)) * int(a_b(3))
            elif calculate[n][1] == '/':
                calculate[n][1] = int(a_b(2)) / int(a_b(3))
    print('#{} {}'.format(tc, int(calculate[0][1])))


