import sys
sys.stdin = open('input.txt')

for tc in range(1,int(input())+1):
    data, K = input().split() # 숫자판의 정보, 교환횟수
    K = int(K)
    N = len(data)
    now = set([data])
    nxt = set()        # 중복제거를 위한 set
    for _ in range(K):
        while now:
            s = now.pop()
            s = list(s)
            for i in range(N):
                for j in range(i+1,N):  # 이중 포문을 통해 교환 횟수 만큼 탐색 실행
                    s[i],s[j] = s[j],s[i]
                    nxt.add(''.join(s))
                    s[i], s[j] = s[j], s[i]
        now,nxt = nxt,now

    print('#{} {}'.format(tc,max(map(int,now))))  # 탐색한 값중 최댓값을 출력


    #
    # T = int(input())
    # for tc in range(1, T+1):
    #     N, M = map(str, input().split())
    #     change = int(M)
    #     numbers = list(map(int, N))

    # 1. 맨 앞자리를 최댓값과 교환 (중복된 최댓값 존재시 뒷자리의 최댓값과 교환)
    # max_n = numbers[0]
    # for i in range(len(numbers)):
    #     if numbers[i] >= max_n:
    #         idx = i
    # numbers[0], numbers[idx] = numbers[idx], numbers[0]
    #
    # change -= 1
    # 최대 변경 횟수를 만족하면 끝냄
    # if change == 0:
    #     print("끝")
