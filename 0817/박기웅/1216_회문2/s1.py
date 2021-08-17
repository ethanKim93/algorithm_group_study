import sys
sys.stdin = open("input.txt")

def is_pal(arr): #1d 리스트에 대해 회문을 판별하는 함수
    n = len(arr)
    for i in range(n//2):
        if arr[i] != arr[n-i-1]:
            return 0
    else:
        return 1

for _ in range(1, 11):
    tc = input()
    arr2d = [input() for _ in range(100)]
    arr2d_tr = [x for x in zip(*arr2d)] # 세로 행 회문 판별위한 transpose
    max_pal = 0 #회문의 최대 길이 초기화
    for i in range(100):
        cnt = 100 #임시로 회문 길이 100으로 초기화
        while(cnt > 0): # 최대 100부터 1까지 검사
            for j in range(101-cnt):
                if is_pal(arr2d[i][j:j+cnt]) or is_pal(arr2d_tr[i][j:j+cnt]):
                    break # 가로, 세로 회문 찾은경우 나감
            else:
                cnt -= 1 #없으면 회문 길이 줄여서 찾는거 반복
                continue

            if cnt: #for 문을 break 로 나간 경우 while 문도 나감
                break
        if max_pal < cnt:
            max_pal = cnt

    print('#{} {}'.format(tc, max_pal))