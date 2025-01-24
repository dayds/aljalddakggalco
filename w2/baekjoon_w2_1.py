n = int(input())

people = set()


for _ in range(n):
    name, status = input().split()
    
    if status == "enter":
        people.add(name)  
    else:
        people.remove(name)  


sorted_people = sorted(people, reverse=True)


for person in sorted_people:
    print(person)
