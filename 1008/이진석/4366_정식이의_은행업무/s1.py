import sys
sys.stdin = open('sample_input.txt', 'r')


def check(b_line,t_line):
    num = int(b_line, 2)            # 입력받은 2진수 > 10진수
    bin_arr = []                    # 가능한 2진수 종류를 저장할 배열

    for i in range(len(b_line)):    # 각 비트마다 토글해서 배열에 저장(한자리씩만 토글)
        bin_arr.append(num ^ (1 << i))

    for j in range(len(t_line)):
        temp1 = t_line[:]       # 3진수 후보 1 > 각 자리마다 두가지의 경우의 수가 있음
        temp2 = t_line[:]       # 3진수 후보 2
        if int(t_line[j]) % 3 == 0:
            temp1[j] = '1'
            temp2[j] = '2'
        elif int(t_line[j]) % 3 == 1:
            temp1[j] = '0'
            temp2[j] = '2'
        else:
            temp1[j] = '0'
            temp2[j] = '1'
        temp1 = int(''.join(temp1), 3)  # 3진수 후보를 10진수로 변환
        temp2 = int(''.join(temp2), 3)
        if temp1 in bin_arr:        # 2진수 후보와 3진수 후보가 일치한다면 정답으로 반환
            return temp1
        elif temp2 in bin_arr:
            return temp2

for tc in range(1, int(input()) + 1):
    bin_line = input()
    tri_line = list(input())
    answer = check(bin_line,tri_line)
    print('#{} {}'.format(tc, answer))