import sys

sys.stdin = open('input.txt')

for tc in range(1,11):
    view_room = 0  # 조망권 공간 갯수
    width = int(input())  # 가로 길이
    buildings_height = list(map(int, input().split())) #빌딩 높이
    for real_width in range(2, width-2): # 빨간색 제외한 실제 가로 길이
        top_height = buildings_height[real_width-2]  # 제일 높은 빌딩을 우선 5개 배열 중 맨왼쪽으로 줌
        if top_height < buildings_height[real_width-1]:
            top_height = buildings_height[real_width-1]
        if top_height < buildings_height[real_width+1]:   # 각각 if문으로 하나씩 비교
            top_height = buildings_height[real_width+1]
        if top_height < buildings_height[real_width+2]:
            top_height = buildings_height[real_width+2]
        if buildings_height[real_width] > top_height:
            view_room += buildings_height[real_width] - top_height
    print('#{} {}'.format(tc, view_room))