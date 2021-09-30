import sys
sys.stdin = open('sample_input.txt')


T = int(input())
for tc in range(1, T+1):
    N = input()

    a, b= N.split('.')
    b = float('0.'+b)
    first_b = b
    res = []
    cnt = 0
    while cnt <= 12:
        b = b*2
        check_num = b
        a, b = str(b).split('.')
        res.append(a)
        b = float('0.' + b)
        if check_num % 1 == 0 or b == first_b:
            break
        cnt += 1
    if len(res) > 12:
        print('#{} overflow'.format(tc))
    else:
        print('#{} {}'.format(tc, ''.join(res)))

