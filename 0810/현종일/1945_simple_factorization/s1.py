import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    N = int(input())
    result = [0, 0, 0, 0, 0]
    fac_list = [2, 3, 5, 7, 11]
    for i in range(len(fac_list)):
        stopper = False
        while not stopper:
            if not N % fac_list[i]:
                N = N // fac_list[i]
                result[i] = result[i]+1
            else:
                stopper = True

    print('#{} {}'.format(tc, ' '.join(map(str, result))))
