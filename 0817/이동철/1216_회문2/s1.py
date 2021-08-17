import sys
sys.stdin = open('input.txt')


def check(a):
    long = len(a)
    for idx in range(long // 2):
        if a[idx] != a[long - idx - 1]:
            return False
    return True


T = 10
for tc in range(1, T+1):
    N = int(input())
    arr_row = [list(input()) for _ in range(100)]
    arr_col = []
    for i in range(100):
        temp_str = ''
        for k in range(100):
            temp_str += arr_row[k][i]
        arr_col.append(temp_str)

#100부터 계산하여 작아지는 단계로 검사하였으며
#회문이 하나라도 나오는 순간 모든 반복문을 중지하고
#찾은 회문의 길이를 출력했다.

    result = 0
    for t_len in range(100, 0, -1):
        if result >= t_len:
            break
        for i in range(100):
            if result == t_len:
                break
            for j in range(100 - t_len + 1):
                if check(arr_col[i][j:j+t_len]) or check(arr_row[i][j:j+t_len]):
                    result = t_len
                    break

    print('#{} {}'.format(tc, result))