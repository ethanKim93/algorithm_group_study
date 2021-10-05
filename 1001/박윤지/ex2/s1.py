# 6자리 숫자에 대해서 완전 검색을 적용해서 Baby-gin을 검사해보시오.

def makeP(n, k):  # n은 6으로 고정되어야하는 함수
    if k == n:
        babygin(arr)
        # 밑처럼 하면 처음 리스트 그대로 들어가는데 왜 그런지 모르겠음
        # global p
        # p.append(arr)

    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            makeP(n, k+1)
            arr[k], arr[i] = arr[i], arr[k]

# babygin 검사
def babygin(arr):
    global flag
    aTriple = arr[0] == arr[1] == arr[2]
    aRun = arr[0] +2 == arr[1] +1 == arr[2]
    bTriple = arr[3] == arr[4] == arr[5]
    bRun = arr[3] +2 == arr[4] +1 == arr[5]
    if (aTriple and bTriple) or (aTriple and bRun) or (aRun and bTriple) or (aRun and bRun):
        flag = 1
        return
    # else: flag = 0 하면 맨 마지막으로 만들어지는 순열 기준으로 flag가 정해진다.


arr = [6, 6, 7, 7, 6, 7]
arr = [1, 3, 5, 6, 7, 3]

flag = 0
makeP(6, 0)

if flag:
    print('baby-gin')
else:
    print('lose')
    
    
#####################################
#2. count 정렬을 이용해서 완전탐색으로 풀 수도 있음 (알고리즘 깃랩 참조)