import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    people = list(map(int, input().split()))
    people.sort()  # 오름차순 정렬
    sec = cnt = i = 0
    pro = 'Possible'
    if M > people[0]:
        print('#{} Impossible'.format(tc))
    else:
        while i < N:
            if sec >= people[i]:
                cnt -= 1
                i += 1
            else:
                sec += M  # M초당
                cnt += K  # K개 생성
            if cnt <= 0:
                pro = 'Impossible'
                break

        print('#{} {}'.format(tc, pro))