import sys
sys.stdin = open('sample_input.txt')
#비트 연산자로 풀이
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    box = [[0] * 10 for _ in range(10)] # 전체 격자
    count_box = [0] * 4 # 나중에 각각의 색칠 수를 셀 카운팅 정렬용 리스트
    for _ in range(N):
        area = list(map(int, input().split()))
        for i in range(area[0],area[2]+1): # 색칠할 격자 범위
            for j in range(area[1],area[3]+1):
                box[i][j] = box[i][j] | area[4] # 이진수로 빨강 01, 파랑 10일때 보라를 11로 간주하면 or 연산자로 같은 색이 겹치는 경우와 색칠이 쉬워집니당
    for i in range(10): #카운팅 정렬
        for j in range(10):
            count_box[box[i][j]] += 1
    print('#{} {}'.format(tc, count_box[3]))
