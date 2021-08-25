import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    T = input()
    num_list = list(map(int, input().split()))

    while num_list[-1]:  # 마지막 숫자가 0일 때까지 반복
        for i in range(1, 6):  # 5번 돌면 1싸이클
            target = num_list.pop(0)
            num_list.append(target-i)  # 첫번째 수를 i만큼 빼주고 끝에 삽입
            if num_list[-1] <= 0:  # 마지막 수가 음수면 0으로 바꾼다
                num_list[-1] = 0
                break
    print('#{} {}'.format(tc, ' '.join(map(str, num_list))))