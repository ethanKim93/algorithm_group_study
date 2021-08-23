import sys
sys.stdin = open("input.txt")

T = int(input())
for test in range(1,T+1):
    N = int(input())
    list_1 = list(map(int, input().split(" ")))
    max_i = list_1[-1]
    result = 0
    for i in range(N-2, -1, -1):
        if list_1[i] <= max_i:
            result += max_i - list_1[i]
        elif list_1[i] > max_i:
            max_i = list_1[i]
    print('#{0} {1}'.format(test,result))