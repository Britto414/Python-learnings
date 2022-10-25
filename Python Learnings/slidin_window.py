arr=[1,2,1,2,1]
t=7
# n=len(arr)
res=99999999
l=0
total=0
res=float("inf")

for r in range(len(arr)):
    total+=arr[r]
    while total>=t:
        if total==t:
            res=min(r-l+1,res)
        total-=arr[l]
        l+=1
print(res)
