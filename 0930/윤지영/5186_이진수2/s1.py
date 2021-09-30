import sys
sys.stdin = open('sample_input (1).txt')

T = int(input())
for tc in range(1,T+1):
    N = float(input())
    result = ''
    for i in range(1,13):
        cal = 2 ** (-i)
        if N :
            if N >= cal:
                result += '1'
                N -= cal
            else:
                result += '0'
        else:
            break
    if N :
        result = 'overflow'
    print('#{} {}'.format(tc,result))








