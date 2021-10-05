import sys
sys.stdin = open('input.txt')

# tc값 받고
T = int(input())
for tc in range(1, T+1):
    num, change = input().split()  # 숫자판의 정보, 교환횟수

    # change를 int형으로 변환
    change = int(change)
    # N은 num의 길이
    N = len(num)
    now = set([num])
    # num 를 집합 set으로 . set은 key가 없는 dictionary
    # 중복제거
    # set('7111117) - > {'711117'}
    nxt = set()

    # 코드 참고
    for _ in range(change):  # 교환 횟수 동안
        while now:  # set 을 조건문으로 만들면?
            s = now.pop()  # set 안의 요소를 꺼냄.
            s = list(s)  # 그걸 list 로 만듬,

            # N = 51423 이라고 가정.
            for i in range(N):  # i로 N까지
                for j in range(i + 1, N):  # i+1부터 N까지, # i == N 일 경우 그냥 통과인가?
                    s[i], s[j] = s[j], s[i]  # 앞뒤 순서를 바꿈.
                    nxt.add(''.join(s))  # ['3','4'] -> "34" 형태로
                    s[i], s[j] = s[j], s[i]
        now, nxt = nxt, now

    print('#{} {}'.format(tc, max(map(int, now))))

# 입력받은 숫자판을 change만큼 바꿀 수 있는 모든 경우의 수를 생성 해내고
# 그 중 최대값을 뽑아내는 원리다.



