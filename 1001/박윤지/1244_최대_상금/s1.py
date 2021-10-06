# 완전탐색으로 모든 경우 따져도 된다고 함...
# -> 최대 자릿수는 6자리, 최대 교환 횟수는 10번으로 숫자가 작아서

# 백트래킹 없이 하면 런타임오류 남(시간초과?)
# -> 같은 횟수를 교환했을 때 숫자가 같으면 하나만 계속 교환해도 되므로 나머지를 걸러야함
# => 만들어진 숫자들을 list 아닌 set에 저장, set(교환횟수)

import sys
sys.stdin = open('input.txt', 'r')

def exchange(arr, cnt):
    global ans
    reward = int(''.join(arr))
    if reward in visited[cnt]:
        return
    visited[cnt].add(reward)

    if cnt == times:
        ans = max(ans, reward)  # ans와 지금 경우에서 구한 상금중 큰걸로 ans를 다시 정의
        return

    for i in range(0, len(arr)-1):
        for j in range(i+1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            exchange(arr, cnt+1)
            arr[i], arr[j] = arr[j], arr[i]


T = int(input())

for tc in range(1, T+1):
    temp = list(input().split())
    num = list(temp[0])
    times = int(temp[1])
    visited = [set() for _ in range(times+1)]  # 0부터 교환횟수까지
    ans = 0
    exchange(num, 0)
    print('#{} {}'.format(tc, ans))