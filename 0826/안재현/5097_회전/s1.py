import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    seq = list(map(int, input().split()))

    for i in range(M):
        tmp = seq.pop(0)
        seq.append(tmp)

    print('#{} {}'.format(tc + 1, seq[0])