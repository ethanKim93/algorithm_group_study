T = int(input())

for tc in range(1, T+1):
    N = float(input())

    result = ''
    cnt = 1
    # N = 0.625 = 1*2^(-1) + 0*2^(-2) + 1*2^(-3) = 1 + 0*2^(-1) + 1*2^(-2) = ...
    # 0.625 => 1.25 => 0.25 => 0.5 => 1
    while True:
        # 12번을 초과하면 overflow 출력
        if cnt > 12:
            result = 'overflow'
            break

        N *= 2
        if N == 1:
            result += '1'
            break
        elif N > 1:
            result += '1'
            N -= 1
        else:
            result += '0'
        cnt += 1                # cnt 증가

    print('#{} {}'.format(tc, result))