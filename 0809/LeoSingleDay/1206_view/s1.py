for tc in range(1, 11):
    L = int(input())
    bu = list(map(int, input().split()))
    #결과값을 저장해줄 result 변수 선언
    result = 0
    for fl in range(2,L-2):
        #max값을 통해 대소비교를 하기위해 앞뒤 두칸의 빌딩 높이를 저장할 asideBu_list를 선언
        asideBu_list = [bu[fl-1],bu[fl-2],bu[fl+1],bu[fl+2]]
        # 방법 1 : 내장함수 사용없이 문제풀이
        maxbu = asideBu_list[0]
        for i in asideBu_list:
            if (i>maxbu):
                maxbu=i
        if( bu[fl] > maxbu):
            result += bu[fl]-maxbu
        # 방법2 (max 내장함수 사용)
        # if( bu[fl] > max(asideBu_list)):
        #     result += bu[fl]-max(asideBu_list)
    print('#{} {}'.format(tc,result))
