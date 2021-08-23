import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    room = []
    for i in range(N):
        now, tar = map(int,input().split())
        trans_now=(now-1)//2
        trans_tar=(tar-1)//2
        room.append([trans_now,trans_tar])
    space=[0]*200
    for child in room:
        if child[0] <= child[1]:
            for i in range(child[0],child[1]+1):
                space[i] += 1
        else:
            for i in range(child[1],child[0]+1):
                space[i] += 1
    print('#{} {}'.format(tc,max(space)))