import sys
sys.stdin = open('sample_input.txt')
from collections import deque

def bfs(i, j):
    global words
    q = deque()
    q.append((i, j, 7, ''))
    while q:
        vr, vc, cnt, word = q.popleft()
        if not cnt:
            words.add(word)

        for d in range(4):
            wr = vr + dr[d]
            wc = vc + dc[d]
            if wr in range(4) and wc in range(4) and cnt:
                q.append((wr, wc, cnt-1, word+mat[wr][wc]))
                

T = int(input())

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, T+1):
    mat = [list( input().split()) for _ in range(4)]
    words = set()
    for i in range(4):
        for j in range(4):
            bfs(i,j)
    print('#{} {}'.format(tc, len(words)))