import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    data = list(map(int, input().split()))

    while 0 not in data:
        for minus in range(1, 6):
            first = data.pop(0)

            if first-minus > 0:
                first -= minus
            else:
                first = 0
            data.append(first)
            if first == 0:
                break

    print('#{}'.format(N), * data)
