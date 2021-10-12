import sys
sys.stdin = open('input.txt')

def verify(three, ans):
    dif = three - ans
    if dif < 0:
        dif = -dif
    while dif > 2:
        if dif % 3:
            return False
        dif //= 3
    return True


for tc in range(1, 1 + int(input())):
    two = input();
    twoN = int(two, 2)
    three = input();
    threeN = int(three, 3)
    for shift in range(len(two)):
        ans = twoN ^ (1 << shift)
        if verify(threeN, ans):
            break
    print(f"#{tc} {ans}")