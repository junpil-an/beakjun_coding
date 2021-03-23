'''
이진수 구하기
테스트 케이스 1
이진수로 만들 단어 13


# '''
T = int(input())
#T =1
for i in range(T):
    num=int(input())
    #num= 14
    cnt=0
    one = ""
    while num != 0:
        
        if num%2 == 0:
            cnt += 1
            num = num//2
            
        elif num%2 !=0 :
            cnt += 1
            one += str(cnt-1)
            num = num//2

        elif num == 1:
            cnt +=1
            #one += str(cnt-1)
            num = 0

    print(' '.join(one))
# T = int(input())
# for _ in range(T):
#    N = bin(int(input()))[2:]
#    for i in range(len(N)):
#        if N[-i-1] == '1':
#            print(i, end = ' ')
           