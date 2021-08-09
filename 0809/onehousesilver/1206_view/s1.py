import sys
sys.stdin = open('input.txt')

for tc in range(1,11): #입력값이 10개의 테스트 케이스라고 했으니까!
    L = int(input())
    buildings = list(map(int, input().split()))
