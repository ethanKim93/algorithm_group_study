import sys
sys.stdin = open('s_input.txt')

for tc in range(1, int(input())+1):
    N = int(input())
    bus_cnt = [0] * 5001

    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            bus_cnt[i] += 1
    print('#{}'.format(tc), end= " ")

    for j in range(int(input())):
        idx = int(input())
        print('{}'.format(bus_cnt[idx]), end=" ")
    print()
