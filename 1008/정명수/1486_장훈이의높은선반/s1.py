import sys
sys.stdin = open('input.txt')

def looking(n,height):
    global answer
    if height >= B:
        answer = min(answer,height-B)
        return
    if n >= N:
        return
    elif n < N:
        looking(n+1,height+people[n])
        looking(n+1,height)

T = int(input())
for tc in range(1,T+1):
    N, B = map(int,input().split())
    people = list(map(int,input().split()))
    answer = 100000
    looking(0,0)
    print('#{} {}'.format(tc,answer))

