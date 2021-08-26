import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    pizza = [(i+1, C[i]) for i in range(M)]  # 위치와 치즈 함께 저장

    in_pot = pizza[:N]  # 화덕으로 들어갈 피자
    out_pot = pizza[N:]  # 대기할 피자

    while len(in_pot) != 1:
        (idx, che) = in_pot.pop(0)  # 위치, 치즈양
        che //= 2  # 치즈 1/2
        if che:
            in_pot.append((idx, che))
        else:
            if out_pot:
                in_pot.append(out_pot.pop(0))
    print('#{} {}'.format(tc, in_pot[0][0]))

