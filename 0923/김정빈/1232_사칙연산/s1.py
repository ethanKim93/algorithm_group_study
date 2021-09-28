import sys
sys.stdin = open("input.txt")
#1232. [S/W 문제해결 기본] 9일차 - 사칙연산
def inorder():
    global res


N = int(input())
tree = [0]*(N+1)
res = 0
for _ in range(N):
    p = list(input().split())
    print(p)
    if len(p) > 2:
        tree[int(p[0])] = p[1]
        tree[int(p[0])*2] = int(p[2])
        tree[int(p[0])*2+1] = int(p[3])
    else:
        tree[int(p[0])] = int(p[1])
print(tree)
"""
#1 13
#2 20
#3 35
#4 107
#5 369
#6 76
#7 123
#8 313
#9 238
#10 2
"""