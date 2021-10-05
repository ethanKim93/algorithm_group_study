import sys
sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t+1):
    n, m = map(int,input().split())
    w = list(map(int,input().split()))
    t = list(map(int,input().split()))
    t = sorted(t)
    ans = 0
    while t:
        truck = t.pop(0)
        mx = 0
        for i in range(len(w)):
            if truck >= w[i] > mx:
                mx_idx, mx = i, w[i]

        if mx:
            ans += mx
            del w[mx_idx]

    print("#{} {}".format(tc,ans))