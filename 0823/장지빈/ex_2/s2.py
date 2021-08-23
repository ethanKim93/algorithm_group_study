#재귀 백트래킹
def f(i, N):
    if i == N:		#순열 완성
    	print(P)
    else:			#i번 원소값 결정
        for j in range(i, N): 	#자신부터 오른쪽 원소와 교환
            P[i], P[j] = P[j], P[i]
            f(i+1, N)
            P[i], P[j] = P[j], P[i]

P = [1, 2, 3]
f(0, len(P))