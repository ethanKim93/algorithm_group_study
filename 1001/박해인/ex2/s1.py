# 연습문제 2 baby-gin greedy
"""
3
667767
054060
101123

"""
"""
#1 baby-gin
#2 baby-gin
#3 not baby-gin
"""
def is_babygin(numbers):
    count = [0 for _ in range(10)]  # 숫자의 등장 횟수를 저장할 리스트
    result = 0  # triplet과 run의 횟수를 담을 변수 result

    for num in numbers:
        count[num] += 1

    # 0~9까지 순회하면서, result를 구할 것
    i = 0
    while i < 10:
        # triplet
        if count[i] >= 3:
            count[i] -= 3
            result += 1

        # run
        if i < 10-2:  # 인덱스 유효 총 길이 - 2
            if count[i] == 1 and count[i+1] == 1 and count[i+2] == 1:
                count[i] -= 1
                count[i+1] -= 1
                count[i+2] -= 1
                result += 1

        i += 1

    if result == 2:
        return True

T = int(input())
for test_case in range(1, T+1):
    numbers = list(map(int, input()))
    if is_babygin(numbers):
        print('#{} baby-gin'.format(test_case))
    else:
        print('#{} not baby-gin'.format(test_case))





