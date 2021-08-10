import sys
sys.stdin = open('sample_input.txt')

t = int(input())
for i in range(1, t+1):
    n = int(input())
    num_list = list(map(int, input().split()))

    def num_max(nlist):
        max_num = num_list[0]
        for num in num_list:
            if num > max_num:
                max_num = num
        return max_num

    def num_min(nlist):
        min_num = num_list[0]
        for num in num_list:
            if num < min_num:
                min_num = num
        return min_num

    result = num_max(num_list) - num_min(num_list)
    print('#{} {}'.format(i, result))

