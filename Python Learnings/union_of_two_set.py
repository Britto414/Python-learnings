# Input: 
# n = 5, arr1[] = {1, 2, 3, 4, 5}  
# m = 3, arr2 [] = {1, 2, 3}
# Output: 1 2 3 4 5
# Explanation: Distinct elements including 
# both the arrays are: 1 2 3 4 5.

a=[1,2,3,4,5]
b=[3]
n=len(a)
m=len(b)



def mergeArrays(a, b, n, m): 
    union_li = list()
    i,j = 0,0
    
    #Using two pointers i and j over the two arrays which helps
    #in storing the smaller element.
    while i < n and j < m: 
        
        #Updating the pointer i until we have identical 
        #elements at consecutive position in a.
        while i+1<n and a[i+1]==a[i]:
            i+=1
            
        #Updating the pointer j until we have identical 
        #elements at consecutive position in b.
        while j+1<m and b[j+1]==b[j]:
            j+=1
            
        #Comparing element of the arrays a and b at pointers
        #i and j and accordingly storing the smaller element
        #and updating the pointers.
        if a[i] < b[j]: 
            union_li.append(a[i])
            i += 1
        elif b[j] < a[i]: 
            union_li.append(b[j])
            j+= 1
        else: 
            #If a[i] is same as b[j], we update both pointers.
            union_li.append(b[j])
            j += 1
            i += 1
  
    #Storing the remaining elements of first array (if there are any).
    while i < n: 
        #Updating the pointer i until we have identical 
        #elements at consecutive position in a.
        while i+1<n and a[i+1]==a[i]:
            i+=1
            
        #Storing the elements.   
        union_li.append(a[i])
        i += 1
        
    #Storing the remaining elements of second array (if there are any).
    while j < m:
        #Updating the pointer j until we have identical 
        #elements at consecutive position in b.
        while j+1<m and b[j+1]==b[j]:
            j+=1
            
        #Storing the elements.    
        union_li.append(b[j]) 
        j += 1
        
    #returning the list containing the union of the two arrays.
    return union_li

print(mergeArrays(a, b, n, m))