import sys
sys.stdin = open("sample_input.txt")

code_16 = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,'7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,'C': 12,'D': 13,'E': 14,'F': 15
    }

for tc in range(1, int(input())+1):
    N, n_16 = input().split()

    n_2 = ''
    for i in range(len(n_16)):
        n_10 = code_16[n_16[i]]
        tmp = ''

        while n_10 > 1:
            tmp = (str(n_10 % 2)) + tmp
            n_10 //= 2

        tmp = str(n_10) + tmp
        if len(tmp) < 4:
            tmp = '0' * (4-len(tmp)) + tmp
        n_2 += tmp

    print("#{} {}".format(tc, n_2))