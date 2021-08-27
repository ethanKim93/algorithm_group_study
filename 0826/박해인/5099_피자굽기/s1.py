# 화덕에 가장 마지막까지 남아있는 피자 번호
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1):
    N, M = map(int, input().split())  # 화덕의 크기 N, 피자 개수 M
    Ci = list(map(int, input().split()))  # M개의 피자에 뿌려진 치즈의 양
    tag = [i for i in range(1, M+1)]  # 피자의 숫자 태그

    print(tag)
    oven = []  # 화덕
    # 화덕이 꽉찰 때 까지 피자를 꺼내서 피자를 넣는다.
    while len(oven) <= N:
        oven.append(Ci.pop(0))

    print(oven)

    # oven.append(oven.pop(0)//2)

    while True:
        # 한바퀴 돌고 치즈가 Ci//2가 된다.
        for cheese in range(N+1):
            p = oven.pop(0)
            melted = p // 2
            oven.append(melted)
            if oven[0] == 0:  # 다 녹은 치즈가 1번자리에 오면
                if Ci:  # 피자가 남아 있으면
                    oven[0] = Ci.pop(0)  # 빈 자리에 새 피자를 넣는다.
                    break

