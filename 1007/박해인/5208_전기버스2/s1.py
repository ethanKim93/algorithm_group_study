import sys
sys.stdin = open('sample_input.txt')
#
#
# def move(num):
#
#     if change > N:
#         return
#
#     elif now == N:
#         result = min(N, change)
#         return
#     if battery:
#         move(now+1, battery-1, change)
#     move(now+1, Mi[now]-1, change+1)

T = int(input())
for test_case in range(1, T+1):
    data = list(map(int, input().split()))
    N = data[0]
    Mi = data[1:] + [0]

    move()
    print('#{} {}'.format(test_case, result))

