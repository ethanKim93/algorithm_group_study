
def select(li,i):
    if i == len(li)-1:
        return
    else:
        minI = i
        for j in range(i+1,len(li)):
            if li[j] < li[minI]:
                minI = j
        # 해당 범위에서의 최소값과 i번째 값 교환
        li[minI], li[i] = li[i], li[minI]
        select(li,i+1)



