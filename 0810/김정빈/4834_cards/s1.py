import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int,list(input())))
    aiL = [0 for a in range(10)] # 숫자 카운팅 할 리스트
    for a in ai: # 숫자 순회하며 카운팅
        aiL[a] += 1
        p = 0 #장수
        n = aiL[0] #숫자
        for i in range(1, 10):
            if aiL[i] >= n: # 숫자값이 위치값보다 크거나같으면
                n = aiL[i] # 숫자값은 리스트의 인덱스위치
                p = i #장수는 카운팅리스트의 개수

    print('#{} {} {}'.format(tc, p, n))