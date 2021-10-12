
import sys
sys.stdin = open('input.txt')


def backTrack(i,j,word):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    if len(word) == 7:
        ans.append(word)
        return

    for k in range(4):
         vx = i + dx[k]
         vy = j + dy[k]
         if vx >= 0 and vx < 4 and vy >= 0 and vy < 4:
             backTrack(vx, vy, word + matrix[vx][vy])

    return

T = int(input())
for tc in range(T):
    matrix = [list(input().split()) for i in range(4)]
    ans = []
    for i in range(4):
        for j in range(4):
            backTrack(i,j,'')

    ans = set(ans)
    print('#{} {}'.format(tc+1, len(ans)))