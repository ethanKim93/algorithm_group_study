# https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVF-WqqecDFAWg&lectureSeq=5&contestProbId=AWTLZMRKpsYDFAVT&kataId=

import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    hall = [[0]*10 for _ in range(10)] #전체격자 0으로 초기화
    N = int(input())
    draw = []
    for i in range(N): #색칠 할 값 받기
        draw.append(list(map(int,input().split())))
    #print(draw)

    #빨간색 먼저 칠하기 (1로변환)
    for k in draw:
        r1 = k[0]
        c1 = k[1]
        r2 = k[2]
        c2 = k[3]
        color = k[4]

        r_dir = 1
        c_dir = 1

        if r1 > r2 :
            r_dir = -1
        if c1 > c2 :
            c_dir = -1

        if color == 1:# 색깔이 빨간색일 경우
            for r in range(r1,r2+1,r_dir):
                for c in range(c1,c2+1,c_dir):
                    hall[r][c] = 1

    # 파란색 칠하기
    for k in draw:
        r1 = k[0]
        c1 = k[1]
        r2 = k[2]
        c2 = k[3]
        color = k[4]

        r_dir = 1
        c_dir = 1

        if r1 > r2 :
            r_dir = -1
        if c1 > c2 :
            c_dir = -1

        if color == 2:# 색깔이 파란색일 경우
            for r in range(r1,r2+1,r_dir):
                for c in range(c1,c2+1,c_dir):
                    if hall[r][c] > 0: #파란색 중복방지
                        hall[r][c] *= -1

    #겹치는 부분 확인
    cnt = 0
    for i in range(len(hall)):
        for j in range(len(hall)):
           if hall[i][j] == -1:
               cnt += 1

    print('#{} {}'.format(tc,cnt))