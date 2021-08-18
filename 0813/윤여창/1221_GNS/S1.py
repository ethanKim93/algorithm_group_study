import sys
sys.stdin = open('GNS_test_input.txt')

T = int(input())

for test_case in range(1, T + 1):
    num, total = input().split()
    target_list = input().split()
    count_list = [0] * 10
    number_dict = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9 }
    result = ''

    for i in range(int(total)):
        current_num = number_dict.get(target_list[i])
        count_list[current_num] += 1

    for key, value in number_dict.items():
        result += (key + ' ') * count_list[value]

    print(num)
    print(result[:-1])