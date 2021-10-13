import sys
sys.stdin = open('input.txt')

T = int(input())

def height(total, B, index):
    global result


    if index == len(steps) - 1:
        if total >= B and result > total:
            result = total
        return

    if result < total:
        return

    height(total + steps[index], B, index + 1)
    height(total, B, index + 1)

for tc in range(1, 1 + T):
    N, B = map(int, input().split())
    steps = sorted(list(map(int, input().split())))
    result = sum(steps)

    height(0, B, 0)
    print("#{} {}".format(tc, result - B))