def subsets(p,up):
    
    if len(up)==0:
        lst=[]
        lst.append(p)
        return lst
    left=subsets(p+[up[0]],up[1:])
    
    right=subsets(p, up[1:])
    left.extend(right)
    return left

print(subsets([],[1,2,3]))

#permutations
def soln(arr):
    
    def perm(arr):
        res=[]
        if len(arr)==1:
            return [arr]
        for i in range(len(arr)):
            # n=arr.pop(0)
            ans=perm(arr[:i]+arr[i+1:])
            for j in ans:
                j.append(arr[i])
            res.extend(ans)
            # arr.append()

        return res
    return perm(arr)

print(soln(['a','b']))

def perm(p,up):
    if up=="":
        print(p)
        return
    perm(p+up[0], up[1:])
    perm(up[0]+p,up[1:])
    return