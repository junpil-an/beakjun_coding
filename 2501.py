'''
n 의 약수 들중 k 번째의 약수 값



'''

n,k =map(int,input().split())

case = []

for i in range(1,n+1):
    if n%i ==0 :
        case.append(i)

        if len(case) == k:
            print(case[k-1])
            break
if len(case) < k:
    print(0)