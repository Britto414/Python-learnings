arr=[1,2,3,5,5,5,5,5,5,5,6,7,7,7]
x=5
def binary_search(arr,x,leftbias):
    l=0
    r=len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]>x:
            r=mid-1
        elif arr[mid]<x:
            l=mid+1
        else:
            i=mid
            if leftbias:
                r=mid-1
            else:
                l=mid+1
    return i

def mxreapeating(arr,x):
    left=binary_search(arr, x, True)
    right=binary_search(arr, x, False)
    return left,right

ans=mxreapeating(arr, x)
print(ans)