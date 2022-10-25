a=[2,4,1,3,5]


big1 = -1
big2 = -1
big3 = -1

for i in a:
    if i > big3:
        big3 = i
    
    if big3 > big2:
        big2, big3 = big3, big2
    
    if big2 > big1:
        big1, big2 = big2, big1

print(big3)