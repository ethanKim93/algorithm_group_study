import sys
sys.stdin = open("input.txt")

for tc in range(1,11):
    N, M = input().split()
    num_list = []
    top = -1
    for num in M:
        if len(num_list) and num_list[top] == num:
            num_list.pop()
            top -= 1
        else:
            num_list.append(num)
            top += 1

    print('#{}'.format(tc), end=" ")
    print(''.join(num_list))