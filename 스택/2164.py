'''
카드 2

제일 앞에 있는 수를 버리고 그 다음 수를 빼 맨 뒤로 붙인다

이걸 반복해 최종 남아있는 수

N = 4

'''

from collections import deque

n =int(input())

stack = []

for i in range(1,n+1):
    stack.append(i)

stack=deque(stack)

A =True

while A:
    if len(stack) == 1:
        A = False
    else:
        stack.popleft()
        if len(stack) == 1:
            A = False
        pop = stack.popleft()
        stack.append(pop)


print(stack[0])

# while len(queue) > 1:
#     queue.popleft()
#     queue.append(queue.popleft())