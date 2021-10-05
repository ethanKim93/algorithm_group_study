import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input())+1):
    N, T = input().split()

    # 중복되는 케이스를 제거하기 위해서 set로 정의
    # set(N) 으로 하면 string들이 하나씩 나눠서 원소로 들어가짐
    Ncase = set([N])
    
    for _ in range(int(T)):
        tmp = set()
        # 모든 케이스들을 돌때까지
        for n in map(list, Ncase): # 케이스를 하나씩 빼서 교환 진행   
            for i in range(len(n)):
                for j in range(i+1,len(n)):
                    # if n[i] <= n[j]: 이 조건은 tmp 에 add 가 안되서 다른 테케에서 런타임 에러 발생
                    n[i], n[j] = n[j], n[i]
                    tmp.add(''.join(n))
                    n[i], n[j] = n[j], n[i]
        # 교환이 한번 일어나면 가능한 경우들을 Ncase에 업데이트
        Ncase = tmp
    
    ans = sorted(Ncase)[-1]
    print('#{} {}'.format(tc, ans))