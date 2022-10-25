# Given a sorted array A[] of size N, delete all the duplicated elements from A[].Update the array 
# such that if there are X distinct elements in it then the first X positions of the array should be 
# filled with them in increasing order.

# Note: Don't use set or HashMap to solve the problem.

#my solution

def remove_duplicate(a, n):
	# code here
	count=0
	l=0
	r=1
	while r<len(a):
	    
	    if a[l]==a[r]:
	        a.remove(a[r])
	       
	    else:
	        l+=1
	        r+=1
	for i in a:
	    count+=1
	return count

#Authors solution
def remove_duplicate1(a,n):
    i = 0
    for j in range(1,n):
        if a[i] != a[j]:
            i+=1
            a[i] = a[j]
    return (i+1)

if __name__=="__main__":
    a=[1,1,2,2,3,4]
    n=len(a)
    print(remove_duplicate(a, n))
print("sucess")
