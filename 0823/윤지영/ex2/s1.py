arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
selected = [0] * N      # 사용여부 확인 배열

def powerset(i):
    if i == N :
        total = 0
        sub = []
        for j, sel in enumerate(selected):
            if sel:
                total += arr[j]
                sub.append(arr[j])
        if total > 10:              # 현재까지 합이 타겟인 10보다 커지면 유망없으므로 return
            return
        elif total == 10:           # 합이 10이 된다면, 해당 부분집합 출력
            print(sub)
        return                  # i를 9을 호출했을 때(powerset(i+1))로 돌아감
    selected[i] = 1             # [1,0,0,0,0,0,0,0,0,0] > [1,1,0,0,0,0,0,0,0,0] > ... > [1,1,1,1,1,1,1,1,1,1] > if 분기
    powerset(i+1)           # return 되면 돌아오는 곳
    selected[i] = 0         # 돌아오면 해당 값 0 으로 변경 [1,1,1,1,1,1,1,1,1,0]
    powerset(i+1)           # powerset(10) -> if 분기타서 출력하고, 다시 return 되면 더 이상 호출할 게 없으니 다시 return 되서 위로 올라감 -> i 하나 줄어듦
powerset(0)





# #비트 연산자 사용
# subset_sum = []
# for i in range(1,1 << N):
#     sub = []
#     sub_sum = 0
#     for j in range(N):
#         if i & (1 << j):
#             sub.append(arr[j])
#             sub_sum += arr[j]
#     if sub_sum == 10:
#         subset_sum.append(sub)
#
# print(subset_sum)

