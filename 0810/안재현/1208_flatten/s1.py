import sys
sys.stdin = open('input.txt')

for a in range(0, 10):
    inp = int(input())
    B_list = list(map(int, input().split()))

    for b in range(0, inp):

        B_list[0] += 1
        B_list[len(B_list) - 1] -= 1

        for i in range(len(B_list) - 1, 0, -1):
            for j in range(i):
                if B_list[j] > B_list[j + 1]:
                    B_list[j], B_list[j + 1] = B_list[j + 1], B_list[j]

    print('#{} {}'.format(a+1, B_list[len(B_list)-1]-B_list[0]))


