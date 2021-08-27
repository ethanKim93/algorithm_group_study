import sys
sys.stdin = open("sample_input.txt")

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    pizza = list(map(int,input().split()))
    oven = [0] # 구워지는 오븐
    finish = [] #구워진 순서
    num = 1
    while oven:
        if len(oven) < N and num < M: #오븐에 빈자리가 있고, 피자수를 넘지 않았다면
            oven.append(num) #피자 추가
            num += 1
        else:
            check = oven.pop(0) #맨앞에 피자 확인
            pizza[check] = pizza[check] // 2 #2로 나눔
            if pizza[check]: #피자 치즈가 다 녹았는지 확인, 녹지 않았다면
                oven.append(check)
            else:# 다녹았다면 finish에 추가
                finish.append(check)
    print('#{} {}'.format(tc,finish[-1]+1))
