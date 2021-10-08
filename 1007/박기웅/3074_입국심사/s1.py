import sys
sys.stdin = open('sample_input.txt')

def binary_search(l, r):
    global min_time
    while l <= r:
        mid = (l+r)//2
        man = sum([mid//t for t in times])
        if man >= M:        # 처리한 사람이 M 이상이라면 범위를 작은쪽 반으로
            min_time = min(min_time, mid)
            r = mid-1       # l, r 크로스하는 경우를 만들기 위해 -1, +1 (안하면 무한루프 지옥..)
        else:               # 처리한 사람이 더 적은 경우
            l = mid+1       
    return
# N : 입국심사대 수, M : 사람 수
# times: 각 입국심사대에서 걸리는 시간
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    times = []
    for _ in range(N):
        times.append(int(input()))
        
    # M명을 처리하는데 가장 오래 걸리는 시간    
    slow = min_time = max(times)*M
    binary_search(0, slow)
    print('#{} {}'.format(tc, min_time))
   
    # 시간 초과.. 최소값의 공배수로 반복을 도는게 비효율적
    # fast = min(times)
    # cnt = man = 0 
    # while man < M:
    #     cnt += 1
    #     man = sum([(fast*cnt)//t for t in times])
    # print('#{} {}'.format(tc, fast*cnt))
