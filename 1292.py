'''

수열의 합
ex) 1 2 2 3 3 3 4 4 4 4 ...
특정 구간의 합
'''

Min, Max = map(int,input().split()) 
n=[]


for i in range(1,1000):

    for j in range(i):
        n.append(i)
    
    # if len(n) > Max+1:
    #     break

#print(n)
n= n[Min-1:Max]
print(sum(n))
