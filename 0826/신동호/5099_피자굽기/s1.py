import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    pizza = [0] # 피자 번호
    cheese = [0] # 치즈 양
    i = 1 # 넣어줄 피자 번호
    while pizza: # 피자가 남아있을 때
        if not cheese[0]//2: # 돌아온 피즈치자의 양이 0일 때
            p = pizza.pop(0) # 피자를 화덕에서 꺼내고 번호 기록
            cheese.pop(0) # 치즈를 없애준다, 더 넣어줄 피자가 없을 경우 치즈 큐의 크기는 N보다 작음
            while C and len(pizza) < N: # 넣어줄 피자가 남아있고, 화덕이 비어있는 동안
                pizza.append(i) # 새 피자를 넣어준다
                cheese.append(C.pop(0)) # 새 피자 치즈의 양을 넣어준다
                i += 1 # 피자 번호 올리기
        else: #치즈가 덜 녹았을 때
            pizza.append(pizza.pop(0)) # 큐의 맨 뒤로 피자를 보낸다
            cheese.append(cheese.pop(0)//2) # 큐의 맨 뒤로 절반이 된 치즈를 보낸다
    print('#{} {}'.format(tc, p))

