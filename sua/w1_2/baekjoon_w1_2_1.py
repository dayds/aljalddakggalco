n=input()
s=n.split('-')

f = sum(map(int, s[0].split('+')))

for i in range(1, len(s)):
    f -= sum(map(int, s[i].split('+')))
    
print(f)
    
    