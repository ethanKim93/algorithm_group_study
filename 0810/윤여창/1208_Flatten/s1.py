import sys
sys.stdin = open('input.txt')
                                              #정답이 안 나왔습니다ㅠㅠ. 했던 곳까지 제출하겠습니다.
for tc in range(1, 11):

    dump = int(input())                               #dump와 상자높이 기본 설정
    box_h = list(map(int, input().split()))

    for k in range(dump):
        for i in range(len(box_h)):
            if i == 0:
                max_num = min_num = box_h[i]                    #비교를 위해서 첫번째 박스 상자와 인덱스 설정
                max_idx = min_idx = i
            else:
                if max_num >= box_h[i]:
                    if min_num > box_h[i]:
                        min_num = box_h[i]
                        min_idx = i
                else:
                    max_num = box_h[i]
                    max_idx = i                            #if문을 계속 돌면서 최대랑 최소 경우의 수를 찾고
                    if min_num > box_h[i]:                 #그 값의 인덱스 역시 함께 수정하면서 변경
                        min_num = box_h[i]
                        min_idx = i
        if box_h[max_idx] == box_h[min_idx]:           # 가장 높은 상자와 가장 낮은 상자가 만약 같아버리는 경우까지 오면
                break                                      # 더이상 dump를 할 필요가 없으니 브레이크로 종료
        box_h[max_idx] = max_num - 1
        box_h[min_idx] = min_num + 1                   #그런게 아니라면 제일 높은 상자에서 한칸 빼고, 그걸 낮은곳에 토스

    result = box_h[max_idx] - box_h[min_idx]

    print('#{} {}'.format(tc, result))