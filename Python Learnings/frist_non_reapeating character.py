arr=[12,0,0]
n=len(arr)


ans=9999999999999
#dictionary to hold key value pair.
d=dict()

#iterating over the array.
for i,e in enumerate(arr):
    if e in d:
        #if d[e]<ans and ans is not equal to -1, we store the index.
        if d[e]<ans :
            ans=d[e]
    else:
        d[e]=i

#returning the position of the first repeating element or -1. 
if ans!=9999999999999:
    print(ans+1)
else:
    print(-1)