import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    a, b = input().split()
    i = 0
    mini = 0

    while i < len(a):
        if a[i] == b[0]:
            if a[i:i+len(b)] == b:
                mini += 1
                i += len(b)
            else:
                mini += 1
                i += 1
        else:
            mini += 1
            i += 1
    print('#{} {}'.format(tc, mini))

