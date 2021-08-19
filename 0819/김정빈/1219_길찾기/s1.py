import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    T, road = map(int,input().split())
    citys = list(map(int, input().split()))
    arr1 = [0]*100
    arr2 = [0]*100