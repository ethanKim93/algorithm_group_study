import sys
sys.stdin=open('input.txt')
binaryarr=input()
k=10
for i in range(0,len(binaryarr),10):
    result=int(binaryarr[i:k+i],2)
    print(result, end='')
