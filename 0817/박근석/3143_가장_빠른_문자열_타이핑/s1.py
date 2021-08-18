import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    t, p = list(map(str, input().split()))

    count = 0
    i = 0
    while i < len(t):
        if t[i:i+len(p)] == p:
            count += 1
            i = i + len(p)
        else:
            count += 1
            i += 1
    print('#{} {}'.format(tc, count))
