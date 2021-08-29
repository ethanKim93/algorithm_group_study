import sys
sys.stdin = open('input.txt')

def in_order(n):
    if n:
        in_order(left_info[n])
        print(node_word[n], end='')
        in_order(right_info[n])


for tc in range(1, 11):
    N = int(input())
    left_info = [0]*(N+1)
    right_info = [0]*(N+1)
    node_word = [0]*(N+1)

    for _ in range(N):
        info = input().split()
        if len(info) == 2:
            node, word = info
            node_word[int(node)] = word
        if len(info) == 3:
            node, word, left = info
            left_info[int(node)] = int(left)
            node_word[int(node)] = word
        if len(info) == 4:
            node, word, left, right = info
            left_info[int(node)] = int(left)
            right_info[int(node)] = int(right)
            node_word[int(node)] = word


    print('#{} '.format(tc), end='')
    in_order(1)
    print()

