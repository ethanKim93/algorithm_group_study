import sys
sys.stdin = open('GNS_test_input.txt')

encode = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
decode = dict(map(reversed, encode.items()))  # reversed 내장함수 이용, dict의 key와 value를 바꿈

T = int(input())
for test_case in range(1, T+1):
    test_case_number, length = input().split()
    numbers = input().split()

    # 숫자로 변환
    changed = []
    for num in numbers:
        changed.append(encode[num])

    # 숫자에서 순서대로 정렬 ## 버블정렬 써보기 ## sort() 쓰면 쉽긴 함
    for i in range(len(changed)-1, 0, -1):  # 뒤에서부터 정렬, 맨앞은 자동 정렬되어서 포함
        for j in range(0, i):
            if changed[j] > changed[j+1]:  # 앞의 값이 더 크면, 자리를 바꾸기 (내림차순은 부호 반대)
                changed[j], changed[j+1] = changed[j+1], changed[j]

    # 숫자를 key로 가진 이상한 숫자를 value로 가진 dict에서 추출해서 출력
    decoded = []
    for i in changed:
        decoded.append(decode[i])
    print(test_case_number)
    print(*decoded)

