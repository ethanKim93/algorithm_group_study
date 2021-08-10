import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    nums = int(input())
    temp_list = input()
    counter = [0] * 10
    #크기가 10인 빈 배열을 생성한다.
    max_info = [0, 0]
    #max_info = [해당하는 숫자, 해당하는 숫자의 갯수]의 형태로 저장한다.
    for i in range(nums):
        temp_num = int(temp_list[i])
        #주어진 문자열 내 i번째 숫자를 temp_num에 저장한다.
        counter[temp_num] += 1
        flag = False
        if max_info[1] < counter[temp_num]:
            flag = True
        if max_info[1] == counter[temp_num]:
            # 동일한 횟수로 등장한 경우, 숫자가 더 큰 경우를 선택한다.
            if max_info[0] < temp_num:
                flag = True
        if flag:
            max_info[0] = temp_num
            max_info[1] = counter[temp_num]
    print("#{} {} {}".format(tc, max_info[0], max_info[1]))