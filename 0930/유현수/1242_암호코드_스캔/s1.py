import sys
sys.stdin = open('sample_input.txt')

decode = {'112': 0, '122': 1, '221': 2,'114': 3, '231': 4,'132': 5, '411': 6, '213': 7, '312': 8, '211': 9}


# 16진수 문자열을 넣으면 '1로 끝나는' 2진수 문자열과 문자열의 길이를 리턴
def hex_to_bin(hex_str):
    n = len(hex_str)
    bin_str = ''
    for j in range(n):
        tmp = int(hex_str[j], 16)
        for k in range(4):
            if tmp & (8 >> k):
                bin_str += '1'
            else:
                bin_str += '0'
    bin_str = bin_str.rstrip('0')
    return bin_str, len(bin_str)


# 2진수 문자열을 넣으면 가장 끝에 있는 1의 인덱스를 리턴
def get_start_idx(b_str):
    n = len(b_str)
    for i in range(n-1, -1, -1):
        if b_str[i]:
            return i


# 유효한 바코드인지 확인
def verify_barcode(brcd):
    if ((brcd[7]+brcd[5]+brcd[3]+brcd[1])*3 +brcd[0]+brcd[2]+brcd[4]+brcd[6]) % 10:
        return False
    return True


T = int(input())
for tc in range(1, T+1):
    # 세로 크기 N, 가로 크기 M
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    ans = 0
    barcode = []
    visited = []

    # 행 순회
    for i in range(N):
        # 이진수 문자열로 변환, 이진수 문자열 길이 확인
        b_str, n = hex_to_bin(arr[i])
        # 이진 문자열에 1이 있으면 바코드 탐색 시작
        if '1' in b_str:
            # 바코드는 뒤에서부터 1-0-1-0 순으로 나옴 => 1-0-1-0 패턴에서 각 개수를 세면 바코드의 두께 확인 가능
            # 각 암호코드는 뒤 3자리가 다르므로 뒤 3자리만 알면 해석 가능
            # flag1은 처음 나오는 1의 개수, flag2는 다음 나오는 0의 개수, flag3는 그다음 나오는 1의 개수
            flag1 = flag2 = flag3 = 0
            # 이진 문자열을 뒤에서부터 탐색
            for j in range(n-1, -1, -1):
                if flag2 == flag3 == 0 and b_str[j] == '1':     # 처음 나오는 1의 개수
                    flag1 += 1
                elif flag1 and flag3 == 0 and b_str[j] == '0':  # 그다음 나오는 0의 개수
                    flag2 += 1
                elif flag1 and flag2 and b_str[j] == '1':       # 그다음 나오는 1의 개수
                    flag3 += 1
                elif flag3 and b_str[j] == '0':                 # 0이 나오면
                    thickness = min(flag1, flag2, flag3)        # 셋 중 가장 작은 수가 바코드의 두께
                    # 각각 두께로 나누어 바코드에 저장
                    barcode.append(decode[str(flag1//thickness)+str(flag2//thickness)+str(flag3//thickness)])
                    # 플래그 초기화
                    flag1 = flag2 = flag3 = 0
                    # 바코드 길이 확인
                    if len(barcode) == 8:
                        # 이전에 봤던 바코드인지 확인
                        if barcode not in visited:
                            # 유효한 바코드인지 확인
                            if verify_barcode(barcode):
                                # 유효하다면 정답에 더한다
                                ans += sum(barcode)
                            # 방문 처리
                            visited.append(barcode)
                        # 바코드 초기화
                        barcode = []
    print('#{} {}'.format(tc, ans))
