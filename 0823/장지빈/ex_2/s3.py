arr = [1,2,3]
N = len(arr)
sel = [0] * N       # 방문 여부를 저장할 sel 리스트    #[0, 0, 0]

def powerset(idx):
    if idx == N:        #위에 있어야 3번 인덱스에 더이상 접근하지 않는다
        for index, i in enumerate(sel):
            if i:
                print(arr[index], end=' ')
        print()
        return
    sel[idx] = 1        # 사용 여부에 들어온 idx 사용 체크
    powerset(idx+1)
    sel[idx] = 0
    powerset(idx+1)
powerset(0)     #0 번 인덱스부터 시작


#
#1  1, 0, 0       2  [1, 1, 0]        3 [1, 1, 1]      6 [1, 0, 1]
#  powerset(1)       powerset(2)         powerset(3)     powerset(3)
#4 [1, 1, 0]     5  [1, 0, 0]         7  [1, 0, 0]
#  powerset(3)      powerset(2)         powerset(3)