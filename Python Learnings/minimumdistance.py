arr=[1,2,3,2]
n=len(arr)
x = 1 
y = 2
recent_x, recent_y = -1, -1
ans = 9999999

for i in range(n):
    if arr[i]==x:
        recent_x=i
        if recent_y!=-1:
            ans = min(ans, abs(recent_x-recent_y))
    elif arr[i]==y:
        recent_y=i
        if recent_x!=-1:
            ans = min(ans, abs(recent_x-recent_y))
    
if ans==9999999:
    print(-1) 
else:
    print(ans)