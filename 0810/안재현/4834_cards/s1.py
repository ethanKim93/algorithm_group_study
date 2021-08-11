import sys
sys.stdin = open('sample_input.txt')


A = int(input())
for a in range(0, A):
    length = input()
    c_list = list(map(int, list(input())))

    num_list = [0] * 10
    for j in c_list:

        num_list[j] += 1

    index = 0
    cnt = 0

    for i in range(9, -1, -1):
        if num_list[i] > cnt:
            cnt = num_list[i]
            index = i

    print("#{} {} {}".format(a+1, index, cnt))