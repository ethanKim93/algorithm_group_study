def biggestPalindrome(text_list):

    # 행에서 가장 큰 길이 찾기
    row_max_len = 0
    for length in range(100, 0, -1):  # 큰 길이부터 줄여나가면서 확인하고 찾으면 바로 break
        if row_max_len:
            break
        for i in range(100):
            if row_max_len:
                break
            for j in range(100-length+1):
                for k in range(length // 2):
                    if text_list[i][j+k] != text_list[i][j+length-1-k]:
                        break
                else:
                    row_max_len = length

    # 열에서 가장 큰 길이 찾기
    col_max_len = 0
    for length in range(100, 0, -1):
        if col_max_len:
            break
        for i in range(100):
            if col_max_len:
                break
            for j in range(100 - length + 1):
                for k in range(length // 2):
                    if text_list[j+k][i] != text_list[j+length-1-k][i]:
                        break
                else:
                    col_max_len = length

    # 비교
    if row_max_len > col_max_len:
        return row_max_len
    else:
        return col_max_len


for _ in range(10):
    tc = int(input())
    text_list = []
    for _ in range(100):
        text_list.append(input())
    print('#{} {}'.format(tc, biggestPalindrome(text_list)))

    # 백준에 넣으면 시간초과 날듯..