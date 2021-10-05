import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def babygin(i, mat):
    global card, visited, last
    if sum(visited) == 3:
        mat = list(map(int, mat))
        mat.sort()
        if (mat[0] == mat[1] and mat[1] == mat[2]) or (mat[0]+1 == mat[1] and mat[1]+1 == mat[2]):
            if last > i:
                last = i
        return 

    for j in range(i, 6):
        if not visited[j]:
            visited[j] = 1
            mat.append(card[j])
            babygin(j, mat)
            mat.pop()
            visited[j] = 0
    
    return last


for tc in range(1, T+1):
    cards = list(input().split())
    card1 = []
    card2 = []
    visited = [0] * 6

    for i in range(12):
        if not i%2:
            card1 += cards[i]
        else:
            card2 += cards[i]
    last = 100
    card = card1
    p1 = babygin(0, list())
    last = 100
    card = card2
    p2 = babygin(0, list())

    if p1 == 100 and p2 == 100:
        res = 0
    elif p1 <= p2:
        res = 1
    else:
        res = 2
    print('#{} {}'.format(tc, res))
