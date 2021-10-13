import sys
import copy
sys.stdin = open('sample_input.txt')

T = int(input())


def bomb(blocks, j, i):
    k = blocks[j][i]
    blocks[j][i] = 0
    for m in range(k):
        if j - m >= 0:
            blocks = bomb(blocks,j-m,i)
        if j + m < H:
            blocks = bomb(blocks, j + m, i)
        if i - m >= 0:
            blocks = bomb(blocks, j, i-m)
        if i + m < W:
            blocks = bomb(blocks, j, i+m)
    return blocks

def zero_sort(arr):
    for i in range(W):
        for j in range(H-1,0,-1):
            if arr[j][i] == 0:
                k = 1
                while (j-k)>=0:
                    if arr[j-k][i]:
                        arr[j][i],arr[j-k][i] = arr[j-k][i],arr[j][i]
                        break
                    k += 1
    return arr


def crush(n,blocks):
    global min_block
    cnt = 0
    if n ==0:  # n이 0이면
        for x in range(H):
            for y in range(W):
                if blocks[x][y]:
                    cnt += 1
        if min_block > cnt:
            min_block = cnt
        return

    for i in range(W):
        temp = copy.deepcopy(blocks)
        for j in range(H):
            if temp[j][i]:
                temp = bomb(temp,j,i)
                temp = zero_sort(temp)
                crush(n - 1, temp)
                break

    for x in range(H):
        for y in range(W):
            if temp[x][y]:
                cnt += 1
    if min_block > cnt:
        min_block = cnt
    return

for tc in range(1,T+1):
    N,W,H = map(int,input().split())
    blocks = [list(map(int,input().split())) for _ in range(H)]
    min_block = W*H
    crush(N,blocks)

    print('#{} {}'.format(tc,min_block))