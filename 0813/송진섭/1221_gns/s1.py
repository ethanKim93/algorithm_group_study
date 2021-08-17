import sys
sys.stdin = open('GNS_test_input.txt')


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_i = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]
    return arr


T = int(input())
for tc in range(1, T+1):
    t, n = input().split()
    strange_num = input().split()
    n = int(n)
    strange_dict = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    strange_code = {0: 'ZRO', 1: 'ONE', 2: 'TWO', 3: 'THR', 4: 'FOR', 5: 'FIV', 6: 'SIX', 7: 'SVN', 8: 'EGT', 9: 'NIN'}
    result = []
    real_result = []
    for i in range(n):
        result.append(strange_dict.get(strange_num[i]))

    sort_result = selection_sort(result)

    for j in range(n):
        real_result.append(strange_code.get(sort_result[j]))

    print('{}'.format(t))
    print(*real_result)








