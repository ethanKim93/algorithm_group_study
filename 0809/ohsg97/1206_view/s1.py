import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    L = int(input())
    buildings = list(map(int, input().split()))

    total = 0

    for i in range(2, L-2):
        height = buildings[i]

        while height > buildings[i+1]:
            if height > buildings[i + 1] and height > buildings[i + 2]:
                if height > buildings[i - 1] and height > buildings[i - 2]:
                    height -= 1
                    total += 1
                else:
                    height -= 1
                    continue

            else:
                height -= 1
                continue

    print('#{} {}'.format(tc,total))