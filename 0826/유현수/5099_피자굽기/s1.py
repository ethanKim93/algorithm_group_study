import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))

    pizza = []
    for idx, chs in enumerate(cheese):              # [피자 번호, 치즈 양]으로 이루어진 pizza 리스트 생성
        pizza.append([idx+1, chs])

    queue = []
    for _ in range(N):                              # 화덕의 크기만큼 피자 꺼내서 넣기
        queue.append(pizza.pop(0))

    while len(queue) > 1:                           # 화덕에 피자가 1개 남을 때까지 반복
        check = queue.pop(0)                        # 화덕에서 피자를 꺼내서
        check[1] //= 2                              # 치즈가 반 줄어든 것을 확인
        if check[1]:                                # 치즈가 남아있으면
            queue.append(check)                     # 화덕의 맨 뒤에 넣기
        else:                                       # 치즈가 모두 녹았고
            if pizza:                               # 구울 피자가 남아있으면
                queue.insert(0, pizza.pop(0))       # 방금 꺼낸 자리에 새 피자 넣기

    print('#{} {}'.format(tc, queue[0][0]))
