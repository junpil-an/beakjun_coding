'''
3kg , 5kg 봉지 

ex) 18 kg 3kg 6개 5kg3개 3kg 1개 더 효율적

5kg짜리만 일때 참
3kg 빼고 5짜리확인
3kg 빼고 5짜리 확인

3kg짜리만 일때 참

그리고도 답이 업음 -1
'''
N=int(input())
cnt= 0
while True:
    if N%5 == 0:
        print(N//5+cnt)
        break
    N = N-3
    cnt +=1

    if N<0:
        print(-1)
        break
