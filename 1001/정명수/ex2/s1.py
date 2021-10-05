data = list(map(int,input().split()))
baby_gin = 0
def baby(data):
    triplet = 0
    run = 0
    for i in range(2):
        if data[i*3] == data[i*3+1] == data[i*3+2]:
            triplet += 1
        elif data[i*3]+2 == data[i*3+1]+1 == data[i*3+2]:
            run += 1
    if triplet + run == 2:
        return True
    return False
def p(data,n):
    global baby_gin
    if n == len(data):
        if baby(data):
            baby_gin = 1
        return
    for i in range(n,len(data)):
        data[n],data[i] = data[i],data[n]
        p(data,n+1)
        data[n],data[i] = data[i],data[n]
p(data,0)

print(baby_gin)