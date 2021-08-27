import sys
sys.stdin = open('sample_input.txt')

t = int(input())
for tc in range(1,t+1):
    n, m = map(int,input().split()) #화덕크기, #피자 개수 ex) 3 5
    cheese = list(map(int,input().split())) #ex) 7 2 6 5 3
    pizza_num = []  #들어갈 피자 번호  7 2 6 5 3
    for i in range(m):              #  0 1 2 3 4
        pizza_num.append(i)
    queue = pizza_num[0:n]  #queue값 설정  ex) 7 2 6
    print(queue)
    while len(queue) != 1:  # 화덕 속 피자가 1개가 될 때까지.
        if cheese[queue[0]] != 1: #투입구에 도착한 0번째 피자가 치즈양이 1이 아니면
            cheese[queue[0]] = cheese[queue[0]] // 2 #절반 줄인다.
            queue.append(queue.pop(0))  # 빼고, 맨 뒤로 돌리기
        else:  # 투입구에 도착한 치즈량이 1이라면
            queue.pop(0) #뺀다
            if n != m:  # M개를 다 넣을 때까지
                queue.append(pizza_num[n])
                n += 1  # 다음넣어야 하는 피자 순서를 위해

    print('#{} {}'.format(tc, queue[0]+1))