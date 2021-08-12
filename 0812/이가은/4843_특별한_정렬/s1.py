import sys
sys.stdin = open('sample_input.txt')

Test_case = int(input())
for test in range(Test_case):
    num_cnt = int(input())
    num_arr = map(int, input().split())
    arr = sorted(num_arr) # 정렬 된 arr

    special_arr= "" # 특별한 arr
    for i in range(10): # 10개의 코드를 뽑을 겁니다
        if i%2==0:
            special_arr += ' ' + str(arr[num_cnt-1-(i//2)])
        else:
            special_arr += ' ' + str(arr[(i-1)//2])

    print('#{}{}'.format(test+1, special_arr))
