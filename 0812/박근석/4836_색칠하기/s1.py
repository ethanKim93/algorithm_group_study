import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    set1 = set() # 빨간색, 파란색 좌표가 들어갈 set타입 변수 생성
    set2 = set()
    for c in range(N):
        list_a = list(map(int, input().split()))
        if list_a[4] == 1: # 빨간색 좌표를 set1에 add
            for i in range(list_a[0], list_a[2]+1):
                for j in range(list_a[1], list_a[3]+1):
                    set1.add((i, j))

        else: # 파란색 좌표를 set2에 add
            for i in range(list_a[0], list_a[2]+1):
                for j in range(list_a[1], list_a[3]+1):
                    set2.add((i, j))

    print('#{} {}'.format(tc, len(set1&set2))) # set1, set2의 교집합 개수를 출력