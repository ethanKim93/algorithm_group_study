import sys
sys.stdin = open('input.txt')

def add():
    ans = 0
    for max_weight in t:
        for weight in w:
            if weight <= max_weight:
                ans += weight
                w.remove(weight)
                break
    return ans


T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())     # 컨테이너 , 트럭 수
    w = sorted(list(map(int,input().split())),reverse=True)  # 컨테이너 무게 내림차순정렬
    t = sorted(list(map(int,input().split())),reverse=True)  # 트럭 중량 내림차순 정렬
    ans = add()
    print('#{} {}'.format(tc,ans))




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

