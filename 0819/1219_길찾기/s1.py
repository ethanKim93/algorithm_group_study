import sys
sys.stdin = open("input.txt")

for _ in range(1, 11):
    tc, road = map(int,input().split())
    maps = list(map(int,input().split()))
    nmaps = []
    ans = 0
    stack = []
    already = []
    for i in range(road):
        nmaps.append([maps[2*i],maps[2*i+1]])

    s = 0
    while True:
        if s == 99:
            ans = 1
            break

        for i in range(road):
            if nmaps[i][0] == s and nmaps[i] not in stack and nmaps[i] not in already:
                stack.append(nmaps[i])
                s = nmaps[i][1]
                break

        else:
            if stack:
                end = stack.pop()
                s = end[0]
                already.append(end)
            else:
                break

    print("#{} {}".format(tc,ans))