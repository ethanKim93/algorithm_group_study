import sys
sys.studin = open('sample_input.txt')

def sub_tree(n):
    global cnt
    if n == 0:
        return
    cnt += 1
    sub_tree(left[n])
    sub_tree(right[n])


T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    node = list(map(int, input().split()))

    left = [0] * (E + 2)
    right = [0] * (E + 2)

    for i in range(0, len(node), 2):
        parent = node[i]
        child = node[i+1]
        if left[parent]:
            right[parent] = child
        else:
            left[parent] = child

    cnt = 0
    sub_tree(N)
    print('#{} {}'.format(tc, cnt))