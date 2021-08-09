import sys
sys.stdin=open('input.txt')

for tc in range(1,11):
    N=int(input())
    buildings=list(map(int,input().split()))
    print(N)
    print(buildings)
    