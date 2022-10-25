def maxSubArraySum(arr,n): 
       
    max_so_far = -9999999 - 1
    max_ending_here = 0
    
    #Iterating over the array. 
    for i in range(0,n): 
        #Updating max sum till current index.
        max_ending_here = max_ending_here + arr[i]
        
        #Storing max sum so far by choosing maximum between max 
        #sum so far and max sum till current index.
        if (max_so_far < max_ending_here): 
            max_so_far = max_ending_here 
    
        #If max sum till current index is negative, we do not need to add
        #it to result so we update it to zero.
        if max_ending_here < 0: 
            max_ending_here = 0   
    
    #returning the result.
    return max_so_far

def maxSubArraySum1(arr,n):
    ##Your code here\
    maxsum=arr[0]
    cursum=0
    for i in arr:
        cursum=max(cursum+i,i)
        # cursum+=i
        maxsum=max(maxsum,cursum)
    return maxsum

arr=[1,2,3,-1,5,15]
n=len(arr)
ans=maxSubArraySum1(arr,n)
print(ans)