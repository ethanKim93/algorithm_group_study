import sys
sys.stdin = open("input.txt")
t = int(input())
def postorder(n):
    global cnt

    if temps1[n]:
        postorder(temps1[n])
        cnt += 1
    if temps2[n]:
        postorder(temps2[n])
        cnt += 1
    return cnt

for tc in range(1, t+1):
    e, n = map(int, input().split())
    maps = list(map(int, input().split()))
    temps1 = [0]*(e+2)
    temps2 = [0]*(e+2)
    for i in range(0,len(maps)-1,2):
        if temps1[maps[i]]:
            temps2[maps[i]] = maps[i+1]
        else:
            temps1[maps[i]] = maps[i+1]

    cnt = 1
    print("#"+str(tc) + " " + str(postorder(n)))