# 뭐여 이게
import sys
sys.stdin = open('sample_input.txt')


T = int(input())
for tc in range(T):
    tw = list(input())
    th = list(input())
    result = '0'
    for i in range(len(tw)):
        twtmp = tw[:]
        for j in range(len(th)):
            thtmp = th[:]
            if twtmp[i] == '0':
                twtmp[i] = '1'
                if thtmp[j] == '1':
                    thtmp[j] = '0'
                elif thtmp[j] == '2':
                    thtmp[j] = '0'
                if int(''.join(twtmp), 2) == int(''.join(thtmp), 3):
                    result = int(''.join(twtmp), 2)
                    # print('1')
                thtmp = th[:]
                if thtmp[j] == '0':
                    thtmp[j] = '1'
                elif thtmp[j] == '2':
                    thtmp[j] = '1'
                if int(''.join(twtmp), 2) == int(''.join(thtmp), 3):
                    result = int(''.join(twtmp), 2)
                    # print('2')
                thtmp = th[:]
                if thtmp[j] == '0':
                    thtmp[j] = '2'
                elif thtmp[j] == '1':
                    thtmp[j] = '2'
                if int(''.join(twtmp), 2) == int(''.join(thtmp), 3):
                    result = int(''.join(twtmp), 2)
                    # print('3')
                twtmp[i] = '0'
            elif twtmp[i] == '1':
                twtmp[i] = '0'
                if thtmp[j] == '1':
                    thtmp[j] = '0'
                elif thtmp[j] == '2':
                    thtmp[j] = '0'
                if int(''.join(twtmp), 2) == int(''.join(thtmp), 3):
                    result = int(''.join(twtmp), 2)
                    # print('4')
                thtmp = th[:]
                if thtmp[j] == '0':
                    thtmp[j] = '1'
                elif thtmp[j] == '2':
                    thtmp[j] = '1'
                if int(''.join(twtmp), 2) == int(''.join(thtmp), 3):
                    result = int(''.join(twtmp), 2)
                    # print('5')
                thtmp = th[:]
                if thtmp[j] == '0':
                    thtmp[j] = '2'
                elif thtmp[j] == '1':
                    thtmp[j] = '2'
                if int(''.join(twtmp), 2) == int(''.join(thtmp), 3):
                    result = int(''.join(twtmp), 2)
                    # print('6')
                twtmp[i] = '1'

    print('#{} {}'.format(tc + 1, result))