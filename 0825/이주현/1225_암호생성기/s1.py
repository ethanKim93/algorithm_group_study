import sys
sys.stdin = open('input.txt', 'r')

def cycle():
    global stop
    for i in range(1, 6):
        tmp = nums.pop(0) - i
        if tmp <= 0:
            nums.append(0)
            stop = True
            return
        else:
            nums.append(tmp)
    return

for _ in range(1, 11):
    tc = input()
    nums = list(map(int, input().split()))
    stop = False
    while stop == False:
        cycle()

    print("#{}".format(tc), end=" ")
    print(*nums)