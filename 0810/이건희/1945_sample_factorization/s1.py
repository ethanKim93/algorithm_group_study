import sys
sys.stdin = open("input.txt")

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    prime_factor = [2, 3, 5, 7, 11] # 소인수 리스트
    ans = [0, 0, 0, 0, 0] # 나눠 준 횟수 담는
    for i in range(5):
				# 나눌 수 있을 때까지 나눠주고, 나눌 때마다 cnt ++1, n 최신화
        while n%prime_factor[i] == 0:
            ans[i] += 1
            n = n//prime_factor[i]

		# ans의 요소들 str형태로 바꿔준 뒤, join으로 list형식 벗어나기
    print("#{} {}".format(tc, " ".join(map(str,ans))))
