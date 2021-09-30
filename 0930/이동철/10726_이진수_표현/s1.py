import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, M = input().split()
    if M == '0':
        binary = ['0' for i in range(int(N))]
    else:
        binary = list(format(int(M), 'b'))

    if binary[len(binary) - int(N):len(binary)] == ['1' for i in range(int(N))]:
        print('#{} ON'.format(tc))
    else:
        print('#{} OFF'.format(tc))
    # print(binary)
    # print(binary[len(binary) - int(N):len(binary)])
    # print()