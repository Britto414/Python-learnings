arr=[1 ,8 ,7 ,5 ,6 ,7 ,8 ,7]
n=len(arr)
x = arr[n - 1]
 
for i in range(n - 1, 0, -1):
    arr[i] = arr[i - 1];
     
arr[0] = x;