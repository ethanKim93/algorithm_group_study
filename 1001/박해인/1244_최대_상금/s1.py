# input testcase는 다 맞는데 swea제출하면 10개중에 7개만 맞는데 뭐가 틀린지 모르겠습니다 :(
import sys
sys.stdin = open('input.txt')

def biggest_prize(temp, depth, now):
    global result

    if depth == ability:
        result = max(int(temp), result)
    else:
        for pick1 in range(now, len(numbers)-1):
            for pick2 in range(pick1+1, len(numbers)):
                temp = list(temp)
                if temp[pick1] <= temp[pick2]:
                    temp[pick1], temp[pick2] = temp[pick2], temp[pick1]
                    biggest_prize(''.join(temp), depth+1, pick1)
                    temp[pick1], temp[pick2] = temp[pick2], temp[pick1]

T = int(input())
for test_case in range(1, T+1):
    numbers, ability = input().split()
    numbers = list(numbers)
    ability = int(ability)
    result = 0

    biggest_prize(numbers, 0, 0)
    print('#{} {}'.format(test_case, result))
