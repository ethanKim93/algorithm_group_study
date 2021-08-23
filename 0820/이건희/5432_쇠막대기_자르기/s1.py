import sys

sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t + 1):
    maps = input()
    maps_m = maps.replace("()", "/")

    status = ans = steel = 0
    for i in maps_m:
        if i == '(':
            status += 1
            steel += 1
        elif i == ')':
            status -= 1
        else:
            ans += status

    ans += steel

    print("#{} {}".format(tc, ans))
