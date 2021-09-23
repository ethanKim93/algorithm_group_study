import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def op():
    pass

for tc in range(1, 11):
    li = ['+', '-', '*', '/']
    N = int(input())
    cal = [0] + [[0] for _ in range(N)]
    ans = 0
    for i in range(1, N+1):
        cal[i] = input().split()
    for j in range(1, N+1):
        if cal[-j][1] in li:
            if cal[-j][1] == '+':
                ans = (int(cal[int(cal[-j][2])][1]) + int(cal[int(cal[-j][3])][1]))
                cal[-j][1] = ans
            elif cal[-j][1] == '-':
                ans = (int(cal[int(cal[-j][2])][1]) - int(cal[int(cal[-j][3])][1]))
                cal[-j][1] = ans
            elif cal[-j][1] == '*':
                ans = (int(cal[int(cal[-j][2])][1]) * int(cal[int(cal[-j][3])][1]))
                cal[-j][1] = ans
            else:
                ans = (int(cal[int(cal[-j][2])][1]) / int(cal[int(cal[-j][3])][1]))
                cal[-j][1] = ans

    print('#{} {}'.format(tc, int(ans)))