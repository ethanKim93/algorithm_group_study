import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    L = int(input())
    buildings = list(map(int, input().split()))

    sunny_total = 0
    for i in range(2, L-2):
        if buildings[i] <= buildings[i-2] or buildings[i] <= buildings[i-1] or buildings[i] <= buildings[i+1] or buildings[i] <= buildings[i+2]:
            continue
        if buildings[i-2] >= buildings[i-1] and buildings[i-2] >= buildings[i+1] and buildings[i-2] >= buildings[i+2]:
            sunny_total =  sunny_total + (buildings[i]-buildings[i-2])
        elif buildings[i-1] >= buildings[i-2] and buildings[i-1] >= buildings[i+1] and buildings[i-1] >= buildings[i+2]:
            sunny_total =  sunny_total + (buildings[i]-buildings[i-1])
        elif buildings[i+1] >= buildings[i-2] and buildings[i+1] >= buildings[i-1] and buildings[i+1] >= buildings[i+2]:
            sunny_total =  sunny_total + (buildings[i] - buildings[i+1])
        elif buildings[i+2] >= buildings[i-2] and buildings[i+2] >= buildings[i-1] and buildings[i+2] >= buildings[i+1]:
            sunny_total =  sunny_total + (buildings[i] - buildings[i+2])
    print('#{} {}'.format(tc, sunny_total))



