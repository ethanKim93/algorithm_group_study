'''
교수님 추천 memoization 활용 코드
30, 50, 70 을 다 받은 다음에 가장 큰 70을 기준으로 계산을 해서
배열에 저장한 다음 한번에 출력하는 코드
'''
import sys
sys.stdin = open("sample_input.txt")

T = int(input())
N = []
for _ in range(1, T+1):
    N.append(int(input())//10)

maxN = 0
for n in N:
    if maxN < n:
        maxN = n

box = [1]
for i in range(1, maxN+1):
    if i%2:             # 홀수인 경우
        box.append(2*box[i-1] -1)
    else:               # 짝수인 경우
        box.append(2*box[i-1] +1)

for tc, n in enumerate(N, start=1):
    print('#{} {}'.format(tc, box[n]))



