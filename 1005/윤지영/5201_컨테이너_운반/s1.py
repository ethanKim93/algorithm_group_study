import sys
sys.stdin = open('input.txt')

def add():
    # 최종무게 ans를 0으로 초기화
    ans = 0
    # 트럭 중량에 대해 반복문 순회
    for max_weight in t:
        # 컨테이너 무게에 대해 반복을 돌면서
        for weight in w:
            # 컨테이너 무게가 현재 트럭의 중량보다 작거나 같으면 최종 무게 ans에 추가
            if weight <= max_weight:
                ans += weight
                # 이번 트럭에 컨테이너를 실은 것이므로 해당 컨테이너 무게는 배열에서 삭제
                w.remove(weight)
                # 트럭 1대당 1개의 컨테이너만 실을 수 있으므로 실을 컨테이너 찾았으면 break
                break
    return ans


T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())     # 컨테이너 , 트럭 수
    # 중량이 큰 트럭에 무거운 무게를 실어야 효율적이므로 트럭 중량과 컨테이너 무게 배열 모두 내림차순 정렬
    w = sorted(list(map(int,input().split())),reverse=True)  # 컨테이너 무게 내림차순정렬
    t = sorted(list(map(int,input().split())),reverse=True)  # 트럭 중량 내림차순 정렬
    print('#{} {}'.format(tc,add()))




# 트럭이 하나만 옮길 수 있는 경우가 아닐 때
# def add(n,weight):
#     ans = 0
#     final = power_set[0]
#     for i in range(1,1<<n):
#         for j in range(n):
#             if i & (1<<j):
#                 if sum(power_set[i]) <= weight:
#                     power_set[i].append(w[j])
#         we = sum(power_set[i])
#         if ans < we:
#             ans = we
#             final = power_set[i]
#     for p in final:
#         w.remove(p)
#     return ans
#
#
# T = int(input())
# for tc in range(1,T+1):
#     N, M = map(int,input().split())     # 컨테이너 , 트럭 수
#     w = list(map(int,input().split()))  # 컨테이너 무게
#     t = list(map(int,input().split()))  # 트럭 중량
#     sorted(t,reverse=True)  # 트럭 중량 내림차 순 정렬
#     power_set = [[] for _ in range(1<<len(w))]
#     result = 0
#     for max_weight in t:
#         result += add(len(w),max_weight)
#     print(result)

