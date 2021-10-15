import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    cnt = 0
    tmp1 = 0
    tmp2 = 0
    print(N, M)
    while N != M:
        print(N)
        print(M)
        if N * 2 <= M:
            N = N*2
            cnt += 1
            # print(cnt)
            print("1번")
        elif N * 2 > M:
            N = N*2
            cnt += 1
            print("2번")
            if abs(N - M) > abs(N/2 - M):
                N = N/2
                cnt -= 1
                cnt += abs(N - M)
                N += abs(N - M)
                print("2-1번")
            elif abs(N - M) < abs(N/2 - M) < 10:
                # print(N)
                # print(M)
                cnt += abs(N - M)
                N -= abs(N - M)
                print("2-2번")
            elif abs(N - M) < abs(N / 2 - M) > 10:
                cnt += abs(N - M)//10
                cnt += abs(N - M)%10
                N += abs(N - M)
                print("2-3번")

    print("#{} {}".format(tc + 1, int(cnt)))

