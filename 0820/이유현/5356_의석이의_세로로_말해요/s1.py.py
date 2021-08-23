import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = [list(input()) for _ in range(5)]

    for lst in arr:
        if len(lst) < 15:
            lst += ['/'] * (15-len(lst))
    
    print('#{}'.format(tc), end=' ')
    for j in range(15):
        word = []
        for i in range(5):
            if arr[i][j] == '/':
                continue
            else:
                print(arr[i][j], end='')
    print()
        

'''
(1) 허락받고하자
if 문을 돌리면서 읽을 수 있는지 확인, 읽을 수 있으면 읽고 넘어가자
(2) 용서를 구하자
try ~ except pass
'''