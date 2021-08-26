import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))
    pizza = [[i + 1, int(cheese[i])] for i in range(M)]  # [피자번호, 치즈] 이중 리스트 생성
    fire_pot = pizza[:N]  # 화덕에 넣을 피자
    ready_pizza = pizza[N:]  # 화덕에 못넣고 준비된 피자

    while len(fire_pot) != 1:  # 화덕에 피자가 하나 남을 때까지
        target = fire_pot.pop(0)  # 화덕에서 하나씩 꺼내며 치즈 확인
        target[1] //= 2  # 치즈 굽기
        if target[1]:  # 치즈가 0이 아니면
            fire_pot.append(target)  # 다시 화덕으로
        elif ready_pizza:  # 치즈가 0이고 준비된 피자가 있다면
            fire_pot.append(ready_pizza[0])  # 준비된 피자를 화덕으로
            del ready_pizza[0]  # 넣은 피자는 준비된 피자에서 삭제

    print('#{} {}'.format(tc, fire_pot[0][0]))
