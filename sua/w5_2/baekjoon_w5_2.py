n= int(input())
weight = []

for _ in range(n):
   weight.append(int(input()))

weight.sort()

max_weight = 0
for i in range(n):
   l = weight[i] * (n-i)
   if l > max_weight:
      max_weight = l

print(max_weight)