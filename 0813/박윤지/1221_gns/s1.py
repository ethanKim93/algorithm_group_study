import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())

for tc in range(1, T+1):
    list1 = input().split()

    length = int(list1[1])
    nums = list(input().split())
    trans = []
    result = []

    dict_num = {'ZRO': 0,
                'ONE': 1,
                'TWO': 2,
                'THR': 3,
                'FOR': 4,
                'FIV': 5,
                'SIX': 6,
                'SVN': 7,
                'EGT': 8,
                'NIN': 9}

    reverse_dict = dict(map(reversed, dict_num.items()))

    for num in nums:
        trans.append(dict_num[num])

    # 숫자로된 리스트 선택정렬
    for i in range(0, len(trans)-1):
        minIdx = i
        for j in range(i+1, len(trans)):
            if trans[minIdx] > trans[j]:
                minIdx = j
        trans[i], trans[minIdx] = trans[minIdx], trans[i]

    # 숫자로 된 리스트 다시 외계어로
    for num in trans:
        result.append(reverse_dict[num])

    print(list1[0])
    print(*result)