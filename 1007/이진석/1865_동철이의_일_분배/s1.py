import sys
sys.stdin = open('input.txt')

def work(person, percent):
    global max_percent, N

    if person == N:
        if percent > max_percent:
            max_percent = percent
        return

    if percent <= max_percent:
        return


    for i in range(N):
        if not worked[i]:
            new_p = percent*P[person][i]
            worked[i] = 1
            work(person+1, new_p)
            worked[i] = 0

for tc in range(1, int(input())+1):
    N = int(input())
    # P = [list(map(int, input().split())) for _ in range(N)]
    P = [list(map(lambda x:x*0.01,map(int, input().split()))) for _ in range(N)]

    worked = [0] * N
    max_percent = -1
    work(0,1)
    print('#{} {:6f}'.format(tc, max_percent*100))
    del worked
