import sys
sys.stdin = open('input.txt')



for tc in range(1, 11):
    L = int(input())
    buildings = list(map(int, input().split()))

    total = 0

    for building in range(2,L-2):
        r_view1 = buildings[building] - buildings[building-2]
        r_view2 = buildings[building] - buildings[building-1]
        r_view3 = buildings[building] - buildings[building+1]
        r_view4 = buildings[building] - buildings[building+2]
        # 3번째 빌딩 부터 시작해서 뒤2 뒤1 앞1 앞2의 차이 구함
        if r_view1 > 0 and r_view2 > 0 and r_view3 > 0 and r_view4 > 0:
        # 처음에 > 0 보다 크다는 조건을 안걸어서 다 - 값이 나왔음 ;;
            if r_view1 >= r_view2:
                lis1 = r_view2
            else:
                lis1 = r_view1

        #각 view를 비교해서 작은 값을 할당
            if r_view3 >= r_view4:
                lis2 = r_view4
            else:
                lis2 = r_view3
        # 각 view를 비교해서 작은 값을 할당
            if lis1 >= lis2:
                total += lis2
            else:
                total += lis1
        #각 view를 비교해서 작은 값을 할당

        #print(total)
    print('#{} {}'.format(tc, total))










