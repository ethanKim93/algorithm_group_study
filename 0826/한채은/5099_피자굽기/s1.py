import sys
sys.stdin = open('sample_input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int,input().split()))
    # print(cheese)

    pizza_num = []  # 0, 1, 2, ...
    for i in range(M):
        pizza_num.append(i)

    queue = pizza_num[:N]   # 화덕에 N개 까지 들어갈 수 있으니까
    # print(queue)

    while len(queue) != 1:  # 한 개가 될 때까지 while
        if cheese[queue[0]] != 1:
            cheese[queue[0]] = cheese[queue[0]] // 2
            queue.append(queue.pop(0))  # pop해주고 다시 append
        else:  # 치즈 0이면 바로 pop
            queue.pop(0)
            if not N == M:  # M개를 다 넣을 때까지
                queue.append(pizza_num[N])
                N += 1  # 다음 피자


    print('#{} {}'.format(tc, queue[0]+1))