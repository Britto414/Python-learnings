def binary_search(arr,x,leftbias):
    i=-1
    l=0
    r=len(arr)-1
    while l<=r:
        mid=(l+r)//2
        if arr[mid]==x:
            i=mid
            if leftbias:
                r=mid-1
            else:
                l=mid+1

        elif arr[mid]>x:
            r=mid-1
        else:
            l=mid+1

    return i

def find(arr,n,x):
    # code here
    left=binary_search(arr, x, True)
    right=binary_search(arr, x, False)
    return left,right

if __name__=="__main__":
    print(find(arr=[1,1,1,2,3],n=4,x=1))