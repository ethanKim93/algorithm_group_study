import sys
sys.stdin = open("input.txt")

def find(w,temps):
    global ans
    if w == n:
        if ans > temps >= h:
            ans = temps
        return

    if temps >= ans:
        return

    find(w+1, temps)
    find(w+1, temps + maps[w])

t = int(input())
for tc in range(1, t+1):
    n, h = map(int,input().split())
    maps = list(map(int,input().split()))

    ans = 987654321
    find(0,0)

    print("#{} {}".format(tc, ans-h))

# Pass