import sys
sys.stdin = open('sample_input.txt')

# 딕셔너리로 key:16진수에 해당하는 2진수 값을 저장
hexa = {}
for i,h in enumerate('0123456789ABCDEF'):
    bins = ''
    # 비트연산으로 2진수의 4자리 중 앞 자리 수부터 비트 연산으로
    # 해당 비트가 있으면 1, 없으면 0을 string concatenate 
    for j in range(3, -1, -1):
        bins += '1' if i & (1<<j) else '0'
    hexa[h] = bins

for tc in range(1, int(input()) + 1):
    _, strs = input().split()
    ans = ''
    for s in strs:
        ans += hexa[s]
    print('#{} {}'.format(tc, ans))