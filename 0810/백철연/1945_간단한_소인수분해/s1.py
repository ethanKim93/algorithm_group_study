import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = [2, 3, 5, 7, 11]         #소인수 리스트
    count = [0] * 5                    #담을 리스트
    for i in range(len(numbers)):
        while 1:
            if N % numbers[i] == 0:    # N이 나누어 떨어지면 소인수로 나누어 주고
                N = N//numbers[i]      # 빈 리스트에 할당
                count[i] += 1
            else:
                break                  # 더이상 나누어 떨어지지 않으면 for문으로 돌아감


    print('#{0} {1}'.format(tc, count))
