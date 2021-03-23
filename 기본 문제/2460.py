'''
기차안에 사람이 가장 많을 때의 사람 수



'''

people = []
Max = 0

for i in range(10):
    #0  32
    #3  13
    Out, In = map(int,input().split())
    

    Max -= Out
    Max += In

    people.append(Max)

print(max(people)) 
    



