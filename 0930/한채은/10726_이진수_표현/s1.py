import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    # binary를 이진수로 변환해주고
    binary = bin(M)[2:]
    check = 1

    # binary가 N보다 클때
    if len(binary) >= N:
        # N까지 돌면서
        for i in range(N):
            # 뒷자리부터 확인해서 0이면
            if binary[-1-i] == '0':
                #check를 0으로 바꿔주고
                check = 0
                # OFF 반환한다음 break
                print('#{} {}'.format(tc, 'OFF'))
                break
        # 위에서 걸렀으니까
        # check가 1이면 ON 출력
        if check == 1:
            print('#{} {}'.format(tc, 'ON'))

    # N보다 작으면 OFF
    else:
        print('#{} {}'.format(tc, 'OFF'))