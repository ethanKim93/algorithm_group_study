import sys
sys.stdin = open("input.txt")

result_1 = []
result_2 = []
result_3 = []
def pre_order_VLR(n):   # 전위 순회
    if n:
        result_1.append(n)
        pre_order_VLR(left[n])
        pre_order_VLR(right[n])
        return result_1

def pre_order_LVR(n):   # 중위 순회
    if n:
        pre_order_LVR(left[n])
        result_2.append(n)
        pre_order_LVR(right[n])
        return result_2

def pre_order_LRV(n):   # 후위 순회
    if n:
        pre_order_LRV(left[n])
        pre_order_LRV(right[n])
        result_3.append(n)
        return result_3


N = int(input())
nums = list(map(int, input().split()))
left = [0] * (N+1)
right = [0] * (N+1)
for i in range(len(nums)//2):
    n1,n2 = nums[i*2], nums[i*2+1]
    if left[n1]:                 # 만약 왼쪽 자식이 더 작아야한다는 조건이 있다면 그에 대한 조건문 필요/ 이미 들어가 있는 수보다 새로 들어갈 수가 더 작다면 위치 바꾸는 정도
        right[n1] = n2
    else:
        left[n1] = n2

print('전위순회 : {}, 중위순회 : {}, 후위 순회 : {}'.format(pre_order_VLR(1), pre_order_LVR(1), pre_order_LRV(1)))



# # 전위 순회[라이브 코드]
# def pre_order(n):
#     if n:               # 유효한 정점이라면
#         print(n)
#         pre_order(left[n])
#         pre_order(right[n])
#
#
# V = int(input())
# edge = list(map(int,input().split()))
# E = V-1
# left = [0]*(V+1)
# right = [0]*(V+1)
# for i in range(E):
#     p, c = edge[i*2], edge[i*2+1]
#     if left[p] == 0 :       #왼쪽 자식이 없다면
#         left[p] = c
#     else:                   # 있다면 오른쪽에 저장
#         right[p] = c
# pre_order(1)