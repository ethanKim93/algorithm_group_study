import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split())) #화덕 크기, 피자 개수
    C = list(map(int, input().split())) #치즈양을 리스트 변수로 생성
    list_a = []
    for i in range(len(C)):             #피자 숫자와 치즈양을 리스트로 생성
        list_a.append([i+1, C[i]])
    queue = []
    for i in range(N):                  #처음 들어갈 피자를 화덕 크기만큼 넣어줌
        queue.append(list_a.pop(0))

    while len(queue) > 1:
        a = queue.pop(0)                #피자를 확인
        a[1] //= 2                      #확인한 피자의 치즈가 반으로 줄어듦
        if a[1] > 0:                    #반으로 줄어든 치즈가 0보다 크다면 append를 통해 다시 화덕으로
            queue.append(a)
        elif a[1] == 0 and list_a:      #치즈가 0이고 대기하는 피자가 남아있다면 대기하는 피자를 화덕으로 append
            queue.append(list_a.pop(0))

    print('#{} {}'.format(tc, queue[0][0]))

