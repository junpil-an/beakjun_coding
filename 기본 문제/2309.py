'''

9명의 난쟁이중 7명을 구하라(합이 100임)

'''

# people= []
# for i in range(9):
#     people.append(int(input()))

people = [20, 7, 23, 19, 10, 15, 25, 8, 13]
Sum = sum(people)

Sub =[]
for i in range(8):
    for j in range(i+1,9):
        
        if Sum - (people[i]+people[j]) == 100:
            
            Sub.append(people[i])
            Sub.append(people[j])
            break
people.remove(Sub[0])
people.remove(Sub[1])        
people = sorted(people)
for i in range(len(people)):
    print(people[i])

# index 로 pop
people.pop(1)
print(people)