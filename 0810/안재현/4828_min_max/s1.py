import sys
sys.stdin = open('sample_input.txt')

A = int(input())

for a in range(0, A):
    inp = int(input())
    B_list = list(map(int, input().split()))
    for i in range(len(B_list) - 1, 0, -1):
        for j in range(i):
            if B_list[j] > B_list[j + 1]:
                B_list[j], B_list[j + 1] = B_list[j + 1], B_list[j]

    calc = B_list[inp - 1] - B_list[0]

    print('#{} {}'.format(a + 1, calc))
