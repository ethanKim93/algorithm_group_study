import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    num, swap_count = input().split()
    num = list(map(int, num))
    swap_count = int(swap_count)

    while swap_count:
        for i in range(len(num)-1):
            max_idx = i
            for j in range(i+1, len(num)):
                if num[j] > num[max_idx]:
                    max_idx = j
        if num[i] != num[max_idx]:
            num[i], num[max_idx] = num[max_idx], num[i]
            swap_count -= 1

