import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    P,Pa,Pb = map(int,input().split())

    # A의 이진탐색
    start = 1
    end = P
    cnt_a = 0
    flag = True
    while flag:
         cnt_a += 1
         middle = (start + end)//2
         if middle == Pa:
              flag =False
         elif middle > Pa:
              end = middle
         else:
              start = middle
         if middle == end -1:
              flag = False

     #B의 이진 탐색
    start = 1
    end = P
    cnt_b = 0
    flag = True
    while flag:
         cnt_b += 1
         middle = (start + end) // 2
         if middle == Pb:
              flag =False
         elif middle > Pb:
              end = middle
         else:
              start = middle
         if middle == end -1:
               flag = False

     # 결과값 출력
         if cnt_a < cnt_b:
              result = 'A'
         elif cnt_a > cnt_b:
              result = 'B'
         else:
              result = 0
    print('#{} {}'.format(tc,result))
