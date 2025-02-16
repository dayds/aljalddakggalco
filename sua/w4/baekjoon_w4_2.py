n = int(input())
list = []

for i in range(n):
    age, name = input().split()
    list.append((int(age), name))
    
list.sort(key=lambda x : x[0])
   
for age, name in list:
           print(age, name)
    