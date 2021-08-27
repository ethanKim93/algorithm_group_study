p = 1                                                           # 처음 줄 설 사람 번호
q = []                                                          # queue 생성
N = 20                                                          # 초기 마이쮸 개수
my = [0] * (N+1)
cnt = [0] * (N+1)
m = 0                                                           # 나눠준 개수
while m<N:

    q.append(p)
    cnt[p] += 1
    print()
    print('엔터를 입력해주세요')
    input()                                                     # 엔터를 치면
    print('큐에 있는 사람 수 : {}, {}'.format(len(q), q))

    v = q.pop(0)                                                # 받을 사람 v
    m += cnt[v]                                                 # 줄선 횟수 만큼 배분
    print('받을 사람 : {} , 받을 개수 : {}'.format(v, cnt[v]))
    my[v] += cnt[v]                                             # 받은 개수

    print('나눠준 개수 : {}'.format(min(m, N)))                 # 실제 가능한 배분 개수 선택

    q.append(v)                                                 # 받은 사람이 다시 줄서면
    cnt[v] += 1
    p += 1                                                      # 따라 들어갈 사람 번호 1증가
    for i in range(1, p):
        print('{} : {}, '.format(i, my[i]), end=' ')
    print()
print('마지막 받은 사람 : {}'.format(v))
