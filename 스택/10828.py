'''

빈리스트에 스택 , 큐
14

'''

num=int(input())
#num=2

stack = []

for _ in range(num):
    command = input()
    if command[0:4]=='push':

        command , num =command.split()    
        stack.append(int(num))
    elif command == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

    elif command == 'size':
        print(len(stack))

    elif command == 'empty':
        if len(stack) == 0 :
            print(1)
        else:
            print(0)
    
    elif command == 'pop':
        if len(stack) ==0:
            print(-1)
        else:
            Pop=stack.pop()
            print(Pop)
