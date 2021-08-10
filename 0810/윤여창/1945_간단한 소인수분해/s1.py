import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    number_list = [2, 3, 5, 7, 11]
    cnt_box = [0] * 5

    for i in range(4, -1, -1):
        while not N % number_list[i]:
            cnt_box[i] += 1
            N /= number_list[i]
    print('#{} {} {} {} {} {}'.format(tc, cnt_box[0], cnt_box[1], cnt_box[2], cnt_box[3], cnt_box[4]))

