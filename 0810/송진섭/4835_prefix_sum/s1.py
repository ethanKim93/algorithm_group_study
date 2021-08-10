import  sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) #N개의 정수 M개 범위의 구간
    numbers = list(map(int, input().split()))

    total_list = [] #각 테스트의 total값 배열 생성

    for i in range(N-M+1): #인덱스 에러방지 뒤의 구간 M만큼 남기기
        total = 0
        for j in range(i, M+i): #i에서 M구간 까지 합 구하기
            total += numbers[j]
        total_list.append(total)

    for i in range(len(total_list) - 1, 0, -1): # 버블정렬을 통해 total_list 최대.최소값 도출
        for j in range(i):
            if total_list[j] > total_list[j + 1]:
                total_list[j], total_list[j + 1] = total_list[j + 1], total_list[j]
    max_number = total_list[-1]
    min_number = total_list[0]
    result = max_number - min_number

    print('#{} {}'.format(tc, result))

