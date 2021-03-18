'''
피보나치 함수 구하기
첫째줄에 갯수 T개
N은 40보다 작거나 같은 자연수 or 0
0 일때 0은 1번 0
1 일때 0은 0번 1은 1번 0 1
3 일때 0은 1번 1은 2번 0 1 1 2

문제 설명 그지같음 ㅡㅡ

'''


#List = [1,2,3,4,1]
#print(' '.join(map(str,List)))
#print(str(List.count(1)))


# a= [0,1]
# N=input()
# for i in range(N-2):
#     a.append(a[-1]+a[-2])

# print(a)
# print(a[-3:])
 
for i in range(int(input())):
    b=[0,1]

    N=int(input())
    if N ==0 :
        print("1 0")
    elif N ==1 :
        print("0 1")
    elif N ==2 :
        print("1 1")
    else:
        for i in range(N-1):
            b.append(b[-1]+b[-2])

        print(' '.join(map(str,b[-2:])))
