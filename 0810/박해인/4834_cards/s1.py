import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input()) # 카드 장수 N
    numbers = list(map(int, input())) # 숫자 하나씩 쪼개서 list 형변환

    max_num = -1 # 가장 많은 카드 숫자
    max_count = 0 # 그 숫자의 장수

    for i in range(10): # 0~9 숫자 순회
        if numbers.count(i) >= max_count:
            max_num = i # 가장 큰 값 i
            max_count = numbers.count(i)  # i의 개수 count


    print('#{} {} {}'.format(test_case, max_num, max_count))
