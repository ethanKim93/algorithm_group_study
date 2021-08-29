import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int,input().split())
    cheese = list(map(int, input().split()))
    pizza = [i for i in range(M)]  # 몇번 피자인지 구별을 위한 피자인덱스
    #print(pizza)

    ov = pizza[:N]

    while len(ov) > 1: # 피자가 하나 남을 때 까지
        if cheese[ov[0]] != 1: # 치즈가 1이 안된 피자는 (0이면 4개 테스트 케이스 틀림 왜?)
            cheese[ov[0]] = cheese[ov[0]] // 2 # 절반 날림
            ov.append(ov.pop(0)) # 피자 인덱스 위치 변경
        else:
            ov.pop(0)
            if N != M:        # 피자 - 화덕 = 안들어간 피자
                ov.append(pizza[N]) # 화덕의 크기 번호는 들어오지 않은 첫번째 피자
                N += 1

    print('#{} {}'.format(tc,ov[0]+1))

