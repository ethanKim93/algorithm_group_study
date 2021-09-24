import sys
sys.stdin = open("input.txt")

def postorder(l):
    if values[l-1] and l > n:
        return 0
    if values[l]:
        return values[l]
    return postorder(l*2) + postorder(l*2+1)

t = int(input())
for tc in range(1,t+1):
    n,m,l = map(int,input().split())
    values = [0]*(n+1)
    for i in range(m):
        num, value = map(int,input().split())
        values[num] = value

    print("#{} {}".format(tc,postorder(l)))