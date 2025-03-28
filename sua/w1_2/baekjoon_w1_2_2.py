n, l = map(int, input().split()) 

water = list(map(int, input().split()))
water.sort(reverse=False)

i = 0
tape = 0

while i <len(water):
    tape += 1
    start = water[i]
    end = start +l -1
    
    while i <len(water) and water[i] <= end:
        i += 1
        
print(tape)
    
    