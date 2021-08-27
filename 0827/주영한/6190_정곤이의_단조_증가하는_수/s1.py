import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    num_lists = list(map(int, input().split()))
    max_num = -1

    # 두 개의 곱에 대한 모든 경우를 확인한다.
    for i in range(N):
        for j in range(i + 1, N):

            # 두 요소의 곱을 temp에, 이에 대해 단조 증가 여부를 확인하기 위하여
            # str으로 형변환한 결과를 str_temp로 담아준다.
            temp = num_lists[i] * num_lists[j]
            str_temp = str(temp)

            # 크기가 1보다 클 경우, 줄어드는 부분이 있으면 이를 무시하고,
            # 단조 증가의 경우, max_num과 비교한다.
            if len(str_temp) > 1:
                growing_flag = True
                for idx in range(len(str_temp) - 1):
                    if str_temp[idx] > str_temp[idx + 1]:
                        growing_flag = False
                        break
                if growing_flag:
                    if int(temp) > max_num:
                        max_num = temp

            # 크기가 1일 경우는 무조건 단조 증가로 판단한다.
            else:
                if int(temp) > max_num:
                    max_num = temp
    print("#{} {}".format(tc, max_num))