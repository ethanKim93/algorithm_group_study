import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N, string = input().split()
    N = int(N)
    string = list(string)
    i = 0
    while i < len(string)-1:
        if string[i] == string[i+1]:   # 번호 쌍이 같다면 문자열에서 제거
            string.pop(i)
            string.pop(i)
            i -= 1                     # 한 쌍이 제거 된 후 새로운 번호 쌍이 생길수 있으므로 다시 전의 인덱스를 확인
        else:
            i += 1
    print('#{} '.format(tc),end=' ')
    print(*string,sep='')