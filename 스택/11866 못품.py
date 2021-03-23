'''
요세푸스의 문제

N , K N개의 수열에서 K번째 숫자를 하나씩 빼옴 그 숫자들을 나열해라

'''

from collections import deque

n = 7 ; k = 3


stack=deque()

for i in range(1,n+1):
    stack.append(i)

#stack 1 2 3 4 5 6 7
# 1 2 4 5 6 7
# 1 2 4 5 7
# 1 4 5 7
# 1 4 5
# 1 4
stack = [1,2,3,4,5,6,7]
# 2 
space = k-1
result =[]
for s in range(len(stack)):
    
    print(s)
    print(stack)
    if space < len(stack):

        result.append(stack.pop(space))
        print(space)
        space += k-1

    elif space >= len(stack):

        
        space = space % len(stack)
        result.append(stack.pop(space))
        space += k-1

print(result)
# 다음으로 넘어가는 수 만큼  space = space % len(stack) 나머지값