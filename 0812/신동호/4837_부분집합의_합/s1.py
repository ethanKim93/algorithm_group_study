import sys
sys.stdin = open('sample_input.txt')
T = int(input())
numbers = [n+1 for n in range(12)]
for tc in range(1,T+1):
    N, K = list(map(int, input().split()))
    result = 0
    #비트 연산자로 모든 부분 집합 구하기
    for i in range(1, 1<<len(numbers)):
        cnt = 0
        sub = 0
        for j in range(len(numbers)):
            if i & (1<<j):
                sub += numbers[j] # numbers의 숫자 더하기
                cnt += 1 # 원소의 개수 증가
        if sub == K and cnt == N: #원소의 개수 일치하고 합도 일치할 때
            result += 1
    print('#{} {}'.format(tc,result))
