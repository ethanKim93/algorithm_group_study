import sys
sys.stdin = open("sample_input.txt")


for tc in range(1,int(input())+1):
    matrix = []
    for _ in range(5):
        mat = list(map(str,input().split()))
        mat.append(0)
        matrix.append(mat)
    matrix.append([0]*5)


    result = ''
    for i in range(5):
        for j in range(5):
            try:
                a = matrix[j][i]
                result += matrix[j][i]
            except:
                pass

    print(result)