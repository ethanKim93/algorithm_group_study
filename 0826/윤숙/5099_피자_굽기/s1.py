import sys

sys.stdin = open('input.txt', 'r')
T = int(input())

for tc in range(1, T + 1):

    N, M = map(int, input().split())  # 화덕의 제한크기, 피자의 갯수
    C = input().split()
    pizza = []
    for i in range(M):  # 한시간 가량 입력을 잘못받아서 삽질을 했었다;; 잠이 덜깼나부다..
        pizza.append((i + 1, int(C[i])))  # 인덱스, 치즈갯수

    inoven = pizza[:N]  # 화덕의 제한 크기만큼 피자의 개수를 나눠줌 (화덕안에 들어간 피자)
    outoven = pizza[N:]  # 화덕 밖의 대기중인 피자들

    while len(inoven) != 1:  # 화덕안에 피자가 없으면 반복을 중지
        num, p = inoven.pop(0)  # 인덱스와 치즈개수를

        tmp = p // 2  # 치즈를 꺼내서 확인
        if tmp <= 0:  # 치즈가 0이면 오븐밖에 피자가 있으면 꺼내서 안에 넣는다.
            if outoven:
                inoven.append(outoven.pop(0))
        elif tmp > 0:  # 치즈가 있으면 다시 오븐안으로 넣는다.
            inoven.append((num, tmp))

    print('#{} {}'.format(tc, inoven[0][0]))
