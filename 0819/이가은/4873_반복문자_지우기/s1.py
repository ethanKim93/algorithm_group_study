import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for test in range(T):

    con_str = str(input())
    result = []             # 확인할 빈 list

    for i in range(len(con_str)):
        if not result:                  # result가 비어있으면 append
            result.append(con_str[i])
        elif con_str[i] != result[-1]:  # result의 마지막 글자와 다르면 append
            result.append(con_str[i])
        else:                           # result의 마지막에 동일 글자 있으면 제거
            result.pop(-1)

    cnt = len(result)
    print('#{} {}'.format(test+1, cnt))