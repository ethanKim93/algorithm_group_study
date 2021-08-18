import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    list_a = list(set(input()))
    list_b = list(input())

    num_max = 0

    for i in range(len(list_a)):
        count = 0
        for j in range(len(list_b)):
            if list_a[i] == list_b[j]:
                count += 1
        if num_max < count:
            num_max = count

    print('#{} {}'.format(tc, num_max))
