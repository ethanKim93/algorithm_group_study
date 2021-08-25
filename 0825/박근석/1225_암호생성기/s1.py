import sys
sys.stdin = open('input.txt')

def check(num):
    queue = []
    front = -1

    while True:
        for i in range(1, 6):
            front += 1
            num.append(num[front] - i)
            if num[-1] <= 0:
                num[-1] = 0
                return num[front+1:]

for i in range(1, 11):
    tc = int(input())
    num = list(map(int, input().split()))

    print('#{} {}'.format(tc, ' '.join(map(str, check(num)))))