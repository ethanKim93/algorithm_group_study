import sys
sys.stdin = open('input.txt')

def find_big(li,n,small):
    max_idx = n-1
    for k in range(n-1,small,-1):
        if board[max_idx] < board[k]:
            max_idx = k
    return max_idx

def find_small(li,n,big):
    min_idx = 0
    for j in range(big):
        if board[min_idx] > board[j]:
            min_idx = j
    return min_idx


T = int(input())
for tc in range(1,T+1):
    N = list(input().split())
    trade = int(N[-1])
    board = list(N[0])
    n = len(board)
    # 뒤에서 찾을땐 가장 큰수, 앞에서 찾을땐 가장 작은수 -> 그렇게 교환
    b, s = n,0
    while trade:
        if s <= n-1:
            b = find_big(board,n,s-1)
            if board.count(board[b]) == 1:
                if s != b :
                    board[b], board[s] = board[s], board[b]
                    trade -= 1
                    s += 1
                else:
                    s += 1
            else:
                m = find_small(board, n, b)
                board[m], board[b] = board[b], board[m]
                trade -= 1
        else:
            board[n-1], board[n-2] = board[n-2], board[n-1]
            trade -= 1

    print('#{} {}'.format(tc, ''.join(board)))



