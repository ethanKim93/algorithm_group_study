import sys
sys.stdin = open('sample_input.txt')

def pizza(N, M):
    rota = [] # 화덕 안에서 로테이션 돌 피자들
    num_li = [i for i in range(1, M+1)]
    num = [] # 화덕 안에 있는 피자의 숫자

    for _ in range(N):
        rota.append(pizza_li.pop(0))
        num.append(num_li.pop(0)) # 초기 설정

    while len(rota) != 1: # 값이 한 개 남을 때까지
        a = rota.pop(0)
        if a//2 == 0: # 치즈가 다 녹으면
            if pizza_li: # 피자가 아직 남아있으면
                rota.insert(0,pizza_li.pop(0)) # 다 녹은 피자 치즈 위에 다른 피자를 넣어줌
                num.pop(0)
                num.insert(0,num_li.pop(0))
            else:
                num.pop(0) # 대기 중인 피자가 없으므로 해당 피자 숫자 out
        else:
            rota.append(a//2)
            b= num.pop(0)
            num.append(b) # 피자 치즈가 남아있으면 피자도, 피자의 숫자도 pop한 뒤 다시 append

    return num

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    pizza_li= list(map(int, input().split()))

    print('#{} {}'.format(tc+1,*pizza(N,M)))