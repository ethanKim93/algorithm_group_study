import sys
sys.stdin = open('input.txt')

def check(i):
    if i <= 1:
        if buildings[i] - buildings[i+1] > 0 and buildings[i] - buildings[i+2] > 0:
            return True
    elif num-2 <= i:
        if buildings[i] - buildings[i-2] > 0 and buildings[i] - buildings[i-1] > 0:
            return True
    elif buildings[i] - buildings[i-2] > 0 and buildings[i] - buildings[i-1] > 0:
        if buildings[i] - buildings[i+1] > 0 and buildings[i] - buildings[i+2] > 0:
            return True

    return False


def find_min(i):
    cand = []
    cand.extend([buildings[i] - buildings[i-2], buildings[i] - buildings[i-1], buildings[i] - buildings[i+1], buildings[i] - buildings[i+2]])
    mn = 255
    for x in cand:
        if x < mn:
            mn = x

    return mn

for tc in range(10):
    num = int(input())
    buildings = list(map(int, input().split()))
    ans = 0

    for i in range(num):
        if check(i):
            ans += find_min(i)

    print("#{} {}".format(tc+1,ans))