import sys
sys.stdin = open('sample_input.txt')

T = int(input())

# 정렬 함수
def sorting(lst):
    for i in range(len(lst) - 1, -1, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    containers = sorting(list(map(int, input().split())))
    trucks = sorting(list(map(int, input().split())))
    result = 0


    for t in range(len(trucks) - 1, -1, -1):            # 큰 값 부터 순회
        truck = trucks[t]
        for c in range(len(containers) - 1, -1, -1):    # 큰 값 부터 순회
            container = containers[c]
            if container <= truck:                      # truck 에 담을 수 있으면 result 에  추가
                result += container
                containers[c] = 101                     # limit 이 100이므로 그 이상 할당(다시 연산되지 않도록)
                break

    print("#{} {}".format(tc, result))