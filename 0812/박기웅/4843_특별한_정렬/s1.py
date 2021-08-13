import sys
sys.stdin = open("sample_input.txt")

for tc in range(1, int(input())+1):
    N = int(input())
    a = list(map(int, input().split()))
    cnt = [0]*101 # a 원소의 값이 1~100이므로 101짜리 count 배열 생성
    for i in range(N):
        cnt[a[i]] += 1 # cnt 배열 초기화

    amax, amin = 100, 1 # 처음 찾는 범위를 지정해주는 amax, amin 값 지정
    asort = [] # 정렬된 리스트
    while ( len(asort) < 10 ): # 10개가 될시 반복문 탈출
        # cnt 배열에서 가장 큰 값을 찾는 반복문
        for i in range(amax, amin-1, -1):
            if cnt[i]: # 0 이 아닐시 max 값을 지정 후 정렬 리스트에 추가 + cnt 배열에서 하나빼줌
                amax = i
                asort.append(i)
                cnt[i] -= 1
                break # 한번 찾으면 반복문 탈출

        #cnt 배열에서 가장 작은 값을 찾는 반복문
        for i in range(amin, amax):
            if cnt[i]:
                amin = i
                asort.append(i)
                cnt[i] -= 1
                break

    print('#{} {}'.format(tc,' '.join(map(str, asort))))