import sys
sys.stdin = open('input.txt')
def sinergyfunction(S):
    sinergy = 0
    for i in range(len(S)):
        for j in range(len(S)):
            if i != j:
                sinergy += arr[S[i]][S[j]]
    return sinergy
def team(n,S):
    global min_diff
    if len(S)==N//2:
        notS = []
        for i in range(N):
            if i not in S:
                notS.append(i)
        diff = abs(sinergyfunction(S)-sinergyfunction(notS))
        min_diff = min(diff,min_diff)
        return
    if n < N:
        team(n+1,S+[n]) #n을 0번 팀에 넣는 경우
        team(n+1,S)     #n을 반대 팀에 넣는 경우

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    min_diff = 1000
    team(1,[0])
    print("#{} {}".format(tc,min_diff))