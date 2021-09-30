import sys
sys.stdin = open('sample_input.txt', 'r')

# 암호규칙
decode = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

# 암호해독
def decoding(data, scale):
    data = data[::scale]                # 암호 패턴 56칸으로만들기(중복제거)
    i = 0
    code = ''                           # 반환할 해독코드 
    while i < 56:
        temp = data[i:i+7]              # 7칸씩 비교
        if temp in decode.keys():       # 존재하는 key일때(decode)
            code += str(decode[temp])   # 암호변환
        else:
            return 0
        i += 7
    return code

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().strip().split())
    lines = set()       # 입력받은 값을 정리해 저장할 set(중복제거)
    codes = set()       # 해독한 코드를 저장할 set(중복제거)
    answer = 0          # 정답저장할 변수

    for _ in range(N):
        temp = input().strip().strip('0')               # 양쪽에 붙어있는 0 제거
        if not len(temp): continue                      # 0으로만 이뤄진 행은 저장하지않는다
        temp = bin(int(temp, 16))[2:].rstrip('0')       # 2진수 변환 후 오른쪽 0 제거(오른쪽 끝은 항상 1)
        lines.add(temp)                                 # 정리된 암호코드를 저장
    for line in lines:
        scale = 1                           # 검사할 스케일(크기)
        max_scale = len(line)//56 +1        # 스케일의 최대크기
        while line and scale <= max_scale:
            line = line.zfill(56 * scale)   # 56의 배수가 아닐때 56의 배수로 만들기(왼쪽을 0으로 채우기)
            sub = line[(-56) * scale:]      # 암호 후보
            ret = decoding(sub, scale)      # 암호인지 검증
            if ret:                         # 암호 맞을때
                codes.add(ret)           # 생성된 코드를 return 받아온다.
                line = line[:-56 * scale].rstrip('0')
                scale = 1
            else:                           # 암호 아닐때
                scale += 1
                
    for code in codes:
        odd = int(code[0]) + int(code[2]) + int(code[4]) + int(code[6])     # 홀수코드
        even = int(code[1]) + int(code[3]) + int(code[5]) + int(code[7])    # 짝수코드
        if (odd*3+even) % 10:   # 암호검증 실패
            continue
        else:   # 암호검증 성공
            answer += sum(list(map(int, code)))

    print('#{} {}'.format(tc, answer))
