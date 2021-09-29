import sys
sys.stdin = open('input.txt')

def serch(n, m):          # 뒤에서 부터 시작해서 첫번째 '1' 을 찾는함수
    for i in range(n):
        for j in range(-1, -m, -1):
            if code[i][j] == '1':
                j = m + j - 56     # 첫번째 좌표부터 시작하기 위해 -56을 빼서 첫번째 시작점을 찾음
                now.append(i)
                now.append(j)
                return now


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    code = [input() for _ in range(N)]
    now = [] # 뒤에서 부터 찾은 첫번째 '1'의 인덱스
    password = [] # 2진코드를 담을 리스트
    ans_list = [] # 정답을 계산할 숫자를 담을 코드


    serch(N,M) # 뒤에서 부터 1을 찾는 함수 호출
    #print(now)
    for j in range(now[1]+1, 56+now[1]+1): # 2진코드의 암호가 시작하는
        password.append(code[now[0]][j])

    #print(password)
    code_list = [['0','0','0','1','1','0','1'],['0','0','1','1','0','0','1'],
     ['0','0','1','0','0','1','1'],['0','1','1','1','1','0','1'],
     ['0','1','0','0','0','1','1'],['0','1','1','0','0','0','1'],
     ['0','1','0','1','1','1','1'],['0','1','1','1','0','1','1'],
     ['0','1','1','0','1','1','1'],['0','0','0','1','0','1','1']]
    # 0 번부터 대응되는 코드 리스트

    k = 0  # 반복문 제어를 위한 변수
    p = 0 # 인덱스 카운트를 위한 변수
    while k < 57:
        password_div = password[0+k:7+k] # 앞에서 부터 password를 7자리씩 끊음
        for i in code_list:
            if i == password_div:  # 위의 코드 리스트와 같으면
                ans_list.append(p)  # 그때의 인덱스 번호를 리스트에 담음
                p = 0
                break
            p += 1
        k += 7

    #print(ans_list)
    vf = 0
    ans = 0
    for y in range(len(ans_list)):
        if y % 2 == 0:    # 홀수 번째 번호를 찾는데 인덱스상은 짝수임
            vf += ans_list[y] * 3 # 홀수 번째 번호일 때 3을 곱하고
        else:
            vf += ans_list[y]     # 짝수 번째 번호일때는 그냥 더해서 검증숫자를 만듬
        ans += ans_list[y]        # 정상적인 암호 코드 일 때 출력을 위한 상품번호 합
    if vf % 10 != 0:        # 검증숫자가 10의 배수가 아니면
        ans = 0            # =0
# 검증을 통해
    print('#{} {}'.format(tc,ans))