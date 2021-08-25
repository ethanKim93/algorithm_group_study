import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())

    li = list(map(int, input().split()))

    while li[-1]:
        for i in range(1, 6):
            a = li.pop(0)
            if a-i <= 0:
                li.append(0)
                break
            else:
                li.append(a-i)


    result = ' '.join(map(str,li))
    print('#{} {}'.format(tc,result))
