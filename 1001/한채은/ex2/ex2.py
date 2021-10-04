data = input().split()
def p(data,n):
    if n == len(data):
        print(data)
        return
    for i in range(n,len(data)):
        data[n],data[i] = data[i],data[n]
        p(data,n+1)
        data[n],data[i] = data[i],data[n]
p(data,0)