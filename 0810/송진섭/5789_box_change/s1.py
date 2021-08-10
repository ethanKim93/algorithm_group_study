import  sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())

    box = [0] * (N+1)
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            box[j] = i
    print('#{}'.format(tc), end=' ')
    for i in range(1, len(box)):
        print('{}'.format(box[i]), end=' ')