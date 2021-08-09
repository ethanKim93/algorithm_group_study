import sys
sys.stdin = open('input.txt')

for tc in range(1,11): #입력값이 10개의 테스트 케이스라고 했으니까
    L = int(input())
    buildings = list(map(int, input().split()))

    view = 0

    for i in range(2, L-2) :#왼쪽 두칸, 오른쪽 두칸이 비어있으니까 범위를 2부터 L-2까지
        m = buildings[i]
        l1 = buildings[i-1]
        l2 = buildings[i-2]
        r1 = buildings [i+1]
        r2 = buildings [i+2]
        if m > l1 and m > l2 and m > r1 and m > r2:
            h1 = m - l1
            h2 = m - l2
            h3 = m - r1
            h4 = m - r2
            llist = [h1,h2,h3,h4]

            for h in llist:
                if h < h1:
                    h1 = h
            view = view + h1

    print('#{} {}'.format(tc,view))
