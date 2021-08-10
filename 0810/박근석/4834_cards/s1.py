import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, list(input())))
    list_a = [0 for i in range(10)] #각 숫자가 들어갈 리스트 생성

    for i in nums:
        list_a[i] += 1 #카드 숫자와 일치하는 인덱스 값에 카드를 한개씩 카운트


    index_a = 0
    max_num = 0
    for j in range(0, len(list_a)): #가장 많은 개수의 카드 찾기
        if max_num < list_a[j]:
            max_num = list_a[j]
            index_a = j

    print('#{} {} {}'.format(tc, index_a, max_num))





