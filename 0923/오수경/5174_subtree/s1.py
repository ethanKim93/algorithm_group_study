import sys
sys.stdin = open('sample_input.txt')

def sub_node(n):
    global cnt
    if left[n] == 0 and right[n] == 0:
        return cnt
    else:
        if left[n] != 0:
            cnt += 1
            sub_node(left[n])

        if right[n] != 0:
            cnt += 1
            sub_node(right[n])
        return cnt

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    num = list(map(int, input().split()))

    left = [0]*(E+2)
    right = [0]*(E+2)
    for i in range(E):
        if left[num[2*i]] == 0:
            left[num[2*i]] = num[2*i+1]
        else:
            right[num[2*i]] = num[2*i+1]
    cnt = 0
    print('#{} {}'.format(tc, sub_node(N)+1))