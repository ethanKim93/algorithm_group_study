import sys
sys.stdin = open('sample_input.txt')
def melting():
    while len(q) != 1:                          # 화덕에 남은 피자가 하나일 때 종료
        if pizza and len(q) < N:                # 아직 굽지 않은 피자가 있고 화덕이 비어있을 때
            q.append(pizza.pop(0))              # 화덕에 피자 넣기
        else:
            while q[0][1]:                      # 화덕의 입구에 있는 피자의 치즈가 0일 때 까지
                temp = q.pop(0)
                temp[1] //= 2                   # 치즈 양을 반으로 줄이고
                if not temp[1]:                 # 치즈가 0이 된다면 피자 꺼내기
                    break
                q.append(temp)                  # 0이 아니라면 가장 뒷순서로 이동

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())            # 화덕의 크기, 피자 개수
    cheese = list(map(int, input().split()))    # 피자에 뿌려진 치즈의 양
    pizza = []                                  # 피자
    q = []                                      # 화덕
    for i in range(M):                          # 피자 번호와 치즈 양 초기화
        pizza.append([i+1, cheese[i]])
    for _ in range(N):
        q.append(pizza.pop(0))                  # 화덕에 넣을수 있는 만큼 피자를 넣고
    melting()                                   # 화덕 돌리기
    print(q[0][0])                              # 남은 피자번호 출력