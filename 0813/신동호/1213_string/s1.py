import sys
sys.stdin = open('test_input.txt','rt', encoding='UTF8')
# brute force 강의 식으로 풀기
T = 10

for tc in range(1, T+1):
    N = int(input())
    words = input()
    sents = input()
    i = 0 # 문장 탐색 인덱스
    j = 0 # 단어 탐색 인덱스
    cnt = 0 # 문장에 들어있는 단어 수
    while i < len(sents): # 마지막 문장 요소까지 조사
        if words[j] != sents[i]: # 문장과 단어 요소 다름
            i = i - j # 문장과 단어 비교 시작했던 지점 초기화
            j = -1 # 단어 인덱스 초기화
        if j == len(words)-1: # 완전 일치
            cnt += 1 # 단어 수 +1
            i = i - j
            j = -1
        i += 1 # 문장 인덱스 증가
        j += 1 # 단어 인덱스 증가

    print('#{} {}'.format(tc,cnt))
